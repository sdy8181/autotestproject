# -*- coding: UTF-8 -*-
from behave import when, then

from elements.launcher import Launcher
from elements.phone import Phone
from utils.helpTools import ht
from utils.uiTools import uit

@when(u'< 打开音乐应用')
def step_impl(context):
    Launcher().click_audio_ele()

@when(u'< 打开收音机应用')
def step_impl(context):
    Launcher().click_radio_ele()

@when(u'< 打开九宫格界面')
def step_impl(context):
    Launcher().click_menu_ele()
@when(u'< 打开其他菜单')
def step_impl(context):
    Launcher().click_others_ele()
@when(u'< 打开Qplay')
def step_impl(context):
    Launcher().click_qplay_ele()
    Phone().click_conn_ele()
@when(u'< 打开导航')
def step_impl(context):
    Launcher().click_navi_ele()
@when(u'< 打开视频应用')
def step_impl(context):
    Launcher().click_video_ele()
@then(u'< 验证主界面元素')
def step_impl(context):
    # 验证时间
    time_text = Launcher().get_clock_txt()
    if ':' not in time_text:
        uit.raise_Exception_info('主界面时间展示错误')

    # 验证提示语
    tip_txt = Launcher().get_tip_txt()
    if '语音助理' not in tip_txt:
        uit.raise_Exception_info('主界面语音提示语不存在')
