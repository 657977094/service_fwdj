import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestGetAreas(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/commonController/getAreas"
    # BASE_URL = "http://120.52.40.45:48080/commonController/getAreas"   #接口地址
    def test_getAreas_type(self):
        params = {
            "type": 1,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
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
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            value_id = "110000"
            text = "北京市"
            # 断言查询结果省份编码和省份名称，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # assert response_data[0]["value"] == value_id, \
            #     f"预期为 requestId={value_id}, 实际为 {response_data[0]['value']}"      #断言查询结果省份编码
            # assert response_data[0]["text"] == text, \
            #     f"预期为 requestId={text}, 实际为 {response_data[0]['text']}"      #断言查询结果省份名称

            # 断言查询结果省份编码
            self.assertEqual(response_data["data"]["data"][0]["value"],value_id,
                f"省份编码不匹配。预期: {value_id}，实际: {response_data['data']['data'][0]['value']}")

            # 断言查询结果省份名称
            self.assertEqual(response_data["data"]["data"][0]["text"],text,
                f"省份名称不匹配。预期: {text}，实际: {response_data['data']['data'][0]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getAreas_Param(self):
        params = {
            "type": 2,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
            "param": 110000  #省份编码
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
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            value_id = "110100"    #提取请求参数中的requestId
            text = "北京市市辖区"    #提取请求参数中的requestId
            # 断言查询结果省份编码和省份名称，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # assert response_data[0]["value"] == value_id, \
            #     f"预期为 requestId={value_id}, 实际为 {response_data[0]['value']}"      #断言查询结果省份编码
            # assert response_data[0]["text"] == text, \
            #     f"预期为 requestId={text}, 实际为 {response_data[0]['text']}"      #断言查询结果省份名称

            # 断言查询结果地市编码
            self.assertEqual(response_data["data"]["data"][0]["value"],value_id,
                f"地市编码不匹配。预期: {value_id}，实际: {response_data['data']['data'][0]['value']}")

            # 断言查询结果地市名称
            self.assertEqual(response_data["data"]["data"][0]["text"],text,
                f"地市名称不匹配。预期: {text}，实际: {response_data['data']['data'][0]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getAreas_typeParam(self):
        params = {
            "type": 1,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
            "param": 110000     #type为1传param会自动过滤不生效
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
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            value_id = "110000"
            text = "北京市"
            # 断言查询结果省份编码和省份名称，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # assert response_data[0]["value"] == value_id, \
            #     f"预期为 requestId={value_id}, 实际为 {response_data[0]['value']}"      #断言查询结果省份编码
            # assert response_data[0]["text"] == text, \
            #     f"预期为 requestId={text}, 实际为 {response_data[0]['text']}"      #断言查询结果省份名称

            # 断言查询结果省份编码
            self.assertEqual(response_data["data"]["data"][0]["value"],value_id,
                f"省份编码不匹配。预期: {value_id}，实际: {response_data['data']['data'][0]['value']}")

            # 断言查询结果省份名称
            self.assertEqual(response_data["data"]["data"][0]["text"],text,
                f"省份名称不匹配。预期: {text}，实际: {response_data['data']['data'][0]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getAreas_noParam(self):
        params = {
            "type": 2,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
        }

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
            self.assertEqual(response_data["data"]["msg"], "param不能为空！",
                             f'提示信息不是"param不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getAreas_errorParam(self):
        params = {
            "type": 2,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
            "param": 110000000     #type为1传param会自动过滤不生效
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

    def test_getAreas_errorType(self):
        params = {
            "type": 3,  #1为查询所有省份编码，2为查询所有地市编码，此时param必传
        }

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
            self.assertEqual(response_data["data"]["msg"], "type错误！",
                             f'提示信息不是"type错误！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getAreas_noType(self):
        params = {} #type为空

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
            self.assertEqual(response_data["data"]["msg"], "type不能为空！",
                             f'提示信息不是"type不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()