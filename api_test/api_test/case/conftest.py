import requests
import pytest
import os
import yaml
from case.common_function import login

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")

@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                                request.config.getoption('environment'),
                               "config.yml")

    with open(config_path,encoding='utf-8') as f:
        env_config = yaml.load(f.read(),Loader=yaml.SafeLoader)
        print(env_config)
        return env_config



@pytest.fixture(scope='module')
def login_fix():
    '''首次登陆用，自定义一个module级别的关于登陆的前置操作'''
    print("测试前先登录--conftest打印内容")
    s = requests.Session()
    token = login(s)
    return s,token
@pytest.fixture(scope="function")
def unlogin_fix():
    '''登录后就无须重复再登陆了'''
    print("无须再登陆了")
    s = requests.Session()
    s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
    return s

@pytest.fixture(scope='session')
def login_test():
    print('用例先登录')


