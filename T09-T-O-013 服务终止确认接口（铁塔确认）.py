import requests
import unittest
import json
from env_config import EnvConfig  # 导入环境配置
from env_config import GetCurrentTime
from env_config import TokenGenerator
from xml.etree import ElementTree as ET


class TestCustomerTerminationConfirmTO(unittest.TestCase):
    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/crm/customerTerminationConfirmTO"
    # BASE_URL = "http://120.52.40.45:48080/crm/customerTerminationConfirmTO"   #接口地址
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/xml"
    }

    def test_customerTerminationConfirmTO_YD(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1001", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1001</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140300</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-04-24 14:56:30</CONFIRM_DATE>'
            '<COUNTY_CODE>140321</COUNTY_CODE>'
            '<OPINION_INFO>/n/t/s~！@#￥%……&*（）——+：“|？》《!@#$%^&*())_+:"|?><</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>02</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # 数据库响应日志
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000000</RESPONSE_CODE>'
        #     '<RESPONSE_MSG></RESPONSE_MSG>'
        #     '<CUST_COMPANY>1001</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-04-24 14:56:30</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY>'
        #     '<SYNC_RESULT>1</SYNC_RESULT>'
        #     '<REQUEST_ID>1219121808465545</REQUEST_ID>'
        #     '<FAIL_MESSAGE>T09_TO_013接口调用成功！</FAIL_MESSAGE>'
        #     '</BODY>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # # 解析请求XML
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

            # # 3. 检查FAIL_MESSAGE是否为空
            # fail_message = response_body.find('FAIL_MESSAGE').text
            # assert fail_message is None or fail_message == '', "FAIL_MESSAGE应为空"

            # # 3. 检查FAIL_MESSAGE是否为T09_TO_013接口调用成功！（移动特殊返回）
            # fail_message = response_body.find('FAIL_MESSAGE').text
            # assert fail_message == 'T09_TO_013接口调用成功！', f"FAIL_MESSAGE应为 T09_TO_013接口调用成功！, 实际为{fail_message}"

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

    def test_customerTerminationConfirmTO_DX(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1003", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1003</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>请推送相关负责人</OPINION_INFO>'
            '<CONFIRMOR>铁塔客户经理</CONFIRMOR>'
            '<RESULT>02</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        #数据库响应日志
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000000</RESPONSE_CODE>'
        #     '<RESPONSE_MSG></RESPONSE_MSG>'
        #     '<CUST_COMPANY>1003</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-26 16:43:57</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY>'
        #     '<SYNC_RESULT>1</SYNC_RESULT>'
        #     '<REQUEST_ID>1218010800906259</REQUEST_ID>'
        #     '<FAIL_MESSAGE></FAIL_MESSAGE>'
        #     '</BODY>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
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

    def test_customerTerminationConfirmTO_LT(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1002</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        #模拟其他运营商数据库日志的预期返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000000</RESPONSE_CODE>'
        #     '<RESPONSE_MSG></RESPONSE_MSG>'
        #     '<CUST_COMPANY>1002</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-26 16:43:57</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY>'
        #     '<SYNC_RESULT>1</SYNC_RESULT>'
        #     '<REQUEST_ID>1218010800906259</REQUEST_ID>'
        #     '<FAIL_MESSAGE></FAIL_MESSAGE>'
        #     '</BODY>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
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

            # 1. 检查REQUEST_ID是否一致
            # request_id_request = request_body.find('REQUEST_ID').text
            # request_id_response = response_body.find('REQUEST_ID').text
            # assert request_id_response == request_id_request, f"REQUEST_ID不匹配: 响应={request_id_response}, 期望={request_id_request}"
            #
            # # 2. 检查SYNC_RESULT是否为1
            # sync_result = response_body.find('SYNC_RESULT').text
            # assert sync_result == '1', f"SYNC_RESULT应为1, 实际为{sync_result}"

            # # 3. 检查FAIL_MESSAGE是否为空（待确认联通实际返回为空，还是有特殊值，还是无此字段）
            # fail_message = response_body.find('FAIL_MESSAGE').text
            # assert fail_message is None or fail_message == '', "FAIL_MESSAGE应为空"

            # 4. 检查RESPONSE_CODE是否为000000
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000000', f"RESPONSE_CODE应为000000, 实际为{response_code}"

            # # 5. 检查RESPONSE_MSG是否为空（待确认联通实际返回为空，还是有特殊值，还是无此字段）
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

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    # def test_customerTerminationConfirmTO_lackToken(self):
    #
    #     # 原始请求XML（保持原始格式）
    #     expected_request_xml = (
    #         '<?xml version="1.0" encoding="UTF-8"?>'
    #         '<PACKET>'
    #         '<HEAD>'
    #         '<ACCESS_TOKEN></ACCESS_TOKEN>'
    #         '<CUST_COMPANY>1002</CUST_COMPANY>'
    #         '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
    #         f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
    #         '</HEAD>'
    #         '<BODY>'
    #         '<REGION_CODE>140200</REGION_CODE>'
    #         '<REQUEST_ID>1234123123112113</REQUEST_ID>'
    #         '<PROVINCE_CODE>140000</PROVINCE_CODE>'
    #         '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
    #         '<COUNTY_CODE>140203</COUNTY_CODE>'
    #         '<OPINION_INFO>已处理</OPINION_INFO>'
    #         '<CONFIRMOR>运营商发起</CONFIRMOR>'
    #         '<RESULT>1</RESULT>'
    #         '</BODY>'
    #         '</PACKET>'
    #     )
    #     # # 预期实际报错返回结果
    #     # expected_response_xml = (
    #     #     '<?xml version="1.0" encoding="UTF-8"?>'
    #     #     '<PACKET>'
    #     #     '<HEAD>'
    #     #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
    #     #     '<RESPONSE_MSG>【访问令牌】不能为空</RESPONSE_MSG>'
    #     #     '<CUST_COMPANY>1002</CUST_COMPANY>'
    #     #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
    #     #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
    #     #     '</HEAD>'
    #     #     '<BODY/>'
    #     #     '</PACKET>'
    #     # )
    #     try:
    #         response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
    #         # 断言测试
    #         self.assertEqual(response.status_code, 200,
    #                          f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
    #         self.assertIn("application/xml", response.headers["Content-Type"])
    #
    #         # 解析请求XML
    #         request_root = ET.fromstring(expected_request_xml)
    #         request_body = request_root.find('BODY')
    #         request_head = request_root.find('HEAD')
    #
    #         # 解析响应XML
    #         response_root = ET.fromstring(response.text)
    #         response_body = response_root.find('BODY')
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

    def test_customerTerminationConfirmTO_lackCustCompany(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY></CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【运营商编码】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY></CUST_COMPANY>'   #可能为空也可能为Null
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(expected_request_xml)
            request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_body = response_root.find('BODY')
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

    def test_customerTerminationConfirmTO_lackServiceCode(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1002</CUST_COMPANY>'
            '<SERVICE_CODE></SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【服务代码】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1002</CUST_COMPANY>'
        #     '<SERVICE_CODE></SERVICE_CODE>'   #可能为空，也可能为Null
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(expected_request_xml)
            request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_body = response_root.find('BODY')
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

    def test_customerTerminationConfirmTO_lackRequestTime(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1002</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            '<REQUEST_TIME></REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000004</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>【请求时间】不能为空</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1002</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(expected_request_xml)
            request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_body = response_root.find('BODY')
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

    # def test_customerTerminationConfirmTO_errorToken(self):
    #
    #     # 原始请求XML（保持原始格式）
    #     expected_request_xml = (
    #         '<?xml version="1.0" encoding="UTF-8"?>'
    #         '<PACKET>'
    #         '<HEAD>'
    #         '<ACCESS_TOKEN>123123</ACCESS_TOKEN>'
    #         '<CUST_COMPANY>1002</CUST_COMPANY>'
    #         '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
    #         f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
    #         '</HEAD>'
    #         '<BODY>'
    #         '<REGION_CODE>140200</REGION_CODE>'
    #         '<REQUEST_ID>1234123123112113</REQUEST_ID>'
    #         '<PROVINCE_CODE>140000</PROVINCE_CODE>'
    #         '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
    #         '<COUNTY_CODE>140203</COUNTY_CODE>'
    #         '<OPINION_INFO>已处理</OPINION_INFO>'
    #         '<CONFIRMOR>运营商发起</CONFIRMOR>'
    #         '<RESULT>1</RESULT>'
    #         '</BODY>'
    #         '</PACKET>'
    #     )
    #     # # 预期实际报错返回结果
    #     # expected_response_xml = (
    #     #     '<?xml version="1.0" encoding="UTF-8"?>'
    #     #     '<PACKET>'
    #     #     '<HEAD>'
    #     #     '<RESPONSE_CODE>000001</RESPONSE_CODE>'
    #     #     '<RESPONSE_MSG>【访问令牌】不正确</RESPONSE_MSG>'
    #     #     '<CUST_COMPANY>1002</CUST_COMPANY>'
    #     #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
    #     #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
    #     #     '</HEAD>'
    #     #     '<BODY/>'
    #     #     '</PACKET>'
    #     # )
    #     try:
    #         response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
    #         # 断言测试
    #         self.assertEqual(response.status_code, 200,
    #                          f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
    #         self.assertIn("application/xml", response.headers["Content-Type"])
    #
    #         # 解析请求XML
    #         request_root = ET.fromstring(expected_request_xml)
    #         request_body = request_root.find('BODY')
    #         request_head = request_root.find('HEAD')
    #
    #         # 解析响应XML
    #         response_root = ET.fromstring(response.text)
    #         response_body = response_root.find('BODY')
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

    def test_customerTerminationConfirmTO_otherCustCompany(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1004</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>999999</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>该接口不支持运营商</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1002</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(expected_request_xml)
            request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_body = response_root.find('BODY')
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

    def test_customerTerminationConfirmTO_otherServiceCode(self):

        # 原始请求XML（保持原始格式）
        expected_request_xml = (
            '<?xml version="1.0" encoding="UTF-8"?>'
            '<PACKET>'
            '<HEAD>'
            f'<ACCESS_TOKEN>{TokenGenerator.generate_access_token("1002", "T09_TO_013")}</ACCESS_TOKEN>'
            '<CUST_COMPANY>1002</CUST_COMPANY>'
            '<SERVICE_CODE>T09_TO_014</SERVICE_CODE>'
            f'<REQUEST_TIME>{GetCurrentTime.get_current_time()}</REQUEST_TIME>'
            '</HEAD>'
            '<BODY>'
            '<REGION_CODE>140200</REGION_CODE>'
            '<REQUEST_ID>1234123123112113</REQUEST_ID>'
            '<PROVINCE_CODE>140000</PROVINCE_CODE>'
            '<CONFIRM_DATE>2025-05-26 16:43:57</CONFIRM_DATE>'
            '<COUNTY_CODE>140203</COUNTY_CODE>'
            '<OPINION_INFO>已处理</OPINION_INFO>'
            '<CONFIRMOR>运营商发起</CONFIRMOR>'
            '<RESULT>1</RESULT>'
            '</BODY>'
            '</PACKET>'
        )
        # # 预期实际报错返回结果
        # expected_response_xml = (
        #     '<?xml version="1.0" encoding="UTF-8"?>'
        #     '<PACKET>'
        #     '<HEAD>'
        #     '<RESPONSE_CODE>000006</RESPONSE_CODE>'
        #     '<RESPONSE_MSG>请求服务与【服务编码】不匹配！</RESPONSE_MSG>'
        #     '<CUST_COMPANY>1002</CUST_COMPANY>'
        #     '<SERVICE_CODE>T09_TO_013</SERVICE_CODE>'
        #     '<RESPONSE_TIME>2025-05-13 14:52:00</RESPONSE_TIME>'
        #     '</HEAD>'
        #     '<BODY/>'
        #     '</PACKET>'
        # )
        try:
            response = requests.post(url=self.BASE_URL, data=expected_request_xml.encode('utf-8'), headers=self.headers)
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            self.assertIn("application/xml", response.headers["Content-Type"])

            # 解析请求XML
            request_root = ET.fromstring(expected_request_xml)
            request_body = request_root.find('BODY')
            request_head = request_root.find('HEAD')

            # 解析响应XML
            response_root = ET.fromstring(response.text)
            response_body = response_root.find('BODY')
            response_head = response_root.find('HEAD')

            # 1. 检查RESPONSE_CODE是否为000006
            response_code = response_head.find('RESPONSE_CODE').text
            assert response_code == '000006', f"RESPONSE_CODE应为000006, 实际为{response_code}"

            # 2. 检查RESPONSE_MSG是否为请求服务与【服务编码】不匹配！
            response_msg = response_head.find('RESPONSE_MSG').text
            assert response_msg == '请求服务与【服务编码】不匹配！', \
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