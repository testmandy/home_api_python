# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 10:50
# @Author  : mandy
import json

import requests


class Request:
    def __init__(self):
        pass

    def get_method(self, url, data, headers=None):
        if headers is None:
            res = requests.get(url=url, data=data).json()
        else:
            res = requests.get(url=url, headers=headers, data=data).json()
        res = json.dumps(res, indent=2)
        return res

    def post_method(self, url, data, headers=None):

        if headers is None:
            res = requests.post(url=url, data=data, encoding='utf-8').json()
        else:
            res = requests.post(url=url, headers=headers, data=data).json()
        res = json.dumps(res, indent=2)
        return res

    def main(self, method, url, data=None, headers=None):
        print(u'请求接口为：%s' % url)
        print(u'请求头信息：%s' % headers)
        print(u'请求body：%s' % data)
        if method == ('get' or 'GET'):
            res = self.get_method(url, data, headers)
        elif method == ('post' or 'POST'):
            res = self.post_method(url, data, headers)
        else:
            print(u'unkown method')
            res = None
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return res
