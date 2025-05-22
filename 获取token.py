import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置
import time

class TestGetSelects(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/electronize/getToken"
    # BASE_URL = "http://120.52.40.45:48080/electronize/getToken"   #接口地址
    getSysCode = "1002"
    getServiceCode = "T03_O_T_001"
    current_timestamp = time.time() #当前时间戳
    getTimestamp = current_timestamp - 600  #当前时间10分钟之前的时间戳
    def test_getToken(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getServiceCode": self.getServiceCode,
            "getTimestamp": self.getTimestamp
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功

            # token = "111111"
            # # 断言查询生成的token
            # self.assertEqual(response_data["data"]["data"][0]["value"],token,
            #     f"生成token不匹配。预期: {token}，实际: {response_data['data']['data'][0]['value']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_noGetSysCode(self):
        # 准备请求数据
        request_data = {
            "getServiceCode": self.getServiceCode,
            "getTimestamp": self.getTimestamp
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入应用标识！",
                             f'提示信息不是"请传入应用标识！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_noGetServiceCode(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getTimestamp": self.getTimestamp
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入服务编码！",
                             f'提示信息不是"请传入服务编码！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_noGetTimestamp(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getServiceCode": self.getServiceCode
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入当前时间戳！",
                             f'提示信息不是"请传入当前时间戳！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_errorGetSysCode(self):
        # 准备请求数据
        request_data = {
            "getSysCode": 1001,
            "getServiceCode": self.getServiceCode,
            "getTimestamp": self.getTimestamp
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入正确的应用标识！",
                             f'提示信息不是"请传入正确的应用标识！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_errorGetServiceCode(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getServiceCode": "T03_O_T_003",
            "getTimestamp": self.getTimestamp
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入正确的服务编码！",
                             f'提示信息不是"请传入正确的服务编码！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_errorGetTimestamp(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getServiceCode": self.getServiceCode,
            "getTimestamp": 1
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入正确的时间戳！",
                             f'提示信息不是"请传入正确的时间戳！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getToken_greatCurrentTiem(self):
        # 准备请求数据
        request_data = {
            "getSysCode": self.getSysCode,
            "getServiceCode": self.getServiceCode,
            "getTimestamp": self.current_timestamp + 600
        }

        # 准备请求头，指定内容类型为JSON
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        try:
            # 发送POST请求
            # 使用json参数自动序列化数据并设置Content-Type头
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "请传入正确的时间戳！",
                             f'提示信息不是"请传入正确的时间戳！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()