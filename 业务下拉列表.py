import requests
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestGetSelects(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/commonController/getSelects"
    # BASE_URL = "http://120.52.40.45:48080/commonController/getSelects"   #接口地址
    def test_getSelects_custSystemCode(self):
        selectName = "CUST_SYSTEM_CODE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1001", "text": "移动"},
                {"value": "1002", "text": "联通"},
                {"value": "1003", "text": "电信"},
                {"value": "1004", "text": "CRM"},
                {"value": "1005", "text": "物业"},
                {"value": "1006", "text": "选址"},
                {"value": "1007", "text": "门户"},
                {"value": "1008", "text": "资源"},
                {"value": "1009", "text": "合同"},
                {"value": "1010", "text": "稽核"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_cscPrCode(self):
        selectName = "CUST_SYSTEM_CODE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {
            "parentCode" : "CUST"
        }

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1001", "text": "移动"},
                {"value": "1002", "text": "联通"},
                {"value": "1003", "text": "电信"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_ftpLogStatus(self):
        selectName = "FTP_LOG_STATUS"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1", "text": "操作成功"},
                {"value": "2", "text": "操作失败"},
                {"value": "3", "text": "系统出错"},
                {"value": "4", "text": "超时回收"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_fileSource(self):
        selectName = "FILE_SOURCE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1", "text": "登记上传"},
                {"value": "2", "text": "定时扫描"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_fileStatus(self):
        selectName = "FILE_STATUS"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1", "text": "启用"},
                {"value": "2", "text": "未启用"},
                {"value": "3", "text": "停用"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_ftpHandlerType(self):
        selectName = "FTP_HANDLER_TYPE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1", "text": "上传"},
                {"value": "2", "text": "下载"},
                {"value": "3", "text": "通知上传完成"},
                {"value": "4", "text": "通知下载完成"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_fhtPrCode(self):
        selectName = "FTP_HANDLER_TYPE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {
            "parentCode" : 1
        }

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "1", "text": "上传"},
                {"value": "2", "text": "下载"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_serviceCode(self):
        selectName = "SERVICE_CODE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {}

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            # print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "T03_OT_004", "text": "批量起租"},
                {"value": "T03_OT_006", "text": "业务变更"},
                {"value": "T03_OT_008", "text": "服务终止"},
                {"value": "T05_OT_001", "text": "结算详单"},
                {"value": "T05_OT_002", "text": "确认费用"},
                {"value": "T05_OT_003", "text": "对账确认"},
                {"value": "T06_OT_005", "text": "电费清单"},
                {"value": "T02_OT_001", "text": "需求提交导入服务"},
                {"value": "T02_TO_001", "text": "需求承接结果反馈服务"},
                {"value": "T02_TO_002", "text": "筛查结果反馈服务"},
                {"value": "T02_OT_002", "text": "筛查确认结果导入服务"},
                {"value": "T03_TO_001", "text": "需求订单同步服务"},
                {"value": "T03_OT_001", "text": "需求订单确认结果导入服务"},
                {"value": "T03_TO_002", "text": "需求订单交付验收信息同步服务"},
                {"value": "T03_OT_002", "text": "需求订单交付验收结果导入服务"},
                {"value": "T03_TO_003", "text": "起租通知信息同步服务"},
                {"value": "T03_OT_003", "text": "起租确认结果导入服务"},
                {"value": "T03_TO_009", "text": "需求取消接口"},
                {"value": "T03_OT_009", "text": "需求取消确认接口"},
                {"value": "T03_TO_010", "text": "起租归档通知接口"},
                {"value": "T07_OT_001", "text": "操作历史查询服务(运营商查铁塔)"},
                {"value": "T07_TO_001", "text": "操作历史查询服务(铁塔查运营商)"},
                {"value": "T03_OT_011", "text": "需求取消接口（运营商发起）"},
                {"value": "T03_TO_011", "text": "需求取消确认接口（铁塔发起确认）"},
                {"value": "T03_TO_014", "text": "起租前需求变更申请接口（铁塔申请）"},
                {"value": "T03_OT_014", "text": "起租前需求变更确认接口（运营商确认）"},
                {"value": "T03_OT_015", "text": "起租前需求变更申请接口（运营商申请）"},
                {"value": "T03_TO_015", "text": "起租前需求变更确认接口（铁塔确认）"},
                {"value": "T03_TO_016", "text": "起租后需求变更申请接口（铁塔申请）"},
                {"value": "T03_OT_016", "text": "起租后需求变更确认接口（运营商确认）"},
                {"value": "T03_OT_017", "text": "起租后需求变更申请接口（运营商申请）"},
                {"value": "T03_TO_017", "text": "起租后需求变更确认接口（铁塔确认）"},
                {"value": "T03_OT_0041", "text": "批量起租补充"},
                {"value": "T06_TO_007", "text": "分摊账单"},
                {"value": "T05_OT_005", "text": "站址信息文件"},
                {"value": "T03_TO_018", "text": "起租后变更归档接口"},
                {"value": "T09_TO_012", "text": "服务终止申请导入接口（铁塔申请）"},
                {"value": "T09_OT_012", "text": "服务终止确认接口（运营商确认）"},
                {"value": "T09_OT_013", "text": "服务终止申请导入接口（运营商申请）"},
                {"value": "T09_TO_013", "text": "服务终止确认接口（铁塔确认）"},
                {"value": "T09_TO_019", "text": "服务终止归档接口"},
                {"value": "T07_TO_002", "text": "业务申请状态通知服务（铁塔发起）"},
                {"value": "T05_TO_004", "text": "调账清单"},
                {"value": "T07_OT_002", "text": "业务申请状态通知服务（运营商发起）"},
                {"value": "T06_TO_006", "text": "油机发电清单"},
                {"value": "T03_OT_012", "text": "订单预警接口"},
                {"value": "T03_OT_013", "text": "需求撤回接口"},
                {"value": "T05_OT_006", "text": "场地费合同"},
                {"value": "T18_JT_001", "text": "比对结果"},
                {"value": "T05_TO_003", "text": "对账确认（运营商）"},
                {"value": "T05_TO_005", "text": "出对账情况报表（运营商）"},
                {"value": "T03_OT_020", "text": "费用稽核退回接口"},
                {"value": "T05_TO_001", "text": "结算详单（运营商）"},
                {"value": "T05_TO_006", "text": "订单数据（运营商）"},
                {"value": "T03_OT_004HZ", "text": "起租单回执文件"},
                {"value": "T05_OT_001HZ", "text": "结算详单回执文件"},
                {"value": "T04_TO_001", "text": "数据管控推送服务"},
                {"value": "T06_TO_008", "text": "分摊账单(物业推送/天)"},
                {"value": "T06_OT_008", "text": "分摊账单(运营商推送/天)"},
                {"value": "T06_OT_009", "text": "铁塔电费电子化对账(安徽电信)"},
                {"value": "T0_OT_009", "text": "订单比对汇总信息"},
                {"value": "T0_OT_010", "text": "订单比对详细清单"},
                {"value": "T10_OT_003", "text": "结算确认单"},
                {"value": "T09_OT_001", "text": "日耗电量"},
                {"value": "T09_OT_002", "text": "分摊比例"},
                {"value": "T03_OT_005", "text": "批量业务续签确认单"},
                {"value": "T03_0T_007", "text": "运营商结果确认文件"},
                {"value": "T05_OT_007", "text": "包干电费清单"},
                {"value": "T05_OT_100", "text": "报账清单"},
                {"value": "T05_TO_008", "text": "营收电子化结算清单"},
                {"value": "T12_OT_001", "text": "铁塔侧签章文件"},
                {"value": "T05_OT_101", "text": "标准账单对比文件"},
                {"value": "T12_TO_002", "text": "电信侧签章文件"},
                {"value": "T05_OT_102", "text": "追溯账单确认通知文件"},
                {"value": "T05_OT_103", "text": "标准账单确认通知文件"},
                {"value": "T12_OT_005", "text": "移动批量起租单计费字段（全量）文件"},
                {"value": "T12_OT_006", "text": "移动批量起租单计费字段（增量）文件"},
                {"value": "T12_OT_004", "text": "移动起租稽查文件(增量)"},
                {"value": "T12_OT_003", "text": "移动起租稽查文件(全量)"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

    def test_getSelects_scPrCode(self):
        selectName = "SERVICE_CODE"
        url=f"{self.BASE_URL}/{selectName}"
        params = {
            "parentCode" : "FTP"
        }

        try:
            response = requests.get(url, params=params)   #发起请求

            # 断言测试
            self.assertEqual(response.status_code, 200,
                             f"响应状态码不是200，实际是{response.status_code}")   #响应码校验
            response_data = response.json()      #响应结果转换为json格式
            code = "0"
            self.assertEqual(response_data["data"]["code"], code,
                             f'业务状态码不是"0"，实际是{response_data["data"]["code"]}')      #code为0表示业务成功
            print("服务器响应:", json.dumps(response_data, indent=2, ensure_ascii=False))      #调试查看

            response_data = response.json()["data"]["data"] #获取响应数据
            expected_data = [
                {"value": "T03_OT_004", "text": "批量起租"},
                {"value": "T03_OT_006", "text": "业务变更"},
                {"value": "T03_OT_008", "text": "服务终止"},
                {"value": "T05_OT_001", "text": "结算详单"},
                {"value": "T05_OT_002", "text": "确认费用"},
                {"value": "T05_OT_003", "text": "对账确认"},
                {"value": "T06_OT_005", "text": "电费清单"},
                {"value": "T05_OT_005", "text": "站址信息文件"},
                {"value": "T06_TO_007", "text": "分摊账单"},
                {"value": "T03_OT_0041", "text": "批量起租补充"},
                {"value": "T05_TO_004", "text": "调账清单"},
                {"value": "T06_TO_006", "text": "油机发电清单"},
                {"value": "T05_OT_006", "text": "场地费合同"},
                {"value": "T18_JT_001", "text": "比对结果"},
                {"value": "T05_TO_003", "text": "对账确认（运营商）"},
                {"value": "T05_TO_005", "text": "出对账情况报表（运营商）"},
                {"value": "T05_TO_001", "text": "结算详单（运营商）"},
                {"value": "T05_TO_006", "text": "订单数据（运营商）"},
                {"value": "T03_OT_004HZ", "text": "起租单回执文件"},
                {"value": "T05_OT_001HZ", "text": "结算详单回执文件"},
                {"value": "T06_TO_008", "text": "分摊账单(物业推送/天)"},
                {"value": "T06_OT_008", "text": "分摊账单(运营商推送/天)"},
                {"value": "T06_OT_009", "text": "铁塔电费电子化对账(安徽电信)"},
                {"value": "T0_OT_009", "text": "订单比对汇总信息"},
                {"value": "T0_OT_010", "text": "订单比对详细清单"},
                {"value": "T10_OT_003", "text": "结算确认单"},
                {"value": "T09_OT_001", "text": "日耗电量"},
                {"value": "T09_OT_002", "text": "分摊比例"},
                {"value": "T03_OT_005", "text": "批量业务续签确认单"},
                {"value": "T03_0T_007", "text": "运营商结果确认文件"},
                {"value": "T05_OT_007", "text": "包干电费清单"},
                {"value": "T05_OT_100", "text": "报账清单"},
                {"value": "T05_TO_008", "text": "营收电子化结算清单"},
                {"value": "T12_OT_001", "text": "铁塔侧签章文件"},
                {"value": "T05_OT_101", "text": "标准账单对比文件"},
                {"value": "T12_TO_002", "text": "电信侧签章文件"},
                {"value": "T05_OT_102", "text": "追溯账单确认通知文件"},
                {"value": "T05_OT_103", "text": "标准账单确认通知文件"},
                {"value": "T12_OT_005", "text": "移动批量起租单计费字段（全量）文件"},
                {"value": "T12_OT_006", "text": "移动批量起租单计费字段（增量）文件"},
                {"value": "T12_OT_004", "text": "移动起租稽查文件(增量)"},
                {"value": "T12_OT_003", "text": "移动起租稽查文件(全量)"}
            ]

            # 逐个验证每个字段
            for i in range(len(expected_data)):
                self.assertEqual(response_data[i]["value"],expected_data[i]["value"],
                    f"第{i + 1}条数据的value不匹配，预期: {expected_data[i]['value']}，实际: {response_data[i]['value']}")
                self.assertEqual(response_data[i]["text"],expected_data[i]["text"],
                    f"第{i + 1}条数据的text不匹配，预期: {expected_data[i]['text']}，实际: {response_data[i]['text']}")

            print("测试通过！")
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")

if __name__ == "__main__":
    unittest.main()