import os
import pytest
from case.send_emails import *

curpath = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(curpath,r"case/")
if __name__ == '__main__':

    pytest.main(['-s',case_path])
    s = SendEmail('smtp.qq.com',587,'807737661@qq.com',"hciwptgmehzzbdeh", ['wesley.wang@feisu.com', 'lin799891@163.com'],u'完整测试一次')
    s.sendFile(r"D:\BaiduNetdiskDownload\api_test\report.html")