# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 19:45
# @Author  : mandy
import json
import time

import pytest
from common.Init import TestInit


@pytest.mark.run(order=3)
class TestTutor(TestInit):
    def get_result(cls, url, data):
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u'请求结果为：%s' % res)
        cls.compare_msg(res)

    def compare_msg(cls, res):
        json_res = json.loads(res)
        if json_res['msg'] == ('success' or 'SUCCESS'):
            print(u'------------测试通过(^_^)------------')
        else:
            print(u'------------测试未通过/(ㄒoㄒ)/~~------------')

    @pytest.mark.skip
    def test_login_success(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.login_uri
        data = {'username': cls.username, 'password': cls.password}
        cls.get_result(url, data)

    # @pytest.mark.skip
    def test_queryCourseList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryCourseList_uri
        data = {'user_id': cls.tutor_id}
        cls.get_result(url, data)

    # @pytest.mark.skip
    def test_queryList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryList_uri
        data = {
            'tutor_id': cls.tutor_id,
            'name': '学',
            'mobile': 13,
            'tag_id': [20, 21],
            'tag_count': 2,
            'currPage': 1,
            'pageSize': 1
        }
        cls.get_result(url, data)

    # @pytest.mark.skip
    def test_getSudentByName(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getSudentByName_uri
        data = {
            'nice_student.tutor_id': cls.tutor_id,
            'nice_student.real_name': '测试',
            'page.currPage': 1,
            'page.pageSize': 10
        }
        cls.get_result(url, data)

    def test_awardCoin(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.awardCoin_uri
        data = [{
            'tutor_id': cls.tutor_id,
            'coin': 1,
            'users': ['4711', '4712', '4713', '4714', '4715', '4716', '4717', '4718', '4719', '4720', '4721', '4722',
                      '4723']
        }]
        cls.get_result(url, data)

    def test_queryStudentAnalysis(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryStudentAnalysis_uri
        data = {
            'course_period_id': cls.course_period_id,
            'lesson_id': cls.lesson_id,
            'teacher_id': cls.teacher_id,
            'class_id': cls.class_id
        }
        cls.get_result(url, data)

    def test_queryStudentList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryStudentList_uri
        data = {
            'course_period_id': cls.course_period_id,
            'lesson_id': cls.lesson_id,
            'teacher_id': cls.teacher_id,
            'class_id': cls.class_id
        }
        cls.get_result(url, data)
