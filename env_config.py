import base64
import gzip
from io import BytesIO
from datetime import datetime
from enum import Enum
import unittest
from xml.etree import ElementTree as ET
from lxml import etree

# 环境配置（单独文件）
class EnvConfig:
    # 定义不同环境的基础地址
    BASE_URLS = {
        'idc': 'http://10.180.65.178:8080',    #老系统
        # 'checkaccept': 'http://10.190.65.24:8080',    #老系统
        'checkaccept': 'http://10.190.140.43:33002',    #新系统
        'Qqproduction': 'http://10.34.45.19:8080',    #老系统
        'produce': 'http://120.52.40.45:48080',    #老系统
    }

    # 当前环境（默认test，可通过修改切换）
    CURRENT_ENV = 'checkaccept'

    @classmethod
    def get_base_url(cls):
        """获取当前环境的基础URL"""
        return cls.BASE_URLS[cls.CURRENT_ENV]

class Base64Util:
    @staticmethod
    def encode_string(params: str) -> str:
        """
        GZIP压缩后Base64编码
        :param params: 输入字符串
        :return: Base64编码后的GZIP压缩字符串
        """
        if not params or not params.strip():
            return ""

        # 使用GZIP压缩
        buffer = BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode='wb') as f:
            f.write(params.encode('utf-8'))

        # Base64编码
        return base64.b64encode(buffer.getvalue()).decode('ascii')

    @staticmethod
    def decode_string(base64_params: str) -> str:
        """
        Base64解码后GZIP解压
        :param base64_params: Base64编码的GZIP压缩字符串
        :return: 原始字符串
        """
        if not base64_params or not base64_params.strip():
            return ""

        # Base64解码
        compressed_data = base64.b64decode(base64_params)

        # GZIP解压
        buffer = BytesIO(compressed_data)
        with gzip.GzipFile(fileobj=buffer, mode='rb') as f:
            decompressed_data = f.read()

        return decompressed_data.decode('utf-8')

class DatePattern:
    """日期格式常量类"""
    P12 = "%Y%m%d%H%M"  # 年月日时分格式

class CustCompanyEnum(Enum):
    """运营商枚举类"""
    CHINA_MOBILE=("1001", "efg", "uvw")
    CHINA_UNICOM=("1002", "ghi", "rst")
    CHINA_TELECOM=("1003", "abc", "xyz")
    CHINATOWER_CRM=("1004", "000", "999")
    CHINATOWER_WY=("1005", "111", "888")
    CHINATOWER_XY=("1006", "222", "777")
    CHINATOWER_MH=("1007", "333", "666")
    CHINATOWER_XZ=("1008", "", "")
    CHINATOWER_HT=("1009", "444", "555")
    CHINATOWER_JH=("1010", "jjj", "hhh")

    def __init__(self, sys_code, prefix, suffix):
        self.sys_code = sys_code
        self.prefix = prefix
        self.suffix = suffix

    @classmethod
    def from_sys_code(cls, sys_code: str):
        """根据运营商编号获取枚举实例"""
        for company in cls:
            if company.sys_code == sys_code:
                return company
        return None

class SoapResponseHandle:
    # @staticmethod
    # def process_soap_response(soap_response):
    #     """
    #     处理SOAP响应，提取并解密returnXml中的内容
    #     :param soap_response: SOAP响应XML字符串
    #     :return: 包含解密后内容的SOAP响应字符串
    #     """
    #     try:
    #         # 解析SOAP响应XML
    #         root = ET.fromstring(soap_response)
    #         # 定义命名空间
    #         ns = {
    #             'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    #             'ns2': 'http://webservice.service.sys.org/'
    #         }
    #
    #         # 方法2：使用更灵活的查找方式
    #         for node_name in [
    #             './/{http://webservice.service.sys.org/}returnXml',
    #             './/returnXml',
    #             './{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://webservice.service.sys.org/}TowerTerminationConfirmOTResponse/{http://webservice.service.sys.org/}returnXml'
    #         ]:
    #             return_xml_element = root.find(node_name, ns)
    #             if return_xml_element is not None:
    #                 break
    #
    #         # 获取加密内容
    #         encrypted_content = return_xml_element.text.strip()
    #
    #         # Base64解码
    #         decoded_content = Base64Util.decode_string(encrypted_content)
    #
    #         # 返回处理后的完整SOAP响应的returnXml数据
    #         return decoded_content
    #
    #     except Exception as e:
    #         raise Exception(f"处理SOAP响应时出错: {str(e)}")

    @staticmethod
    def get_return_xml_value(soap_response):
        # 解析 XML
        root = etree.fromstring(soap_response)

        # # 定义命名空间
        # namespaces = {
        #     'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        #     'ns2': 'http://webservice.service.sys.org/'
        # }
        #
        # # 使用 XPath 查找
        # return_xml_elements = root.xpath('//ns2:returnXml', namespaces=namespaces)

        # if return_xml_elements and return_xml_elements[0].text:
        #     return return_xml_elements[0].text

        # 备用方法：不依赖命名空间前缀
        return_xml_elements = root.xpath('//*[local-name()="returnXml"]')
        if return_xml_elements and return_xml_elements[0].text:
            # 获取加密内容
            encrypted_content = return_xml_elements[0].text.strip()
            # Base64解码
            decoded_content = Base64Util.decode_string(encrypted_content)
            # 返回处理后的完整SOAP响应的returnXml数据
            response_returnxml = ET.fromstring(decoded_content)
            return response_returnxml

        raise ValueError("returnXml element not found or empty")

class TokenGenerator:
    @staticmethod
    def generate_access_token(sys_code: str, service_code: str) -> str:
        """
        生成访问令牌 (AccessToken)

        :param sys_code: 运营商编号 (如: "1001")
        :param service_code: 服务编码 (如: "T09_OT_013")
        :return: Base64编码后的GZIP压缩令牌字符串
        :raises: ValueError 当运营商编号无效时
        """
        # 验证运营商编号有效性
        company = CustCompanyEnum.from_sys_code(sys_code)
        if not company:
            raise ValueError(f"无效的运营商编号: {sys_code}")

        # 构建原始Token字符串
        timestamp = datetime.now().strftime(DatePattern.P12)
        raw_token = f"{sys_code}{company.prefix}{service_code}{company.suffix}{timestamp}"

        # 使用GZIP压缩后进行Base64编码
        try:
            return Base64Util.encode_string(raw_token)
        except Exception as e:
            raise RuntimeError(f"Token生成失败: {str(e)}")

class GetCurrentTime():
    @staticmethod
    def get_current_time():
        """获取当前时间，格式为YYYY-MM-DD HH:MM:SS"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

