# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:07
# @Author  : mandy
import json

from common.request import Request
from config.data import Data
from util.read_ini import ReadIni


class RunExcel:
    def __init__(self):
        self.dt = Data()
        readIni = ReadIni()
        self.base_url = readIni.get_value('base_url', 'api')
        self.schoolweb_url = readIni.get_value('schoolweb_url', 'api')
        self.req = Request()
        self.row_total = self.dt.row_total()

    def run_dependent(self, i):
        depend_id = self.dt.get_depend_id(i)
        depend_data = self.dt.get_depend_data(i)
        depend_key = self.dt.get_depend_key(i)
        # 轮询case id
        for j in range(0, self.row_total):
            name = self.dt.get_case_id(j)
            # 如果找到了目标依赖用例，则先执行，再把依赖数据写入depend_data中
            if depend_id == name:
                res = self.get_result(j)
                json_res = json.loads(res, encoding='utf-8')

                depend_data = json_res[depend_key]
                self.dt.write_failed_result()

    def get_result(self, i):
        uri = self.dt.get_api(i)
        is_live = self.dt.get_is_live(i)
        method = self.dt.get_method(i)
        is_header = self.dt.get_is_header(i)
        request_data = self.dt.get_request_data(i)
        expect = self.dt.get_expect(i)
        result = self.dt.get_result(i)

        # 拼接请求地址
        if is_live == 'no' or 'NO':
            url = self.schoolweb_url + uri
        else:
            url = self.base_url + uri
        # 判断是否需要请求头
        print(u'是否有请求头：%s' % is_header)
        if is_header == 'no':
            print(method + url + request_data)
            res = self.req.main(method, url, request_data)
            print(res)
        else:
            headers = {'Content-Type': 'application/json;charset=UTF-8',
                       'token': '3552ed08e78b272a2988a1f283ac949cc054'}
            res = self.req.main(method, url, request_data, headers)
            print(res)
            self.compare_msg(i, res)
            return res

    def compare_msg(self, i, res):
        json_res = json.loads(res, encoding='utf-8')
        if json_res['msg'] == ('success' or 'SUCCESS'):
            print(u'------------测试通过(^_^)------------')
            self.dt.write_passed_result(i)
        else:
            print(u'------------测试未通过/(ㄒoㄒ)/~~------------')
            self.dt.write_failed_result(i, res)

    def run(self):
        print(u'行数：', self.row_total)
        for i in range(1, self.row_total):
            print(u'开始执行第 %d 行' % i)
            # 如果运行
            if self.dt.get_is_run(i) == 'yes' or 'YES':
                self.get_result(i)


if __name__ == '__main__':
    excel = RunExcel()
    excel.run()







