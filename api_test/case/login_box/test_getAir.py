import requests
import pytest
import os
# from common import read_yml
from common.read_yml import *
import jsonpath
base_url = os.path.dirname(__file__)
ymlpath = os.path.join(base_url,'test_data.yml')


cases, parameters = get_test_data(ymlpath)
list_params=list(parameters)

class TestInTheaters(object):

    @pytest.fixture(scope="function")
    def preparation(self):
        print("在数据库中准备测试数据")
        test_data = "在数据库中准备测试数据"
        yield test_data
        print("清理测试数据")


    @pytest.mark.parametrize("case,http,expected",list(list_params),ids= cases)
    def test_in_theaters(self,preparation,env,case,http,expected):#实现测试数据与用例代码逻辑分离
        '''[
                ('验证响应中status和message与预期一致',
                    {
                    'method': 'GET',
                     'path': '/weather/v1/',
                    'headers': {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                                },
                     'params': {
                                'ak': 'SKEu06VYg5GH6VA7zERlpM33acLOKNBG',
                                'district_id': 222405,
                                'data_type': 'all'
                                }
                    },
                    {
                    'status': 0,
                    'message': 'success'
                        }
                ),
                 ('你好',
                    {
                    'method': 'POST',
                    'path': '/weather/v1/',
                    'headers':{
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
                                },
                    'params': {
                                'ak': 'SKEu06VYg5GH6VA7zERlpM33acLOKNBG',
                                'district_id': 222405,
                                'data_type': 'all'
                                }
                    },
                    {
                    'status': 0,
                    'message': 'success'
                        }
                     )
                ]'''
        # host = "http://api.map.baidu.com"
        #[0][1]中0表示是第一条用例（列表中的第一个小元祖），1表示小元祖其中的字典“http”键的值--请求内容
        # ps:小元祖中的内容分为三块，第一部分为用例标题，为字符串的形式；第二块是http的请求主体内容；第三块是预期结果的内容；后面两块都是以字典数据类型存储表达
        #所以基本的形式有[i][0],[i][1],[i][2],i为用例的条数
        # r = requests.request(list_params[0][1]["method"],
        #                      url=host + list_params[0][1]["path"],
        #                      headers=list_params[0][1]["headers"],
        #                      params=list_params[0][1]["params"])

        r = requests.request(http["method"],
                             url=env["host"]["air"] + http["path"],
                             headers=http["headers"],
                             params=http["params"]
                             )
        response = r.json()
        print(response)
        # assert response["status"] == 0
        # assert response["status"] == list_params[0][2]['response']['status']
        #以下是经过参数化改良后的断言内容表达式
        # assert response["status"] == expected['response']['status']
        # assert response['message'] == expected['response']['message']
        #以下是采用jsonpath的方式来提取断言表达
        assert jsonpath.jsonpath(response,"$.message") == expected['response']['message']

        #对于同一接口的用例设计，这里测试预期结果待验证字段应该是保持相同的，属于同一接口不同用例响应结果交集的这一部分。
        # assert response["message"] == "failed", "实际的结果是：{}".format(response["message"])


# class TestAirInfo():
#     def test_get_airinfo(self):
#         host = "http://api.map.baidu.com"
#         # url = "/weather/v1/"
#         # params = {
#         #     "district_id":222405,
#         #     "data_type": "all",
#         #     "ak": "SKEu06VYg5GH6VA7zERlpM33acLOKNBG"
#         #
#         # }
#         # headers = {
#         #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
#         #     "Content-Type":"application/x-www-form-urlencoded"
#         # }
#         res = requests.request('GET',
#                                url=host+url,
#                                params=params,
#                                headers= headers
#                                ).json()
#         print(res)
#         assert res['status']==0

#py.test -s -q --tb=no -n auto  case/login_box/test_getAir.py
#py.test  case/login_box/test_getAir.py
#生成报告三部走
#pytest case/login_box
#pytest --alluredir=./report/allure_raw
#allure generate ./report/allure_raw -o ./report/html
#allure generate ${WORKSPACE}/allure-results -o ${WORKSPACE}/allure-results/html

if __name__=='__main__':

    pytest.main()







