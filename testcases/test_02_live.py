# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 19:45
# @Author  : mandy
import json
import time
import pytest
from common.Init import TestInit


@pytest.mark.run(order=2)
class TestLive(TestInit):
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

    def extract_data(cls, url, data):
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u'请求结果为：%s' % res)
        return json.loads(res)

    @pytest.mark.skip
    def test_login_success(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.login_uri
        data = {'username': cls.username, 'password': cls.password}
        cls.get_result(url, data)

    @pytest.mark.run(order=1)
    def test_qryLiveInfo(cls):
        # 拼接请求地址
        url = cls.base_url + cls.qryLiveInfo_uri
        data = {'nice_student_course_lesson_learn.lesson_id': cls.lesson_id,
                'nice_student_course_lesson_learn.course_id': cls.course_id,
                'nice_student_course_lesson_learn.course_period_id': cls.course_period_id,
                'nice_student_course_lesson_learn.user_id': cls.user_id}
        json_res = cls.extract_data(url, data)
        class_id = json_res['data']['class_id']
        cls.config.set_ini('data', 'class_id', str(class_id))
        class_group_id = json_res['data']['class_group_id']
        cls.config.set_ini('data', 'class_group_id', str(class_group_id))
        lesson_group_id = json_res['data']['lesson_group_id']
        cls.config.set_ini('data', 'lesson_group_id', str(lesson_group_id))

    def test_getCoin(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getCoin_uri
        data = {'nice_user_coin_account.user_id': cls.user_id}
        cls.get_result(url, data)

    def test_getSystemMsg(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getSystemMsg_uri
        data = {'sysCurrencyId': cls.sysCurrencyId, 'sysType': 'classroom.ppt', 'groupId': cls.lesson_group_id}
        cls.get_result(url, data)

    def test_updateRoom(cls):
        # 拼接请求地址
        url = cls.base_url + cls.updateRoom_uri
        data = {'course_id': cls.course_id, 'course_period_id': cls.course_period_id, 'lesson_id': cls.lesson_id,
                'user_id': cls.user_id, 'groupId': cls.class_group_id, 'type': 'enter'}
        cls.get_result(url, data)

    def test_queryIsCanSpeak(cls):
        # 拼接请求地址
        url = cls.base_url + cls.queryIsCanSpeak_uri
        data = {'nice_user_classroom_status.user_id': cls.user_id,
                'nice_user_classroom_status.course_lesson_id': cls.lesson_id,
                'nice_user_classroom_status.course_period_id': cls.course_period_id}
        cls.get_result(url, data)

    def test_getClearBeforeMsg(cls):
        # 拼接请求地址
        url = cls.base_url + cls.getClearBeforeMsg_uri
        data = {'sysType': 'classroom.point', 'sysCurrencyId': cls.sysCurrencyId, 'groupId': cls.lesson_group_id}
        cls.get_result(url, data)

    def test_onlineNum(cls):
        # 拼接请求地址
        url = cls.base_url + cls.onlineNum_uri
        data = {'class_id': cls.class_id}
        cls.get_result(url, data)

    def test_heartBeat(cls):
        # 拼接请求地址
        url = cls.base_url + cls.heartBeat_uri
        data = {'course_id': cls.course_id, 'course_period_id': cls.course_period_id,
                'lesson_id': cls.lesson_id, 'user_id': cls.user_id,
                'class_id': cls.class_id, 'group_id': cls.class_group_id}
        cls.get_result(url, data)
