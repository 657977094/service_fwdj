import requests
import base64
from xml.etree import ElementTree as ET
import unittest
import json
from env_config import EnvConfig  # 导入环境配置


class TestGetStatisticsResult(unittest.TestCase):
    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/report/getStatisticsResult"
    # BASE_URL = "http://120.52.40.45:48080/report/getStatisticsResult"   #接口地址
    def test_getStatisticsResult(self):
        """
        老代码为post表单格式上传，新代码为GET请求
        老代码参数为province和city，新代码变更为provinceCode和cityCode
        :return:
        """
        # request_data = {
        #     "province": 110000,  # 省份(直辖市)的编码,老代码为province
        #     # "provinceCode": 110000,    #省份(直辖市)的编码，,新代码为provinceCode
        #     "city": 110100,  # 地市编码,老代码为city
        #     # "cityCode": 110100,  #地市编码,新代码为cityCode
        #     "startTime": "2025-04-02",  # 开始时间
        #     "endTime": "2025-04-27"  # 结束时间
        # }
        params = {
            "province": 110000,  # 省份(直辖市)的编码,老代码为province
            # "provinceCode": 110000,    #省份(直辖市)的编码，,新代码为provinceCode
            "city": 110100,  # 地市编码,老代码为city
            # "cityCode": 110100,  #地市编码,新代码为cityCode
            "startTime": "2025-04-02",  # 开始时间
            "endTime": "2025-04-27"  # 结束时间
        }

        try:
            # response = requests.post(
            #     url=self.BASE_URL,
            #     data=request_data
            # )
            response = requests.get(self.BASE_URL, params=params)  # 发起请求
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")  # 响应码校验
            response_data = response.json()  # 响应结果转换为json格式
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))  # 调试查看
            # 新代码返回JSON格式
            sucNumCm = "12"
            self.assertEqual(response_data["data"]["data"]["demandImport"]["sucNumCm"], sucNumCm,
                             f"预期 sucNumCm={sucNumCm}, 实际为 {response_data['data']['data']['demandImport']['sucNumCm']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getStatisticsResult_noProviceCode(self):
        # request_data = {
        #     "startTime": "2025-04-02",  #开始时间
        #     "endTime": "2025-04-27"   #结束时间
        # }
        params = {
            "startTime": "2025-04-02",  # 开始时间
            "endTime": "2025-04-27"  # 结束时间
        }
        try:
            # response = requests.post(
            #     url=self.BASE_URL,
            #     json=request_data
            # )
            response = requests.get(self.BASE_URL, params=params)  # 发起请求
            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            # 断言业务状态码（code="FAILURE" 表示报错失败）
            self.assertEqual(response_data["data"]["code"], "FAILURE",
                             f'业务状态码不是"FAILURE"，实际是{response_data["data"]["code"]}')

            # 断言提示信息
            self.assertEqual(response_data["data"]["msg"], "ProviceCode不能为空！",
                             f'提示信息不是"ProviceCode不能为空！"，实际是{response_data["data"]["msg"]}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()