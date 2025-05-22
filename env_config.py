# 环境配置（单独文件）
class EnvConfig:
    # 定义不同环境的基础地址
    BASE_URLS = {
        'idc': 'http://10.180.65.178:8080',
        'checkaccept': 'http://10.190.65.24:8080',
        'Qqproduction': 'http://10.34.45.19:8080',
        'produce': 'http://120.52.40.45:48080',
    }

    # 当前环境（默认test，可通过修改切换）
    CURRENT_ENV = 'produce'

    @classmethod
    def get_base_url(cls):
        """获取当前环境的基础URL"""
        return cls.BASE_URLS[cls.CURRENT_ENV]