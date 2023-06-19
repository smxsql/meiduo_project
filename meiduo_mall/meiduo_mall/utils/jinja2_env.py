# -*- coding：utf-8 -*-
# @Time   :2023/6/18 21:25
# @Author :sql
# @File   :jinja2_env.py

from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

def jinja2_environment(**options):
    """jinja2的环境变量"""
    # 创建环境对象
    env = Environment(**options)

    # 自定义语法，{{static ('静态文件相对路径')}} {{url('路由命名空间')}}
    env.globals.update(
        {
            'static': staticfiles_storage, #获取静态文件的前缀
            'url': reverse # 反向解析
        })
    return env
