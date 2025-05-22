import requests
import base64
from xml.etree import ElementTree as ET
import unittest
import json
from .env_config import EnvConfig  # 导入环境配置

class TestFilesMutual(unittest.TestCase):

    base_url = EnvConfig.get_base_url()
    BASE_URL = f"{base_url}/services/filesMutual"
    # BASE_URL = "http://120.52.40.45:48080/services/filesMutual"   #接口地址

    def test_soap_ftp_files_mutual(self):

        # 原始请求XML内容（PACKET部分）
        packet_xml = """
        <PACKET>
            <HEAD>
                <SYS_COMPANY>1004</SYS_COMPANY>
                <SERVICE_CODE>T05_OT_001</SERVICE_CODE>
                <FILE_TYPE>JSXD</FILE_TYPE>
                <REQUEST_TIME>2025-04-02 22:38:50</REQUEST_TIME>
                <ACCESS_TOKEN>MTAwNDAwMFQwNV9PVF8wMDE5OTkyMDI1LTA0</ACCESS_TOKEN>
                <HANDLE_TYPE>1</HANDLE_TYPE>
                <CUST_COMPANY>1001</CUST_COMPANY>
                <ACCOUNT_PERIOD>202503</ACCOUNT_PERIOD>
                <PROVINCE_ID>650000</PROVINCE_ID>
                <CITY_ID>650000</CITY_ID>
                <FLOW_ID></FLOW_ID>
                <STATUS></STATUS>
            </HEAD>
        </PACKET>
        """

        # 构建完整的SOAP请求信封（包含encReqXml）
        soap_request = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.service.sys.org/">
           <soapenv:Header/>
           <soapenv:Body>
              <web:ftpFilesMutual>
                 <encReqXml>{packet_xml}</encReqXml>
              </web:ftpFilesMutual>
           </soapenv:Body>
        </soapenv:Envelope>
        """

        # 2. 设置请求头（SOAP接口需要特定的Content-Type）
        headers = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": ""  # 根据实际接口文档填写SOAPAction，当前wsdl中无此字段值，暂时留空
        }

        try:
            # 3. 发送POST请求
            response = requests.post(self.BASE_URL, data=soap_request, headers=headers)

            # 验证HTTP状态码为200
            assert response.status_code == 200, f"HTTP状态码非200，实际为：{response.status_code}"

            # 4. 解析SOAP响应
            response_xml = response.text

            # 使用ElementTree解析XML
            root = ET.fromstring(response_xml)

            # 查找returnXml节点（注意命名空间）
            namespaces = {
                'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ns2': 'http://webservice.service.sys.org/'
            }
            return_xml_node = root.find(".//ns2:returnXml", namespaces)

            # 验证returnXml节点存在
            assert return_xml_node is not None, "响应中未找到returnXml节点"

            # 5. 解码base64编码的returnXml内容
            encoded_content = return_xml_node.text.strip()
            decoded_bytes = base64.b64decode(encoded_content)
            decoded_xml = decoded_bytes.decode('utf-8')  # 假设编码为UTF-8

            # 预期的解码后XML内容
            expected_decoded_xml = """
            <PACKET>
                <HEAD>
                    <FLOW_ID>68498057</FLOW_ID>
                    <RESPONSE_CODE>000000</RESPONSE_CODE>
                    <RESPONSE_MSG>上传登记成功</RESPONSE_MSG>
                    <SERVICE_CODE>T05_OT_001</SERVICE_CODE>
                    <RESPONSE_TIME>2025-04-02 22:38:50</RESPONSE_TIME>
                    <FTP_USER>CRM_u_0</FTP_USER>
                    <FTP_PWD>crm468581</FTP_PWD>
                    <FILE_PATH>ftp://10.180.65.178:21/</FILE_PATH>
                    <FILE_NAME></FILE_NAME>
                </HEAD>
            </PACKET>
            """

            # 6. 完全匹配断言（去除空格和换行符进行比较）
            assert decoded_xml.strip() == expected_decoded_xml.strip(), "解码后的响应与预期不完全匹配"

            print("测试通过！解码后的响应完全匹配预期结果。")

        except Exception as e:
            print(f"接口测试失败：{str(e)}")
            raise


# 执行测试
if __name__ == "__main__":
    unittest.main()