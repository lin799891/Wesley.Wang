import requests
import json

#公共的函数


def login(s):
    '''登陆获取token'''
    # s  = requests.Session()
    url = "http://54.245.72.232/api/RequestToken"
    body ={
        "param": '{"emailAddress":"d2VzbGV5LndhbmdAZmVpc3UuY29t","passWord":"eXV4dWFuMzUwNw=="}'
        # "param": '{"emailAddress":"cm95LmxpQGZlaXN1LmNvbQ==","passWord":"eXV4dWFuMzUwNw=="}'
    }
    h={
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Bearer null",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    r = s.post(url=url,data=body,headers = h)
    print(r.json())

    #按照键值取出token
    token = r.json()["obj"]["token"]
    # print(token+"--登陆后取出的token")


    s.headers.update(h)
    # print(s.headers)
    return token


if __name__ == '__main__':
    s = requests.Session()
    login(s)