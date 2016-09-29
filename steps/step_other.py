# -*- coding: UTF-8 -*-
from behave import then, when

from actions.phone import Phone
from actions.qplay import Qplay
from utils.utils import Utils


@then(u'< 验证Qplay连接成功')
def step_impl(context):
    Phone().check_device_conn_phone()

@then(u'< 验证Qplay手机歌曲是否一致')
def step_impl(context):
    #获取入参
    param = context.table[0]['chk_name']
    if str(param).startswith('o_'):
        chk_name = Utils().get_context_map(param)
    else:
        chk_name = param

    Phone().check_is_play_specil_music(chk_name)

@when(u'< 选择Qplay歌曲')
def step_impl(context):
    #获取出参
    o_name = context.table[0]['o_result']
    name = Qplay().click_qplay_local_name_random()
    # 保存到上下文变量
    Utils().set_context_map(o_name, name)

@then(u'< 验证Qplay歌曲是否一致')
def step_impl(context):
    # 获取入参
    param = context.table[0]['chk_name']
    if str(param).startswith('o_'):
        chk_name = Utils().get_context_map(param)
    else:
        chk_name = param

    name = Qplay().get_qplay_play_name()
    if not name == chk_name:
        Utils().raise_Exception_info('Qplay播放音乐名称不一致，期望值为《' + chk_name + '》，实际值为《' + name + '》')
@when(u'< 手机退出车机模式')
def step_impl(context):
    Phone().click_exit_qplay()
@then(u'< 验证当前为Qplay初始界面')
def step_impl(context):
    Qplay().check_qplay_init()


