import requests
import unittest
import json
from env_config import EnvConfig  # 导入环境配置

class TestGetDemandStatus(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/webservice/getDemandStatus"
    # BASE_URL = "http://120.52.40.45:48080/webservice/getDemandStatus"   #接口地址
    def test_getDemandStatus(self):
        params = {
            # "provinceCode": 110000,     #省份编码，新代码为provinceCode
            "province": 110000,     #省份编码，老代码为province
            # "cityCode": 110100,     #地市编码，新代码为cityCode
            "city": 110100,     #地市编码，老代码为city
            "customer":1003,    #运营商，前端页面限制只能传1003，但是后端代码未做任何限制
            "requestId":"1225032814470706",   #需求单号
            "requestType":1,    #订单类型
            "processType":"ORDER_ACT_TYPE_2",       #流程类型，为空代表全部
            "requestTime":"2025-03-31"      #请求时间，格式2025-05-15
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            request_id = params["requestId"]    #提取请求参数中的requestId
            # 断言查询结果的需求单号与请求中的需求单号一致，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # assert response_data["rows"][0]["requestId"] == request_id, \
            #     f"预期为 requestId={request_id}, 实际为 {response_data['rows'][0]['requestId']}"
            #
            self.assertEqual(response_data["data"]["data"]["rows"][0]["requestId"], request_id,
                f"预期 requestId={request_id}, 实际为 {response_data['data']['data']['rows'][0]['requestId']}")

            print("测试通过！")
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getDemandStatus_lackProvinceCode(self):
        params = {
            "cityCode": 110100,     #地市编码，老代码为city
            "customer":1003,    #运营商，前端页面限制只能传1003，但是后端代码未做任何限制
            "requestId":"1225032814470706",   #需求单号
            "requestType":1,    #订单类型
            "processType":"ORDER_ACT_TYPE_2",       #流程类型，为空代表全部
            "requestTime":"2025-03-31"      #请求时间，格式2025-05-15
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "provinceCode不能为空！",
                             f'提示信息不是"provinceCode不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getDemandStatus_lackCustomer(self):
        params = {
            "provinceCode": 110000,  # 省份编码，老代码为province
            "cityCode": 110100,     #地市编码，老代码为city
            "requestId":"1225032814470706",   #需求单号
            "requestType":1,    #订单类型
            "processType":"ORDER_ACT_TYPE_2",       #流程类型，为空代表全部
            "requestTime":"2025-03-31"      #请求时间，格式2025-05-15
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "customer不能为空！",
                             f'提示信息不是"customer不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getDemandStatus_lackRequestId(self):
        params = {
            "provinceCode": 110000,  # 省份编码，老代码为province
            "cityCode": 110100,     #地市编码，老代码为city
            "customer": 1003,  # 运营商，前端页面限制只能传1003，但是后端代码未做任何限制
            "requestType":1,    #订单类型
            "processType":"ORDER_ACT_TYPE_2",       #流程类型，为空代表全部
            "requestTime":"2025-03-31"      #请求时间，格式2025-05-15
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "requestId不能为空！",
                             f'提示信息不是"requestId不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getDemandStatus_lackRequestType(self):
        params = {
            "provinceCode": 110000,  # 省份编码，老代码为province
            "cityCode": 110100,     #地市编码，老代码为city
            "customer": 1003,  # 运营商，前端页面限制只能传1003，但是后端代码未做任何限制
            "requestId": "1225032814470706",  # 需求单号
            "processType":"ORDER_ACT_TYPE_2",       #流程类型，为空代表全部
            "requestTime":"2025-03-31"      #请求时间，格式2025-05-15
        }

        try:
            response = requests.get(self.BASE_URL, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "requestType不能为空！",
                             f'提示信息不是"requestType不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()
