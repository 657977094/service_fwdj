import requests
import unittest
import json
from env_config import Base64Util  # 导入环境配置
from env_config import TokenGenerator
from env_config import GetCurrentTime
from env_config import EnvConfig  # 导入环境配置
from env_config import SoapResponseHandle  # 导入环境配置
from xml.etree import ElementTree as ET


class TestOperatorConfirmLeaseAfter(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/kafkaserver/crm/operatorConfirmLeaseAfter"
    # 准备请求头，指定内容类型为JSON
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    def test_operatorConfirmLeaseAfter(self):
        # 准备请求数据(无参数校验，参数值任意)
        request_data = {
            'tradeId' : '123123',
            'requestId' : '123123',
            'confirmResult' : '123123',
            'confirmOpinion' : '123123',
            'confirmDate' : '123123',
            'confirmor' : '123123',
            'shareBatch' : '123123',
            'shareResult' : '123123'
        }

        try:
            response = requests.post(
                url=self.BASE_URL,
                json=request_data,
                headers=self.headers
            )

            # 断言测试
            # self.assertEqual(response.status_code, 200,
            #                  f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式,成功后无任何返回值
            self.assertIsNone(response, "响应应该是 None")
            print(f'响应：{response_data}')

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == '__main__':
    unittest.main()