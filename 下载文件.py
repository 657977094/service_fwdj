import json
import unittest
import requests

from service_fwdj.env_config import EnvConfig


class TestDownLoadFile(unittest.TestCase):

    def public_request(self,param, headers):


        try:
            response = requests.get(
                url=f'{EnvConfig.get_base_url()}/qryFtpLogController/downLoadFile',
                params=param,
                headers=headers,
                timeout=5
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            self.fail(f"请求失败，错误信息: {e}")


        return response

    '''
    下载文件
    '''
    def test_getDownLoadFile_all_param(self):
        """
        全部参数查询
        :return:
        """
        params = {
            'dirPath': f'/xxx/xxx',
            'fileName': ''
        }

        headers = {
            'User-Agent':'firefox'
        }

        expected_status_code = 200

        response = self.public_request(params,headers)

        # 断言状态码
        self.assertEqual(response.status_code, expected_status_code,
                         f"预期状态码为： {expected_status_code}, 实际为： {response.status_code}")
        # 断言错误信息
        # self.assertEqual(response.status_code, expected_status_code,
        #                  f"预期返回信息为： {expected_status_code}, 实际为： {response.status_code}")
        # 断言响应体
        # try:
        #     response_data = json.loads(response.text)
        # except json.JSONDecodeError:
        #     self.fail("Response 格式不是json")
        #
        # self.assertIn('total', response_data, "Response 中没有 'total' 字段")
        # 需求单号为唯一时，可以精确断言返回内容


    def getDownLoadFile_empty_pram(self,data,header,pramname,param_type):
        """
        必填参数为空通用查询
        :return:
        """

        expected_status_code = 200

        response = self.public_request(data, header)

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


    def test_getDownLoadFile_empty_dirpath(self):
        params = {
            'dirPath': '',
            'fileName': 'XXXX'
        }

        headers = {
            'User-Agent': 'firefox'
        }
        self.getDownLoadFile_empty_pram(params, headers,'dirPath','empty')

    def test_getDownLoadFile_empty_filename(self):
        params = {
            'dirPath': f'/xxx/xxx',
            'fileName': ''
        }

        headers = {
            'User-Agent': 'firefox'
        }
        self.getDownLoadFile_empty_pram(params, headers,'dirPath','empty')



