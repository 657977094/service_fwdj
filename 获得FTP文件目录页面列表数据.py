import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置
import time

class TestGetFtpDirGrid(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/qryFtpLogController/getFtpDirGrid"
    # BASE_URL = "http://120.52.40.45:48080/qryFtpLogController/getFtpDirGrid"   #接口地址
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    def test_getFtpDirGrid(self):
        """
        老代码为post表单格式上传，新代码为postjson格式上传
        老代码参数为provinceId和cityId，新代码变更为provinceCode和cityCode
        :return:
        """
        # 准备请求数据
        request_data = {
            # "provinceId": 520000,   #老代码字段
            "provinceCode": 520000,   #新开发后的字段
            # "cityId" : 520100,   #老代码字段
            "cityCode" : 520100,   #新开发后的字段
            # "start": 0,   #老代码字段
            # "limit": 10,   #老代码字段
            "page" : 0,   #新开发后的字段
            "size" : 10,   #新开发后的字段
            "custCompany" : 1003,
            "serviceCode": "T05_TO_008",
            "fileSource" : 1,
            "accountPeriod": 202503,
            "status": 1
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
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            id = "2127661"
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # 断言查询结果ID
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpDirGrid_noPage(self):
        # 准备请求数据
        request_data = {
            # "provinceId": 520000,  # 老代码字段
            "provinceCode": 340000,   #新开发后的字段
            # "cityId": 520100,  # 老代码字段
            "cityCode" : "",   #新开发后的字段
            # "limit": 10,   #老代码字段
            "size" : 10,   #新开发后的字段
            "custCompany" : 1003,
            "serviceCode": "T05_TO_008",
            "fileSource" : 1,
            "accountPeriod": 202503,
            "status": 1
        }

        try:
            # # 发送POST请求
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

            id = "2127661"
            # start = 1   #老代码为start，新代码为page
            page = 1   #老代码默认为0，新代码默认为1
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # assert response_data['rows'][0]['start'] == start, \
            #     f"预期为 id={start}, 实际为 {response_data['rows'][0]['start']}"  # 断言查询结果ID

            # 断言查询结果id和page，page不传默认按1生效
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["page"],page,
                f"page与预期不匹配。预期: {page}，实际: {response_data['data']['data']['rows'][0]['page']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpDirGrid_noSize(self):
        # 准备请求数据
        request_data = {
            "provinceId": 520000,  # 老代码字段
            # "provinceCode": 340000,   #新开发后的字段
            "cityId": 520100,  # 老代码字段
            # "cityCode" : "",   #新开发后的字段
            "start": 0,  # 老代码字段
            # "page" : 0,   #新开发后的字段
            "custCompany" : 1003,
            "serviceCode": "T05_TO_008",
            "fileSource" : 1,
            "accountPeriod": 202503,
            "status": 1
        }

        try:
            # # 发送POST请求
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

            id = "2127661"
            # limit = 2099999999   #老代码为limit，新代码为size
            size = 2099999999   #默认为2099999999
            # assert response_data['rows'][0]['id'] == id, \
            #     f"预期为 id={id}, 实际为 {response_data['rows'][0]['id']}"      #断言查询结果ID
            # assert response_data['rows'][0]['limit'] == limit, \
            #     f"预期为 id={limit}, 实际为 {response_data['rows'][0]['limit']}"  # 断言查询结果limit

            # 断言查询结果id和size，size不传默认按2099999999生效
            self.assertEqual(response_data["data"]["data"]['rows'][0]["id"],id,
                f"id与预期不匹配。预期: {id}，实际: {response_data['data']['data']['rows'][0]['id']}")
            self.assertEqual(response_data["data"]["data"]['rows'][0]["size"],size,
                f"page与预期不匹配。预期: {size}，实际: {response_data['data']['data']['rows'][0]['size']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpDirGrid_errorPage(self):
        # 准备请求数据
        request_data = {
            "provinceId": 520000,   #老代码字段
            # "provinceCode": 520000,   #新开发后的字段
            "cityId" : 520100,   #老代码字段
            # "cityCode" : 520100,   #新开发后的字段
            # "start": "-1",   #老代码字段
            # "limit": 10,   #老代码字段
            "page" : "-1",   #新开发后的字段
            "size" : 10,   #新开发后的字段
            "custCompany" : 1003,
            "serviceCode": "T05_TO_008",
            "fileSource" : 1,
            "accountPeriod": 202503,
            "status": 1
        }

        try:
            # # 发送POST请求
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

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "page必须为正整数！",
                             f'提示信息不是"page必须为正整数！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getFtpDirGrid_errorSize(self):
        # 准备请求数据
        request_data = {
            "provinceId": 520000,   #老代码字段
            # "provinceCode": 520000,   #新开发后的字段
            "cityId" : 520100,   #老代码字段
            # "cityCode" : 520100,   #新开发后的字段
            # "start": 1,   #老代码字段
            # "limit": "-10",   #老代码字段
            "page" : 1,   #新开发后的字段
            "size" : "-10",   #新开发后的字段
            "custCompany" : 1003,
            "serviceCode": "T05_TO_008",
            "fileSource" : 1,
            "accountPeriod": 202503,
            "status": 1
        }

        try:
            # # 发送POST请求
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

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "size必须为正整数！",
                             f'提示信息不是"size必须为正整数！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()