import json
import unittest
import requests
from parameterized import parameterized
from service_fwdj.env_config import EnvConfig


class TestQryFlowLog(unittest.TestCase):

    def public_request(self,data):
        try:
            response = requests.post(
                url=f'{EnvConfig.get_base_url()}/qry/qryFlowLog',
                data=data,
                timeout=5
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.fail(f"请求失败，错误信息: {e}")


        return response

    '''
    查询服务管理日志
    '''
    def test_postQryFlowLog_all_param(self):
        """
        全部参数查询
        :return:
        """
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': 0,
            'limit': 100
        }
        expected_status_code = 200

        response = self.public_request(data)

        # 断言状态码
        self.assertEqual(response.status_code, expected_status_code,
                         f"预期状态码为： {expected_status_code}, 实际为： {response.status_code}")
        # 断言错误信息
        # self.assertEqual(response.status_code, expected_status_code,
        #                  f"预期返回信息为： {expected_status_code}, 实际为： {response.status_code}")
        # 断言响应体
        try:
            response_data = json.loads(response.text)
        except json.JSONDecodeError:
            self.fail("Response 格式不是json")

        self.assertIn('total', response_data, "Response 中没有 'total' 字段")
        # 需求单号为唯一时，可以精确断言返回内容


    def postQryFlowLog_empty_pram(self,data,pramname,param_type):
        """
        必填参数为空通用查询
        :return:
        """

        expected_status_code = 200

        response = self.public_request(data)

        # 断言状态码
        self.assertEqual(response.status_code, expected_status_code,
                         f"预期状态码为： {expected_status_code}, 实际为： {response.status_code}")


        # 断言响应体
        try:
            response_data = json.loads(response.text)
        except json.JSONDecodeError:
            self.fail("Response 格式不是json")


        if param_type == 'empty':
            # 断言错误信息
            self.assertEqual(response_data['msg'], f'{pramname}不能为空',
                                 f"预期返回信息为： {pramname}不能为空, 实际为： {response_data['msg']}")


        elif param_type == 'error':
            # 断言错误信息
            self.assertEqual(response_data['msg'], f'{pramname}格式不正确',
                             f"预期返回信息为： {pramname}格式不正确, 实际为： {response_data['msg']}")
        else:
            self.fail(f"未定义的传入参数{param_type}")



        self.assertEqual(response_data['code'], 'FAILURE',
                         f"预期返回状态为： FAILURE, 实际为： {response_data['code']}")


    def test_postQryFlowLog_empty_province(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': 0,
            'limit': 100
        }
        self.postQryFlowLog_empty_pram(data,'province','empty')


    def test_postQryFlowLog_empty_requestId(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': 0,
            'limit': 100
        }
        self.postQryFlowLog_empty_pram(data,'requestId','empty')

    def test_postQryFlowLog_empty_start(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': '',
            'limit': 100
        }
        self.postQryFlowLog_empty_pram(data,'start','empty')

    def test_postQryFlowLog_empty_limit(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': 0,
            'limit': ''
        }
        self.postQryFlowLog_empty_pram(data,'limit','empty')


    def test_postQryFlowLog_error_type_limit(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': 0,
            'limit': -1
        }
        self.postQryFlowLog_empty_pram(data,'limit','error')

    def test_postQryFlowLog_error_type_start(self):
        data = {
            'province': 110000,
            # 'city': '',
            'requestId': '',
            'start': -1,
            'limit': 100
        }
        self.postQryFlowLog_empty_pram(data,'start','error')



if __name__ == '__main__':
    unittest.main()