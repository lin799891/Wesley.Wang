import allure
import pytest

@allure.step('step one:clickxxx')
def step_1():
    print('1')

@allure.step('step two:clickxxx')
def step_2():
    print('2')

@allure.feature('编辑页面')
class TestEditPage():
    '''用例描述：先登录，然后再干嘛干嘛'''

    @allure.story('这是一个测试用例')
    def test_1(self,login_test):
        "用例描述：test_1"
        step_1()
        step_2()
        print('test_1')

    @allure.story('登录后进入个人中心')
    def test_2(self,login_test):
        "用例描述：test_2"
        print('test_2')
