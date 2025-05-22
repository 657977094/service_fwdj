import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestGetAPI(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/webservice/orderTrajectoryQuery"
    # BASE_URL = "http://120.52.40.45:48080/webservice/orderTrajectoryQuery"   #接口地址
    def test_orderTrajectoryQuery(self):

        # 准备请求数据
        request_data = {
            "province": 110000,  # 省份编码
            "city": 110100,  # 地市编码
            "customer": 1003,  # 运营商，固定只能传1003
            "requestId": "1225032814470706",  # 需求单号
            "requestType": 1,  # 订单类型
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            request_id = request_data["requestId"]    #提取请求参数中的requestId

            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))    #调试查看

            # 断言测试
            # 断言查询结果的需求单号与请求中的需求单号一致，注释方法为老代码响应格式，下方为新代码预期格式，实际响应结果待环境部署后调试确认
            # assert response_data["data"][0]["requestId"] == request_id, \
            #     f"预期为 requestId={request_id}, 实际为 {response_data['data'][0]['requestId']}"
            self.assertEqual(response_data["data"]["data"]["data"][0]["requestId"],request_id,
                f"预期 requestId={request_id}, 实际为 {response_data['data']['data']['data'][0]['requestId']}" )
            print("测试通过！")

        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")

    def test_orderTrajectoryQuery_lackProvince(self):

        # 准备请求数据
        request_data = {
            "city": 110100,  # 地市编码
            "customer": 1003,  # 运营商，固定只能传1003
            "requestId": "1225032814470706",  # 需求单号
            "requestType": 1,  # 订单类型
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "province不能为空！",
                             f'提示信息不是"province不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")

    def test_orderTrajectoryQuery_lackCustomer(self):

        # 准备请求数据
        request_data = {
            "province": 110000,  # 省份编码
            "city": 110100,  # 地市编码
            "requestId": "1225032814470706",  # 需求单号
            "requestType": 1,  # 订单类型
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "customer不能为空！",
                             f'提示信息不是"customer不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")

    def test_orderTrajectoryQuery_lackRequestId(self):

        # 准备请求数据
        request_data = {
            "province": 110000,  # 省份编码
            "city": 110100,  # 地市编码
            "customer": 1003,  # 运营商，固定只能传1003
            "requestType": 1,  # 订单类型
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "requestId不能为空！",
                             f'提示信息不是"requestId不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")

    def test_orderTrajectoryQuery_lackRequestType(self):

        # 准备请求数据
        request_data = {
            "province": 110000,  # 省份编码
            "city": 110100,  # 地市编码
            "customer": 1003,  # 运营商，固定只能传1003
            "requestId": "1225032814470706",  # 需求单号
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "requestType不能为空！",
                             f'提示信息不是"requestType不能为空！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")

    def test_orderTrajectoryQuery_LT(self):

        # 准备请求数据
        request_data = {
            "province": 110000,  # 省份编码
            "city": 110100,  # 地市编码
            "customer": 1002,  # 运营商，固定只能传1003
            "requestId": "1225032814470706",  # 需求单号
            "requestType": 1,  # 订单类型
            "processType": "ORDER_ACT_TYPE_2",  # 流程类型，为空代表全部
            "requestTime": "2025-03-31"  # 请求时间，格式2025-05-15
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

            # 断言响应状态码是200(Created)
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")

            # 将响应内容解析为JSON格式
            response_data = response.json()

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "customer只能为1003！",
                             f'提示信息不是"customer只能为1003！"，实际是{response_data["data"]["msg"]}')
            print("测试通过！")
        except requests.exceptions.RequestException as e:
            # 捕获并处理请求异常
            self.fail(f"请求发送失败: {str(e)}")
if __name__ == '__main__':
    # 运行所有测试用例
    unittest.main()