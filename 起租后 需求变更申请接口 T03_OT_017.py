import requests
import unittest
import json
from env_config import Base64Util  # 导入环境配置
from env_config import TokenGenerator
from env_config import GetCurrentTime
from env_config import EnvConfig  # 导入环境配置
from env_config import SoapResponseHandle  # 导入环境配置
from xml.etree import ElementTree as ET


class DemandChangeApplyAfterRent(unittest.TestCase):
    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/services/DemandChangeApplyAfterRent"
    WSDL_URL = f"{base_url}/services/DemandChangeApplyAfterRent?wsdl"  # WSDL地址
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': ''    # 替换为实际的SOAPAction
    }

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        # 实例级别的参数，可以在所有方法中使用
        self.CUST_COMPANY = "1002"  # 客户公司代码
        self.SERVICE_CODE = "T03_OT_017"  # 服务代码

    def generate_request_xml(self,cust_company,service_code,access_token,request_time):
        """生成请求XML内容"""
        return f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <PACKET>
            <HEAD>
            <CUST_COMPANY>{cust_company}</CUST_COMPANY>
            <SERVICE_CODE>{service_code}</SERVICE_CODE>
            <ACCESS_TOKEN>{access_token}</ACCESS_TOKEN>
            <REQUEST_TIME>{request_time}</REQUEST_TIME>
            </HEAD>
            <BODY>
            <PROVINCE_CODE>110000</PROVINCE_CODE>
            <REGION_CODE>110200</REGION_CODE>
            <COUNTY_CODE>110201</COUNTY_CODE>
            <REQUEST_ID>待确认</REQUEST_ID>
            <APPLY_ID>BJ-W-2025051202233T</APPLY_ID>
            <REQUEST_TYPE>4</REQUEST_TYPE>
            <CUST_COMPANY>1002</CUST_COMPANY>
            <SYS_REQUEST_TIME>2025-05-12 15:46:31</SYS_REQUEST_TIME>
            <APPLY_BATCH>S25051200002</APPLY_BATCH>
            <MODIFY_SOURCE>01</MODIFY_SOURCE>
            <EFFECTIVE_DATE>2025-05-01 00:00:00</EFFECTIVE_DATE>
            <CHANGE_REASON>维护费</CHANGE_REASON>
            <IS_TRACE>0</IS_TRACE>
            <TRACE_REASON></TRACE_REASON>
            <CHANGE_FEE>652.97</CHANGE_FEE>
            <COMPONENT_ID>200132</COMPONENT_ID>
            <OPERATOR>杨帆</OPERATOR>
            <LINKTEL>13601174201</LINKTEL>
            <RESULT>1</RESULT>
            <OPINION_INFO></OPINION_INFO>
            <CONFIRMOR>李江元</CONFIRMOR>
            <CONFIRM_DATE>2025-05-27 13:56:08</CONFIRM_DATE>
            </BODY>
            </PACKET>
        """

    def build_soap_envelope(self, request_xml):
        """构建SOAP信封"""
        return f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                          xmlns:web="http://webservice.service.sys.org/">
           <soapenv:Header/>
           <soapenv:Body>
              <web:DemandChangeApplyAfterRent>
                <encReqXml>{request_xml}</encReqXml>
              </web:DemandChangeApplyAfterRent>
           </soapenv:Body>
        </soapenv:Envelope>
        """

    def test_demandChangeApplyAfterRent_LT(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code=self.SERVICE_CODE,
                                                access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY, self.SERVICE_CODE),
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # # 解析请求XML
            # request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            # request_head = request_root.find('HEAD')

            # 解析业务响应XML
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # # 1. 检查REQUEST_ID是否一致
            # request_id_request = request_body.find('REQUEST_ID').text
            # request_id_response = response_body.find('REQUEST_ID').text
            # assert request_id_response == request_id_request, f"REQUEST_ID不匹配: 响应={request_id_response}, 期望={request_id_request}"
            #
            # # 2. 检查SYNC_RESULT是否为1
            # sync_result = response_body.find('SYNC_RESULT').text
            # assert sync_result == '1', f"SYNC_RESULT应为1, 实际为{sync_result}"

            # # 3. 检查FAIL_MESSAGE是否为空（待确认联通实际返回为空还是无此字段）
            # fail_message = response_body.find('FAIL_MESSAGE').text
            # assert fail_message is None or fail_message == '', "FAIL_MESSAGE应为空"

            # 4. 检查RESPONSE_CODE是否为000000
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000000', f"RESPONSE_CODE应为000000, 实际为{response_code}"

            # # 5. 检查RESPONSE_MSG是否为空（待确认联通实际返回为空还是无此字段）
            # response_msg = response_head.find('RESPONSE_MSG').text
            # assert response_msg is None or response_msg == '', "RESPONSE_MSG应为空"

            # # 6. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            # for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
            #     request_value = request_head.find(tag).text
            #     response_value = response_head.find(tag).text
            #     assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"
            #
            # # 7. 检查RESPONSE_TIME是否不为空
            # response_time = response_head.find('RESPONSE_TIME').text
            # assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_lackToken(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code=self.SERVICE_CODE,
                                                access_token="",
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【访问令牌】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【访问令牌】不能为空', f"RESPONSE_MSG应为【访问令牌】不能为空, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
                request_value = request_head.find(tag).text
                response_value = response_head.find(tag).text
                assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

            # 4. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_lackCustCompany(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company="",
                                                service_code=self.SERVICE_CODE,
                                                access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY, self.SERVICE_CODE),
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            # response_packet = SoapResponseHandle.process_soap_response(response.text)
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【运营商编码】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【运营商编码】不能为空', f"RESPONSE_MSG应为【运营商编码】不能为空, 实际为{response_msg}"

            # 3. 检查SERVICE_CODE与请求的SERVICE_CODE一致
            request_service_code = request_head.find('SERVICE_CODE').text
            response_service_code = response_head.find('SERVICE_CODE').text
            assert response_service_code == request_service_code, f"SERVICE_CODE不匹配: 响应={response_service_code}, 请求={request_service_code}"

            # 4. 检查CUST_COMPANY是否为空
            response_cust_company = response_head.find('CUST_COMPANY').text
            assert response_cust_company is None or response_cust_company == '', "CUST_COMPANY应为空"

            # 5. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_lackServiceCode(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code="",
                                                access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY, self.SERVICE_CODE),
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            # response_packet = SoapResponseHandle.process_soap_response(response.text)
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【服务代码】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【服务代码】不能为空', f"RESPONSE_MSG应为【服务代码】不能为空, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY与请求的CUST_COMPANY一致
            request_cust_company = request_head.find('CUST_COMPANY').text
            response_cust_company = response_head.find('CUST_COMPANY').text
            assert response_cust_company == request_cust_company, f"CUST_COMPANY不匹配: 响应={response_cust_company}, 请求={request_cust_company}"

            # 4. 检查SERVICE_CODE是否为空
            response_service_code = response_head.find('SERVICE_CODE').text
            assert response_service_code is None or response_service_code == '', "SERVICE_CODE应为空"

            # 5. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_lackRequestTime(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code=self.SERVICE_CODE,
                                                access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY, self.SERVICE_CODE),
                                                request_time="").strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            # response_packet = SoapResponseHandle.process_soap_response(response.text)
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【请求时间】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【请求时间】不能为空', f"RESPONSE_MSG应为【请求时间】不能为空, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
                request_value = request_head.find(tag).text
                response_value = response_head.find(tag).text
                assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

            # 4. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_errorToken(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code=self.SERVICE_CODE,
                                                access_token="123123",
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            # response_packet = SoapResponseHandle.process_soap_response(response.text)
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000001
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000001', f"RESPONSE_CODE应为000001, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【访问令牌】不正确
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【访问令牌】不正确', f"RESPONSE_MSG应为【访问令牌】不正确, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
                request_value = request_head.find(tag).text
                response_value = response_head.find(tag).text
                assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

            # 4. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

    def test_demandChangeApplyAfterRent_otherServiceCode(self):
        """铁塔终止确认SOAP接口测试"""
        # 1. 准备测试数据
        request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                service_code='T09_OT_013',
                                                access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY, self.SERVICE_CODE),
                                                request_time=GetCurrentTime.get_current_time()).strip()
        request_xml_decode = Base64Util.encode_string(request_xml)
        soap_request = self.build_soap_envelope(request_xml_decode)

        try:
            # 2. 发送SOAP请求
            response = requests.post(
                url=self.BASE_URL,
                data=soap_request.encode('utf-8'),
                headers=self.headers
            )

            # 3. 验证基础响应
            self.assertEqual(response.status_code, 200,
                             f"响应状态码应为200，实际为{response.status_code}")
            self.assertIn("text/xml", response.headers["Content-Type"],
                          "响应Content-Type应为text/xml")

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            # request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析业务响应XML
            # response_packet = SoapResponseHandle.process_soap_response(response.text)
            response_packet = SoapResponseHandle.get_return_xml_value(response.text)
            # response_body = response_packet.find('BODY')
            response_head = response_packet.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000006
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000006', f"RESPONSE_CODE应为000006, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为请求服务与【服务编码】不匹配！
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '请求服务与【服务编码】不匹配！',\
                f"RESPONSE_MSG应为请求服务与【服务编码】不匹配！, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
                request_value = request_head.find(tag).text
                response_value = response_head.find(tag).text
                assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

            # 4. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("SOAP接口测试通过！")

        except requests.exceptions.RequestException as e:
            self.fail(f"SOAP请求失败: {e}")
        except ET.ParseError as e:
            self.fail(f"XML解析错误: {e}")

if __name__ == '__main__':
    unittest.main()