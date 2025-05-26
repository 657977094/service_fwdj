import json
import unittest
import requests
from Tools.scripts.generate_opcode_h import header

from service_fwdj.env_config import EnvConfig


class TestGetStatisticsDtl(unittest.TestCase):

    def public_request(self,param):


        try:
            response = requests.get(
                url=f'{EnvConfig.get_base_url()}/report/getStatisticsDtl',
                params=param,
                timeout=5
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.fail(f"请求失败，错误信息: {e}")


        return response

    '''
    获取统计明细
    '''
    def test_getStatisticsDtl_all_param(self):
        """
        全部参数查询
        :return:
        """
        params = {
            'province': '110000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '',
            'limit': ''
        }


        expected_status_code = 200

        response = self.public_request(params)

        # 断言状态码
        self.assertEqual(response.status_code, expected_status_code,
                         f"预期状态码为： {expected_status_code}, 实际为： {response.status_code}")

        # 断言响应体
        try:
            response_data = json.loads(response.text)
        except json.JSONDecodeError:
            self.fail("Response 格式不是json")
        #
        # self.assertIn('total', response_data, "Response 中没有 'total' 字段")
        # 需求单号为唯一时，可以精确断言返回内容


    def getStatisticsDtl_empty_pram(self,data,pramname,param_type):
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


    def test_getStatisticsDtl_empty_province(self):
        params = {
            'province': '340000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '',
            'limit': ''
        }

        self.getStatisticsDtl_empty_pram(params,'province','empty')

    def test_getStatisticsDtl_empty_start(self):
        params = {
            'province': '340000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '',
            'limit': ''
        }

        self.getStatisticsDtl_empty_pram(params,'start','empty')
        assert False, '当前环境没有测试数据，不知道返回结构，断言待补充'

    def test_getStatisticsDtl_empty_limit(self):
        params = {
            'province': '340000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '',
            'limit': ''
        }

        self.getStatisticsDtl_empty_pram(params,'limit','empty')
        assert False, '当前环境没有测试数据，不知道返回结构，断言待补充'


    def test_getStatisticsDtl_error_start(self):
        params = {
            'province': '340000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '-1',
            'limit': ''
        }

        self.getStatisticsDtl_empty_pram(params,'start','error')

    def test_getStatisticsDtl_error_limit(self):
        params = {
            'province': '340000',
            'city': '',
            'company': '',
            'serverCode': '',
            'isSuccess': '',
            'startTime': '',
            'endTime': '',
            'start': '',
            'limit': '-1'
        }

        self.getStatisticsDtl_empty_pram(params,'limit','error')


if __name__ == '__main__':
    # unittest.main()
    TestGetStatisticsDtl().test_getStatisticsDtl_all_param()