# -*- coding: UTF-8 -*-
from behave import when, then

from actions.phone import Phone


@when(u'< 手机拨打号码')
def step_impl(context):
    # 获取电话号码
    phone_no = context.table[0]['phone_no']
    Phone().dail_phone_no(phone_no)
@when(u'< 手机挂断电话')
def step_impl(context):
    Phone().end_phone_call()

@when(u'< 手机播放QQ音乐')
def step_impl(context):
    Phone().play_qq_music()