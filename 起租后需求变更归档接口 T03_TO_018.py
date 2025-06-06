import requests
import unittest
import json
from env_config import EnvConfig  # 导入环境配置
from env_config import GetCurrentTime
from env_config import TokenGenerator
from xml.etree import ElementTree as ET

class TestOrderStatusQueryTO(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/crm/demandChangePigeonholeAfterRent"
    # BASE_URL = "http://120.52.40.45:48080/crm/demandChangePigeonholeAfterRent"   #接口地址
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/xml"
    }

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        # 实例级别的参数，可以在所有方法中使用
        self.CUST_COMPANY = "1001"  # 客户公司代码
        self.SERVICE_CODE = "T03_TO_018"  # 服务代码

    def generate_request_xml(self,cust_company,service_code,access_token,request_time):
        """生成请求XML内容"""
        return (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<CUST_COMPANY>{cust_company}</CUST_COMPANY>'
            f'<SERVICE_CODE>{service_code}</SERVICE_CODE>'
            f'<ACCESS_TOKEN>{access_token}</ACCESS_TOKEN>'
            f'<REQUEST_TIME>{request_time}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<EFFECTIVE_DATE>2025-05-01</EFFECTIVE_DATE>'
            '<CHANGE_RESULT>1</CHANGE_RESULT>'
            '<REGION_CODE>410100</REGION_CODE>'
            '<CHANGE_BATCH>T1508696594</CHANGE_BATCH>'
            '<CUST_COMPANY>1001</CUST_COMPANY>'
            '<CHANGE_INFO>100110|0.0</CHANGE_INFO>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>410000</PROVINCE_CODE>'
            '<IS_TRACE>0</IS_TRACE>'
            '<EXECUTION_DATE>/n/t/s~！@#￥%……&*（）——+：“|？》《!@#$%^&*())_+:"|?></EXECUTION_DATE>'
            '<APPLY_ID>T2025053100311828562</APPLY_ID>'
            '<CHANGE_SOURCE>04</CHANGE_SOURCE>'
            '<REQUEST_TYPE>1</REQUEST_TYPE>'
            '<COUNTY_CODE>410105</COUNTY_CODE>'
            '</BODY>'
            '</PACKET>'
        )

    def test_orderStatusQueryTO_DX(self):
        #数据库响应日志
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<BODY>'
        #     '<REQUEST_ID>1221011409771816</REQUEST_ID>'
        #     '<SYNC_RESULT>1</SYNC_RESULT>'
        #     '<FAIL_MESSAGE></FAIL_MESSAGE>'
        #     '</BODY>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000000</RESPONSE_CODE>'
        #     '<RESPONSE_MSG></RESPONSE_MSG>'
        #     '<CUST_COMPANY>1003</CUST_COMPANY>'
        #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-31 18:39:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '</PACKET>'
        # )
        try:
            request_xml = self.generate_request_xml(cust_company='1003',
                                                    service_code=self.SERVICE_CODE,
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            # request_root = ET.fromstring(expected_request_xml)
            # request_body = request_root.find('BODY')
            # request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            # response_body = response_root.find('BODY')
            response_head = response_root.find('HEAD')

            # # 1. 检查REQUEST_ID是否一致
            # request_id_request = request_body.find('REQUEST_ID').text
            # request_id_response = response_body.find('REQUEST_ID').text
            # assert request_id_response == request_id_request, f"REQUEST_ID不匹配: 响应={request_id_response}, 期望={request_id_request}"
            #
            # # 2. 检查SYNC_RESULT是否为1
            # sync_result = response_body.find('SYNC_RESULT').text
            # assert sync_result == '1', f"SYNC_RESULT应为1, 实际为{sync_result}"
            #
            # # 3. 检查FAIL_MESSAGE是否为空
            # fail_message = response_body.find('FAIL_MESSAGE').text
            # assert fail_message is None or fail_message == '', "FAIL_MESSAGE应为空"

            # 4. 检查RESPONSE_CODE是否为000000
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000000', f"RESPONSE_CODE应为000000, 实际为{response_code}"

            # # 5. 检查RESPONSE_MSG是否为空
            # response_msg = response_head.find('RESPONSE_MSG').text
            # assert response_msg is None or response_msg == '', "RESPONSE_MSG应为空"
            #
            # # 6. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            # for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
            #     request_value = request_head.find(tag).text
            #     response_value = response_head.find(tag).text
            #     assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"
            #
            # # 7. 检查RESPONSE_TIME是否不为空
            # response_time = response_head.find('RESPONSE_TIME').text
            # assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_orderStatusQueryTO_YD(self):
        #数据库响应日志
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<CUST_COMPANY>1001</CUST_COMPANY>'
        #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-29 14:55:00</RESPONSE_TIME>'
        #     '<RESPONSE_MSG></RESPONSE_MSG>'
        #     '<RESPONSE_CODE>000000</RESPONSE_CODE>'
        #     '</HEAD>'
        #     '<BODY>'
        #     '<REQUEST_ID>1015071501503108</REQUEST_ID>'
        #     '<SYNC_RESULT>1</SYNC_RESULT>'
        #     '<FAIL_MESSAGE></FAIL_MESSAGE>'
        #     '</BODY>'
        #     '</PACKET>'
        # )
        try:
            request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                    service_code=self.SERVICE_CODE,
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            # request_root = ET.fromstring(expected_request_xml)
            # request_body = request_root.find('BODY')
            # request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            # response_body = response_root.find('BODY')
            response_head = response_root.find('HEAD')

            # # 1. 检查REQUEST_ID是否一致
            # request_id_request = request_body.find('REQUEST_ID').text
            # request_id_response = response_body.find('REQUEST_ID').text
            # assert request_id_response == request_id_request, f"REQUEST_ID不匹配: 响应={request_id_response}, 期望={request_id_request}"
            #
            # # 2. 检查SYNC_RESULT是否为1
            # sync_result = response_body.find('SYNC_RESULT').text
            # assert sync_result == '1', f"SYNC_RESULT应为1, 实际为{sync_result}"

            # 3. 检查RESPONSE_CODE是否为000000
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000000', f"RESPONSE_CODE应为000000, 实际为{response_code}"

            # # 4. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            # for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
            #     request_value = request_head.find(tag).text
            #     response_value = response_head.find(tag).text
            #     assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"
            #
            # # 5. 检查RESPONSE_TIME是否不为空
            # response_time = response_head.find('RESPONSE_TIME').text
            # assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    # def test_orderStatusQueryTO_lackToken(self):
    #
    #     # # 预期实际报错返回结果
    #     # expected_response_xml = (
    #     #     '<?xml version="1.0" encoding="UTF-8"?>'
    #     #     '<PACKET>'
    #     #     '<HEAD>'
    #     #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
    #     #     '<RESPONSE_MSG>【访问令牌】不能为空</RESPONSE_MSG>'
    #     #     '<CUST_COMPANY>1001</CUST_COMPANY>'
    #     #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
    #     #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
    #     #     '</HEAD>'
    #     #     '<BODY/>'
    #     #     '</PACKET>'
    #     # )
    #
    #     try:
    #         request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
    #                                                 service_code=self.SERVICE_CODE,
    #                                                 access_token='',
    #                                                 request_time=GetCurrentTime.get_current_time()).strip()
    #         response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
    #         # 断言测试
    #         self.assertEqual(response.status_code, 200,
    #                          f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
    #         self.assertIn("application/xml", response.headers["Content-Type"])
    #
    #         # 解析请求XML
    #         request_root = ET.fromstring(request_xml)
    #         request_head = request_root.find('HEAD')
    #
    #         # 解析响应XML
    #         response_root = ET.fromstring(response.text)
    #         response_head = response_root.find('HEAD')
    #
    #         # 1. 检查RESPONSE_CODE是否为000004
    #         response_code = response_head.find('RESPONSE_CODE').text
    #         assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"
    #
    #         # 2. 检查RESPONSE_MSG是否为【访问令牌】不能为空
    #         response_msg = response_head.find('RESPONSE_MSG').text
    #         assert response_msg == '【访问令牌】不能为空', f"RESPONSE_MSG应为【访问令牌】不能为空, 实际为{response_msg}"
    #
    #         # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
    #         for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
    #             request_value = request_head.find(tag).text
    #             response_value = response_head.find(tag).text
    #             assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"
    #
    #         # 4. 检查RESPONSE_TIME是否不为空
    #         response_time = response_head.find('RESPONSE_TIME').text
    #         assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"
    #
    #         print("测试通过！")
    #     except requests.exceptions.RequestException as e:
    #         print(f"请求失败: {e}")

    def test_orderStatusQueryTO_lackCustCompany(self):
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【运营商编码】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY></CUST_COMPANY>'   #可能为空也可能为Null
        #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )

        try:
            request_xml = self.generate_request_xml(cust_company='',
                                                    service_code=self.SERVICE_CODE,
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_head = response_root.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【运营商编码】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【运营商编码】不能为空', f"RESPONSE_MSG应为【运营商编码】不能为空, 实际为{response_msg}"

            # # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            # for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
            #     request_value = request_head.find(tag).text
            #     response_value = response_head.find(tag).text
            #     assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

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

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_orderStatusQueryTO_lackServiceCode(self):
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【服务代码】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1001</CUST_COMPANY>'
        #     '<SERVICE_CODE></SERVICE_CODE>'   #可能为空，也可能为Null
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )

        try:
            request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                    service_code='',
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_head = response_root.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000004
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000004', f"RESPONSE_CODE应为000004, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为【服务代码】不能为空
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '【服务代码】不能为空', f"RESPONSE_MSG应为【服务代码】不能为空, 实际为{response_msg}"

            # # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            # for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
            #     request_value = request_head.find(tag).text
            #     response_value = response_head.find(tag).text
            #     assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

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

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_orderStatusQueryTO_lackRequestTime(self):
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【请求时间】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1001</CUST_COMPANY>'
        #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )

        try:
            request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                    service_code=self.SERVICE_CODE,
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time='')
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_head = response_root.find('HEAD')

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

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    # def test_orderStatusQueryTO_errorToken(self):
    #
    #     # # 预期实际报错返回结果
    #     # expected_response_xml = (
    #     #     '<?xml version="1.0" encoding="UTF-8"?>'
    #     #     '<PACKET>'
    #     #     '<HEAD>'
    #     #     '<RESPONSE_CODE>000001</RESPONSE_CODE>'
    #     #     '<RESPONSE_MSG>【访问令牌】不正确</RESPONSE_MSG>'
    #     #     '<CUST_COMPANY>1001</CUST_COMPANY>'
    #     #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
    #     #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
    #     #     '</HEAD>'
    #     #     '<BODY/>'
    #     #     '</PACKET>'
    #     # )
    #
    #     try:
    #         request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
    #                                                 service_code=self.SERVICE_CODE,
    #                                                 access_token='123123',
    #                                                 request_time=GetCurrentTime.get_current_time()).strip()
    #         response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
    #         # 断言测试
    #         self.assertEqual(response.status_code, 200,
    #                          f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
    #         self.assertIn("application/xml", response.headers["Content-Type"])
    #
    #         # 解析请求XML
    #         request_root = ET.fromstring(request_xml)
    #         request_head = request_root.find('HEAD')
    #
    #         # 解析响应XML
    #         response_root = ET.fromstring(response.text)
    #         response_head = response_root.find('HEAD')
    #
    #         # 1. 检查RESPONSE_CODE是否为000001
    #         response_code = response_head.find('RESPONSE_CODE').text
    #         assert response_code == '000001', f"RESPONSE_CODE应为000001, 实际为{response_code}"
    #
    #         # 2. 检查RESPONSE_MSG是否为【访问令牌】不正确
    #         response_msg = response_head.find('RESPONSE_MSG').text
    #         assert response_msg == '【访问令牌】不正确', f"RESPONSE_MSG应为【访问令牌】不正确, 实际为{response_msg}"
    #
    #         # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
    #         for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
    #             request_value = request_head.find(tag).text
    #             response_value = response_head.find(tag).text
    #             assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"
    #
    #         # 4. 检查RESPONSE_TIME是否不为空
    #         response_time = response_head.find('RESPONSE_TIME').text
    #         assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"
    #
    #         print("测试通过！")
    #     except requests.exceptions.RequestException as e:
    #         print(f"请求失败: {e}")

    def test_orderStatusQueryTO_otherCustCompany(self):

        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>999999</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>该接口不支持运营商</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1004</CUST_COMPANY>'
        #     '<SERVICE_CODE>T03_TO_018</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )

        try:
            request_xml = self.generate_request_xml(cust_company='1004',
                                                    service_code=self.SERVICE_CODE,
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_head = response_root.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为999999
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '999999', f"RESPONSE_CODE应为999999, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为该接口不支持运营商
            response_msg = response_head.find('RESPONSE_MSG').text
            response_cust_company=response_head.find('CUST_COMPANY').text
            assert response_msg == f'该接口不支持运营商{response_cust_company}', \
                f"RESPONSE_MSG应为该接口不支持运营商{response_cust_company}, 实际为{response_msg}"

            # 3. 检查CUST_COMPANY、SERVICE_CODE是否与请求一致
            for tag in ['CUST_COMPANY', 'SERVICE_CODE']:
                request_value = request_head.find(tag).text
                response_value = response_head.find(tag).text
                assert response_value == request_value, f"{tag}不匹配: 响应={response_value}, 期望={request_value}"

            # 4. 检查RESPONSE_TIME是否不为空
            response_time = response_head.find('RESPONSE_TIME').text
            assert response_time is not None and response_time != '', "RESPONSE_TIME不应为空"

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_orderStatusQueryTO_otherServiceCode(self):

        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000006</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>请求服务与【服务编码】不匹配！</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1001</CUST_COMPANY>'
        #     '<SERVICE_CODE>T07_TO_002</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )

        try:
            request_xml = self.generate_request_xml(cust_company=self.CUST_COMPANY,
                                                    service_code='T07_TO_002',
                                                    access_token=TokenGenerator.generate_access_token(self.CUST_COMPANY,
                                                                                                      self.SERVICE_CODE),
                                                    request_time=GetCurrentTime.get_current_time()).strip()
            response = requests.post(url=self.BASE_URL, data=request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(request_xml)
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_head = response_root.find('HEAD')

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

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()