# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 22:15
# @Author  : mandy
import json
import time
import pytest
from common.Init import TestInit


@pytest.mark.run(order=1)
class TestSchool(TestInit):
    def get_result(cls, url, data):
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u'请求结果为：%s' % res)
        cls.compare_msg(res)

    def compare_msg(cls, res):
        json_res = json.loads(res)
        assert json_res['msg'] == ('success' or 'SUCCESS')
        if json_res['msg'] == ('success' or 'SUCCESS'):
            print(u'------------测试通过(^_^)------------')
        else:
            print(u'------------测试未通过/(ㄒoㄒ)/~~------------')

    def extract_data(cls, url, data):
        json_data = json.dumps(data)
        res = cls.req.main('post', url, json_data, cls.headers)
        print(u'请求结果为：%s' % res)
        return json.loads(res)

    @pytest.mark.run(order=1)
    def test_login_success(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.login_uri
        data = {'username': cls.username, 'password': cls.password}
        json_res = cls.extract_data(url, data)
        sys_user_id = json_res['data']['sys_user_id']
        cls.config.set_ini('data', 'user_id', str(sys_user_id))
        token = json_res['data']['token']
        cls.config.set_ini('data', 'token', str(token))

    @pytest.mark.run(order=2)
    def test_getStudentInfo(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getStudentInfo_uri
        data = {'nice_user_base.user_Id': cls.user_id}
        json_res = cls.extract_data(url, data)
        list_json = json_res['data']['list'][0]
        tutor_id = list_json['tutor_id']
        cls.config.set_ini('data', 'tutor_id', str(tutor_id))
        grade = list_json['grade']
        cls.config.set_ini('data', 'grade', str(grade))

    @pytest.mark.run(order=3)
    def test_studentCourseTask(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.studentCourseTask_uri
        data = {'nice_course.user_id': cls.user_id}
        json_res = cls.extract_data(url, data)
        list_json = json_res['data']['list'][0]
        course_id = list_json['course_id']
        cls.config.set_ini('data', 'course_id', str(course_id))
        course_period_id = list_json['course_period_id']
        cls.config.set_ini('data', 'course_period_id', str(course_period_id))
        lesson_id = list_json['lesson_id']
        cls.config.set_ini('data', 'lesson_id', str(lesson_id))
        teacher = list_json['teacher']
        cls.config.set_ini('data', 'teacher_id', str(teacher))

    def test_getDownLoadUrl(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getDownLoadUrl_uri
        data = {'type': 'c'}
        cls.get_result(url, data)

    def test_qryCourseBanner(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.qryCourseBanner_uri
        data = {'nice_course_banner.appid': '562'}
        cls.get_result(url, data)

    def test_queryGoodsList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryGoodsList_uri
        data = {'subject': '', 'version': '', 'grade': cls.grade, 'user_id': cls.user_id, 'order_name': '暑假'}
        cls.get_result(url, data)

    def test_queryCourseDetail(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryCourseDetail_uri
        data = {'id': cls.course_id, 'goods_id': cls.goods_id}
        cls.get_result(url, data)

    def test_getCourseIsBuy(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getCourseIsBuy_uri
        data = {'nice_order.goods_id': cls.goods_id, 'nice_order.user_id': cls.user_id,
                'nice_course_period_student.course_id': cls.course_id}
        cls.get_result(url, data)

    def test_queryRecommendGoods(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryRecommendGoods_uri
        data = {'grade': cls.grade}
        cls.get_result(url, data)


    def test_queryUserAllCourse(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryUserAllCourse_uri
        data = {'student_id': cls.user_id, 'is_close': '', 'subject': '', 'type': '', 'name': ''}
        cls.get_result(url, data)

    def test_queryLessonTaskByCourseId(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.queryLessonTaskByCourseId_uri
        data = {'nice_student_course_lesson_learn.user_id': cls.user_id,
                'nice_student_course_lesson_learn.course_id': cls.course_id,
                'nice_student_course_lesson_learn.course_period_id': cls.course_period_id}
        cls.get_result(url, data)

    def test_courseCalendar(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.courseCalendar_uri
        data = {'nice_course.user_id': cls.user_id}
        cls.get_result(url, data)

    def test_inputSource(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.inputSource_uri
        data = {'username': '15200000020', 'password': 'nice123456'}
        cls.get_result(url, data)

    def test_table_queryList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.table_queryList_uri
        data = {'table_name': 'nice_region'}
        cls.get_result(url, data)

    def test_getActivityCouponResource(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getActivityCouponResource_uri
        data = {}
        cls.get_result(url, data)

    def test_getMyUsableCouponList(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getMyUsableCouponList_uri
        data = {'user_id': cls.user_id}
        cls.get_result(url, data)

    def test_getCurrentAndOutdoorQuestions(cls):
        # 拼接请求地址
        url = cls.schoolweb_url + cls.getCurrentAndOutdoorQuestions_uri
        data = {'course_lesson_id': cls.lesson_id, 'course_period_id': cls.course_period_id}
        cls.get_result(url, data)

