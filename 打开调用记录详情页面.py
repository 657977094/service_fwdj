import requests
import base64
from xml.etree import ElementTree as ET
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestGetFtpLogDetailPage(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/qryFtpLogController/getFtpLogDetailPage"
    # BASE_URL = "http://120.52.40.45:48080/qryFtpLogController/getFtpLogDetailPage"   #接口地址
    def test_getFtpLogDetailPage(self):
        params = {
            "id": 3260848
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            print(response.text)    #打印原始响应报文，原生产环境响应结果为HTML,新开发会重新开发实现返回JSON
            # response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
            # code = "0"
            # self.assertEqual(response_data["data"]["code"], code,
            #                  f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # request_id = params["requestId"]    #提取请求参数中的requestId
            # # 断言查询结果的需求单号与请求中的需求单号一致，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # # assert response_data["rows"][0]["requestId"] == request_id, \
            # #     f"预期为 requestId={request_id}, 实际为 {response_data['rows'][0]['requestId']}"
            # #
            # self.assertEqual(response_data["data"]["data"]["rows"][0]["requestId"], request_id,
            #     f"预期 requestId={request_id}, 实际为 {response_data['data']['data']['rows'][0]['requestId']}")

            print("测试通过！")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogDetailPage_noId(self):
        params = {}

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "id不能为空！",
                             f'提示信息不是"id不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogDetailPage_notExistId(self):
        params = {
            "id" : 11111111111111
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')
            #断言查询结果为空
            self.assertIsNone(response_data["data"]["data"],
                f"预期为 None，实际为 {response_data['data']['data']}")
            print("测试通过！")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()