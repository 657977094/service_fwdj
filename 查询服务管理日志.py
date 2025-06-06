import json
import unittest
import requests
from env_config import EnvConfig


class TestQryFlowLog(unittest.TestCase):

    def public_request(self,data):
        try:
            response = requests.get(
                url=f'{EnvConfig.get_base_url()}/admin/qry/qryFlowLog',
                params=data,
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
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '124415235235',
            'page': 1,
            'size': 100
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

            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))  # 调试查看

            # 需求单号为唯一时，可以精确断言返回内容
            self.assertEqual(response_data["data"]["data"]["rows"][0]["requestId"], data["requestId"],
                             f"不匹配，预期: {data['requestId']}，实际: {response_data['data']['data']['rows'][0]['requestId']}")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

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
            self.assertEqual(response_data['data']['code'], 'FAILURE',
                             f"预期返回状态为： FAILURE, 实际为： {response_data['data']['code']}")
            self.assertEqual(response_data['data']['msg'], f'{pramname}不能为空，请录入后再进行查询！',
                                 f"预期返回信息为： {pramname}不能为空，请录入后再进行查询！, 实际为： {response_data['data']['msg']}")
        elif param_type == 'error':
            # 断言错误信息
            self.assertEqual(response_data['data']['code'], 'FAILURE',
                             f"预期返回状态为： FAILURE, 实际为： {response_data['data']['code']}")
            self.assertEqual(response_data['data']['msg'], '【分页起始页码】和【每页数据量】值必须大于0！',
                             f"预期返回信息为：【分页起始页码】和【每页数据量】值必须大于0！, 实际为： {response_data['data']['msg']}")
        elif param_type == 'default':
            self.assertEqual(len(response_data['data']['data']['rows']), '10',
                             f"预期返回数据条数为：'10', 实际数据条数为： {len(response_data['data']['data']['rows'])}")
        elif param_type == 'prcode_error':
            self.assertEqual(response_data['data']['code'], 'FAILURE',
                             f"预期返回状态为： FAILURE, 实际为： {response_data['data']['code']}")
            self.assertEqual(response_data['data']['msg'], f'{pramname}编码不存在，请重新录入后再进行查询！',
                             f"预期返回信息为： {pramname}编码不存在，请重新录入后再进行查询！, 实际为： {response_data['data']['msg']}")
        elif param_type == 'requestid_error':
            self.assertEqual(response_data['data']['code'], 'FAILURE',
                             f"预期返回状态为： FAILURE, 实际为： {response_data['data']['code']}")
            self.assertEqual(response_data['data']['msg'], f'{pramname}只能为数字，请录入后再进行查询！',
                             f"预期返回信息为： {pramname}只能为数字，请录入后再进行查询！, 实际为： {response_data['data']['msg']}")
        elif param_type == 'len_error':
            self.assertEqual(response_data['data']['code'], 'FAILURE',
                             f"预期返回状态为： FAILURE, 实际为： {response_data['data']['code']}")
            self.assertEqual(response_data['data']['msg'], f'{pramname}长度不能超过20！',
                             f"预期返回信息为： {pramname}长度不能超过20！, 实际为： {response_data['data']['msg']}")
        else:
            self.fail(f"未定义的传入参数{param_type}")



    def test_postQryFlowLog_empty_province(self):
        data = {
            'provinceCode': '',
            # 'city': '',
            'requestId': '124415235235',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【省份】','empty')


    def test_postQryFlowLog_empty_requestId(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【需求单号】','empty')

    def test_postQryFlowLog_empty_start(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '124415235235',
            'page': '',
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'page','default')

    def test_postQryFlowLog_empty_limit(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '124415235235',
            'page': 1,
            'size': ''
        }
        self.postQryFlowLog_empty_pram(data,'size','default')


    def test_postQryFlowLog_error_type_size(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '124415235235',
            'page': 1,
            'size': -1
        }
        self.postQryFlowLog_empty_pram(data,'size','error')

    def test_postQryFlowLog_error_type_page(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '124415235235',
            'page': -1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'page','error')

    def test_postQryFlowLog_error_provincecode(self):
        data = {
            'provinceCode': 123123,
            # 'city': '',
            'requestId': '124415235235',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【省份】','prcode_error')

    def test_postQryFlowLog_char_requestid(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '啊',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【需求单号】','requestid_error')

    def test_postQryFlowLog_english_requestid(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': 'asdasd',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【需求单号】','requestid_error')

    def test_postQryFlowLog_symbol_requestid(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '%',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【需求单号】','requestid_error')

    def test_postQryFlowLog_len_requestid(self):
        data = {
            'provinceCode': 110000,
            # 'city': '',
            'requestId': '123451234512345123451',
            'page': 1,
            'size': 100
        }
        self.postQryFlowLog_empty_pram(data,'【需求单号】','len_error')

if __name__ == '__main__':
    unittest.main()