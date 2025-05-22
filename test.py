import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置
import time

class TestGetFtpLogGrid(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/qryFtpLogController/getFtpLogGrid"
    # BASE_URL = "http://120.52.40.45:48080/qryFtpLogController/getFtpLogGrid"   #接口地址
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
                data=request_data
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