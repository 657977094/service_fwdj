import requests
import base64
from xml.etree import ElementTree as ET
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestQryPacket(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/qry/qryPacket"
    # BASE_URL = "http://120.52.40.45:48080/qry/qryPacket"   #接口地址
    def test_QryPacket(self):
        params = {
            # "province": 110000,    #省份(直辖市)的编码,老代码为province
            "provinceCode": 110000,    #省份(直辖市)的编码，,新代码为provinceCode
            "flowId": 2456221,  #调用记录ID
            "qryFlg": 1   #0-请求报文，1-响应报文
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 第一步：提取嵌套的XML字符串
            xml_string = response_data['data']['data']

            # 第二步：解析XML
            root = ET.fromstring(xml_string)

            # 第三步：查找FLOW_ID节点
            requests_id = root.find(".//REQUEST_ID").text

            expected_requests_id = "1225032814470706"
            assert requests_id == expected_requests_id, (
                f"FLOW_ID 验证失败！\n"
                f"期望: {requests_id}\n"
                f"实际: {expected_requests_id}\n"
            )

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_QryPacket_noProvinceCode(self):
        params = {
            "flowId": 2456221,  # 调用记录ID
            "qryFlg": 1  # 0-请求报文，1-响应报文
        }

        try:
            response = requests.get(self.BASE_URL, params=params)  # 发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            response_data = response.json()  # 响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "provinceCode不能为空！",
                             f'提示信息不是"provinceCode不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_QryPacket_noFlowId(self):
        params = {
            # "province": 110000,    #省份(直辖市)的编码,老代码为province
            "provinceCode": 110000,  # 省份(直辖市)的编码，,新代码为provinceCode
            "qryFlg": 1  # 0-请求报文，1-响应报文
        }

        try:
            response = requests.get(self.BASE_URL, params=params)  # 发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            response_data = response.json()  # 响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "flowId不能为空！",
                             f'提示信息不是"flowId不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_QryPacket_noQryFlg(self):
        params = {
            # "province": 110000,    #省份(直辖市)的编码,老代码为province
            "provinceCode": 110000,  # 省份(直辖市)的编码，,新代码为provinceCode
            "flowId": 2456221  # 调用记录ID
        }

        try:
            response = requests.get(self.BASE_URL, params=params)  # 发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            response_data = response.json()  # 响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "qryFlg不能为空！",
                             f'提示信息不是"qryFlg不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()