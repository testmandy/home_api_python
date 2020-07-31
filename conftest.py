# coding=utf-8
# @Time    : 2019/9/3 11:05
# @Author  : Mandy
import os
import logging
import logging.config


project_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(project_dir, 'config')
userconfig_dir = os.path.join(config_dir, 'userconfig.yaml')
env_dir = os.path.join(config_dir, 'env.ini')
data_dir = os.path.join(config_dir, 'data.json')
excel_dir = os.path.join(config_dir, 'testcases.xls')


def get_logger():
    CONF_LOG = "../config/logging.ini"
    logging.config.fileConfig(CONF_LOG)
    logger = logging.getLogger()


