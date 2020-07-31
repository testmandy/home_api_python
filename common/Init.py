# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:51
# @Author  : mandy
import pytest

import conftest
from common.request import Request
from util.read_ini import ReadIni


class TestInit(object):
    def setup_class(cls) -> None:
        print(r'--------------------Before Class--------------------')
        cls.config = ReadIni()
        cls.username = cls.config.get_value('username', 'data')
        cls.password = cls.config.get_value('password', 'data')
        cls.user_id = cls.config.get_value('user_id', 'data')
        cls.course_id = cls.config.get_value('course_id', 'data')
        cls.lesson_id = cls.config.get_value('lesson_id', 'data')
        cls.course_period_id = cls.config.get_value('course_period_id', 'data')
        cls.class_group_id = cls.config.get_value('class_group_id', 'data')
        cls.lesson_group_id = cls.config.get_value('lesson_group_id', 'data')
        cls.class_id = cls.config.get_value('class_id', 'data')
        cls.sysCurrencyId = cls.config.get_value('sysCurrencyId', 'data')
        cls.goods_id = cls.config.get_value('goods_id', 'data')
        cls.grade = cls.config.get_value('grade', 'data')
        cls.tutor_id = cls.config.get_value('tutor_id', 'data')  # name=0716测试辅导数据
        cls.teacher_id = cls.config.get_value('teacher_id', 'data')  # name=619站立直播老师

        cls.base_url = cls.config.get_value('base_url')
        cls.schoolweb_url = cls.config.get_value('schoolweb_url')
        cls.login_uri = cls.config.get_value('padLogin')
        cls.queryCourseList_uri = cls.config.get_value('queryCourseList')
        cls.queryList_uri = cls.config.get_value('queryList')
        cls.getSudentByName_uri = cls.config.get_value('getSudentByName')
        cls.awardCoin_uri = cls.config.get_value('awardCoin')
        cls.queryStudentAnalysis_uri = cls.config.get_value('queryStudentAnalysis')
        cls.queryStudentList_uri = cls.config.get_value('queryStudentList')
        cls.getStudentInfo_uri = cls.config.get_value('getStudentInfo')
        cls.getDownLoadUrl_uri = cls.config.get_value('getDownLoadUrl')
        cls.qryCourseBanner_uri = cls.config.get_value('qryCourseBanner')
        cls.queryGoodsList_uri = cls.config.get_value('queryGoodsList')
        cls.queryCourseDetail_uri = cls.config.get_value('queryCourseDetail')
        cls.getCourseIsBuy_uri = cls.config.get_value('getCourseIsBuy')
        cls.queryRecommendGoods_uri = cls.config.get_value('queryRecommendGoods')
        cls.cascadeQuery_uri = cls.config.get_value('cascadeQuery')
        cls.studentCourseTask_uri = cls.config.get_value('studentCourseTask')
        cls.queryUserAllCourse_uri = cls.config.get_value('queryUserAllCourse')
        cls.queryLessonTaskByCourseId_uri = cls.config.get_value('queryLessonTaskByCourseId')
        cls.courseCalendar_uri = cls.config.get_value('courseCalendar')
        cls.inputSource_uri = cls.config.get_value('inputSource')
        cls.table_queryList_uri = cls.config.get_value('table_queryList')
        cls.getActivityCouponResource_uri = cls.config.get_value('getActivityCouponResource')
        cls.getMyUsableCouponList_uri = cls.config.get_value('getMyUsableCouponList')
        cls.getCurrentAndOutdoorQuestions_uri = cls.config.get_value('getCurrentAndOutdoorQuestions')

        cls.qryLiveInfo_uri = cls.config.get_value('qryLiveInfo', 'live')
        cls.getCoin_uri = cls.config.get_value('getCoin', 'live')
        cls.getSystemMsg_uri = cls.config.get_value('getSystemMsg', 'live')
        cls.updateRoom_uri = cls.config.get_value('updateRoom', 'live')
        cls.queryIsCanSpeak_uri = cls.config.get_value('queryIsCanSpeak', 'live')
        cls.getClearBeforeMsg_uri = cls.config.get_value('getClearBeforeMsg', 'live')
        cls.onlineNum_uri = cls.config.get_value('onlineNum', 'live')
        cls.heartBeat_uri = cls.config.get_value('heartBeat', 'live')

        cls.req = Request()
        cls.headers = {'Content-Type': 'application/json;charset=UTF-8', 'token': cls.config.get_value('token', 'data')}

    def teardown_class(cls) -> None:
        print(r'--------------------After Class--------------------')
        # cls.op.close()





