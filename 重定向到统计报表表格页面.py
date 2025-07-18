import json
import unittest
import requests
from Tools.scripts.generate_opcode_h import header

from service_fwdj.env_config import EnvConfig


class TestGetFlowReportCell(unittest.TestCase):

    def public_request(self,param):


        try:
            response = requests.get(
                url=f'{EnvConfig.get_base_url()}/report/getFlowReportCell',
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
    def test_getFlowReportCell_all_param(self):
        """
        全部参数查询
        :return:
        """
        params = {
            'reportType': '',
            'prov': '',
            'city': '',
            'startTime': '',
            'endTime': '',
            'excelName': '',
            'custAndStatus': ''
        }


        expected_status_code = 200

        response = self.public_request(params)

        # 断言状态码
        self.assertEqual(response.status_code, expected_status_code,
                         f"预期状态码为： {expected_status_code}, 实际为： {response.status_code}")

        # 断言响应体,返回的拼接url是确定的，可以根据参数拼接断言
        # self.assertEqual(response.content)
        # try:
        #     response_data = json.loads(response.text)
        # except json.JSONDecodeError:
        #     self.fail("Response 格式不是json")
        #
        # self.assertIn('total', response_data, "Response 中没有 'total' 字段")
        # 需求单号为唯一时，可以精确断言返回内容


    def getFlowReportCell_empty_pram(self,data,pramname,param_type):
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


    def test_getFlowReportCell_empty_reportType(self):
        params = {
            'reportType': '',
            'prov': '',
            'city': '',
            'startTime': '',
            'endTime': '',
            'excelName': '',
            'custAndStatus': ''
        }

        self.getFlowReportCell_empty_pram(params,'reportType','empty')




if __name__ == '__main__':
    unittest.main()