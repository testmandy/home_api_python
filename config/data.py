# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 15:30
# @Author  : mandy
import xlwt

from common.excel import Excel


class Data:
    col_case_id = 0
    col_api = 1
    col_is_live = 2
    col_is_run = 3
    col_method = 4
    col_is_header = 5
    col_depend_id = 6
    col_depend_data = 7
    col_depend_key = 8
    col_request_data = 9
    col_expect = 10
    col_result = 11

    def __init__(self):
        self.data = Excel()
        pass

    def get_case_id(self, rowx):
        colx = Data.col_case_id
        return self.data.get_cell(rowx, colx)

    def get_api(self, rowx):
        colx = Data.col_api
        return self.data.get_cell(rowx, colx)

    def get_is_live(self, rowx):
        colx = Data.col_is_live
        return self.data.get_cell(rowx, colx)

    def get_is_run(self, rowx):
        colx = Data.col_is_run
        return self.data.get_cell(rowx, colx)

    def get_method(self, rowx):
        colx = Data.col_method
        return self.data.get_cell(rowx, colx)

    def get_is_header(self, rowx):
        colx = Data.col_is_header
        return self.data.get_cell(rowx, colx)

    def get_depend_id(self, rowx):
        colx = Data.col_depend_id
        return self.data.get_cell(rowx, colx)

    def get_depend_data(self, rowx):
        colx = Data.col_depend_data
        return self.data.get_cell(rowx, colx)

    def get_depend_key(self, rowx):
        colx = Data.col_depend_key
        return self.data.get_cell(rowx, colx)

    def get_request_data(self, rowx):
        colx = Data.col_request_data
        return self.data.get_cell(rowx, colx)

    def get_expect(self, rowx):
        colx = Data.col_expect
        return self.data.get_cell(rowx, colx)

    def row_total(self):
        return self.data.get_rows()

    def write_passed_result(self, rowx):
        # 设置样式
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 3  # 5 背景颜色为黄色
        # 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
        # 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal,
        # 22 = Light Gray, 23 = Dark Gray
        style = xlwt.XFStyle()
        style.pattern = pattern
        # 写入数据并保存
        colx = Data.col_result
        self.data.write_data(rowx, colx, 'PASS', style)

    def write_failed_result(self, rowx, actual_result):
        # 设置样式
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 2  # 5 背景颜色为黄色
        # 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
        # 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal,
        # 22 = Light Gray, 23 = Dark Gray
        style = xlwt.XFStyle()
        style.pattern = pattern
        # 写入数据并保存
        colx = Data.col_result
        self.data.write_data(rowx, colx, actual_result, style)


if __name__ == '__main__':
    data = Data()
    cell = data.get_api(1)
    print(cell)
