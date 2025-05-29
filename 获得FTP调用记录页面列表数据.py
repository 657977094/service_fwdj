import requests
import unittest
import json
from env_config import EnvConfig  # 导入环境配置
import time

class TestGetFtpLogGrid(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/qryFtpLogController/getFtpLogGrid"
    # BASE_URL = "http://120.52.40.45:48080/qryFtpLogController/getFtpLogGrid"   #接口地址
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    def test_getFtpLogGrid(self):
        # 准备请求数据
        request_data = {
            "provinceId": 340000,   #老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            "start": 0,    #老代码字段
            "limit": 10,    #老代码字段
            # "page" : 0,   #新开发后的字段
            # "size" : 10,   #新开发后的字段
            "sysCode": 1004,
            "handleType": 1,
            "serviceCode": "T09_OT_002",
            "accountPeriod": 20250521,
            "status": 1,
            "flowId": 75405637,
            "startTime": "2025-05-01",
            "endTime": "2025-05-21"
        }

        try:
            # # 发送POST请求,老代码为表单
            # response = requests.post(
            #     url=self.BASE_URL,
            #     data=request_data
            # )
            #新代码为json
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            id = "3265133"
            flowId = str(request_data["flowId"])
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # assert response_data['rows'][0]['flowId'] == flowId, \
            #     f"预期为 flowId={flowId}, 实际为 {response_data['rows'][0]['flowId']}"      #断言查询结果flowId
            # 断言查询结果ID和flowId
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["flowId"],flowId,
                f"flowId与预期不匹配。预期: {flowId}，实际: {response_data['data']['data']['rows'][0]['flowId']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogGrid_noPage(self):
        # 准备请求数据
        request_data = {
            "provinceId": 340000,   #老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            "limit": 10,    #老代码字段
            # "size" : 10,   #新开发后的字段
            "sysCode": 1004,
            "handleType": 1,
            "serviceCode": "T09_OT_002",
            "accountPeriod": 20250521,
            "status": 1,
            "flowId": 75405637,
            "startTime": "2025-05-01",
            "endTime": "2025-05-21"
        }

        try:
            # 发送POST请求
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            id = "3265133"
            flowId = str(request_data["flowId"])
            # start = 0   #老代码为start，新代码为page
            page = 1   #老代码默认为0，新代码默认为1
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # assert response_data['rows'][0]['start'] == start, \
            #     f"预期为 id={start}, 实际为 {response_data['rows'][0]['start']}"  # 断言查询结果ID
            # assert response_data['rows'][0]['flowId'] == flowId, \
            #     f"预期为 flowId={flowId}, 实际为 {response_data['rows'][0]['flowId']}"      #断言查询结果flowId

            # 断言查询结果id、flowId和page，page不传默认按1生效
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["page"],page,
                f"page与预期不匹配。预期: {page}，实际: {response_data['data']['data']['rows'][0]['page']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["flowId"],flowId,
                f"flowId与预期不匹配。预期: {flowId}，实际: {response_data['data']['data']['rows'][0]['flowId']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogGrid_noSize(self):
        # 准备请求数据
        request_data = {
            "provinceId": 340000,   #老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            "start": 0,  # 老代码字段
            # "page" : 0,   #新开发后的字段
            "sysCode": 1004,
            "handleType": 1,
            "serviceCode": "T09_OT_002",
            "accountPeriod": 20250521,
            "status": 1,
            "flowId": 75405637,
            "startTime": "2025-05-01",
            "endTime": "2025-05-21"
        }

        try:
            # 发送POST请求
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
            )

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            id = "3265133"
            flowId = str(request_data["flowId"])
            # limit = 2099999999   #老代码为limit，新代码为size
            size = 2099999999   #默认为2099999999
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # assert response_data['rows'][0]['limit'] == limit, \
            #     f"预期为 id={limit}, 实际为 {response_data['rows'][0]['limit']}"  # 断言查询结果limit
            # assert response_data['rows'][0]['flowId'] == flowId, \
            #     f"预期为 flowId={flowId}, 实际为 {response_data['rows'][0]['flowId']}"      #断言查询结果flowId

            # 断言查询结果id、flowId和page，page不传默认按1生效
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["size"],size,
                f"page与预期不匹配。预期: {size}，实际: {response_data['data']['data']['rows'][0]['size']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["flowId"],flowId,
                f"flowId与预期不匹配。预期: {flowId}，实际: {response_data['data']['data']['rows'][0]['flowId']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogGrid_errorSize(self):
        # 准备请求数据
        request_data = {
            "provinceId": 340000,   #老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            # "start": 1,   #老代码字段
            # "limit": "-10",   #老代码字段
            "page" : 1,   #新开发后的字段
            "size" : "-10",   #新开发后的字段
            "sysCode": 1004,
            "handleType": 1,
            "serviceCode": "T09_OT_002",
            "accountPeriod": 20250521,
            "status": 1,
            "flowId": 75405637,
            "startTime": "2025-05-01",
            "endTime": "2025-05-21"
        }

        try:
            # 发送POST请求
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
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
            self.assertEqual(response_data["data"]["msg"], "size必须为正整数！",
                             f'提示信息不是"size必须为正整数！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpLogGrid_errorPage(self):
        # 准备请求数据
        request_data = {
            "provinceId": 340000,   #老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            # "start": "-1",   #老代码字段
            # "limit": 10,   #老代码字段
            "page" : "-1",   #新开发后的字段
            "size" : 10,   #新开发后的字段
            "sysCode": 1004,
            "handleType": 1,
            "serviceCode": "T09_OT_002",
            "accountPeriod": 20250521,
            "status": 1,
            "flowId": 75405637,
            "startTime": "2025-05-01",
            "endTime": "2025-05-21"
        }

        try:
            # 发送POST请求
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
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
            self.assertEqual(response_data["data"]["msg"], "page必须为正整数！",
                             f'提示信息不是"page必须为正整数！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()