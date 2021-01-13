import yaml
import os

'''通过文件所在路径读取并返回文件内容'''
# def readyml(yamlpath):
#     '''读取yaml文件'''
#     if  not os.path.isfile(yamlpath):
#         raise FileNotFoundError("文件不存在，请检查文件路径是否正确：%s"%yamlpath)
#     #open方法打开直接读取
#     f = open(yamlpath,'r',encoding='utf-8')
#     cfg = f.read()
#     d = yaml.load(cfg)
#     print("读取的测试文件数据：%s"%d)
#     return d

#绝对路径
curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ymlpath = os.path.join(curpath, "case\\login_box\\test_data.yml")
def get_test_data(ymlpath):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    if not os.path.exists(ymlpath):
        raise  FileNotFoundError('文件不存在，请检查文件路径{}是否正确'.format(ymlpath))

    with open(ymlpath,encoding="utf-8") as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['testcases']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters

if __name__ == '__main__':
    cases,parameters = get_test_data(ymlpath)
    print(list(parameters))

    # print(curpath)
    # print(ymlpath)

