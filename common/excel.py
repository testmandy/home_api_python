# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 10:49
# @Author  : mandy
# excel的封装
import xlwt
from xlutils.copy import copy
import xlrd
import conftest


class Excel:
    def __init__(self, file_path=None, sheet_id=None):
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            try:
                self.file_path = conftest.excel_dir
                sheet_id = 0
            except Exception as msg:
                print(u'文件不存在%s' % msg)
        global workbook, sheet
        workbook = self.open_excel()
        sheet = self.get_sheet(sheet_id)

    def open_excel(self):
        '''获取工作簿'''
        workbook = xlrd.open_workbook(self.file_path)
        return workbook

    def get_sheet(self, index=0):
        '''获取表单'''
        return workbook.sheet_by_index(index)

    def get_rows(self):
        '''获取行数'''
        return sheet.nrows

    def get_cols(self):
        '''获取列数'''
        return sheet.ncols

    def get_row_data(self, rowx):
        '''获取一行数据'''
        return sheet.row_values(rowx)

    def get_col_data(self, colx):
        '''获取一列数据'''
        return sheet.col_values(colx)

    def get_cell(self, rowx, colx):
        '''获取单元格的值'''
        return sheet.cell_value(rowx, colx)

    def release(self):
        '''释放excel减少内存'''
        workbook.release_resources()
        del workbook

    # 写入数据并保存
    def write_data(self, rowx, colx, data=None, style=None):
        '''写入单元格数据'''
        wb = copy(workbook)
        ws = wb.get_sheet(0)
        ws.write(rowx, colx, data, style)
        wb.save(self.file_path)

# if __name__ == '__main__':
#     excel = Excel()
#     cell_value = excel.get_cell(1, 1)
#     row_value = excel.get_row_data(1)
#     print(row_value)
#     excel.write_data(3, 2, 'test')

