# -*- coding: UTF-8 -*-
import os
import time

from behave import when, then

from actions.common import Common
from support.global_vars import d
from utils.utils import Utils


@when(u'< 延时')
def step_impl(context):
    # 获取延时时间
    sec = context.table[0]['sleep_time']
    time.sleep(int(sec))
@then(u'< 验证放音通道一致')
def step_impl(context):
    chk_tinymix = context.table[0]['chk_tinymix']
    # 获取当前的放音通道
    cur_tinymix = Utils().get_cur_tinymix()
    if chk_tinymix != cur_tinymix:
        Utils().raise_Exception_info('放音通道不一致，期望值为《' + chk_tinymix + '》，实际值为《' + cur_tinymix + '》')
@when(u'< 回到系统主界面')
def step_impl(context):
    Common().back_to_launcher()
@when(u'< 播放音频文件')
def step_impl(context):
    # 获取参数
    voiceFile = context.table[0]['voice_file']
    Utils().play_voice(voiceFile)
    time.sleep(4)
@when(u'< ivoka唤醒应用')
def step_impl(context):
    # 获取需要播放的音频文件
    voice_name = context.table[0]['voice_name']
    Common().ivoka_start_app(voice_name)
@when(u'< 获取MEDIA音量')
def step_impl(context):
    #获取出参
    param = context.table[0]['o_result']
    volume_value = Common().get_media_volume()
    #保存在上下文变量中
    Utils().set_context_map(param, volume_value)

@then(u'< 验证MEDIA音量一致')
def step_impl(context):
    # 获取入参
    param = context.table[0]['chk_volume']
    if str(param).startswith('o_'):
        chk_volume = Utils().get_context_map(param)
    else:
        chk_volume = param
    # 获取当前的音量
    cur_volume = Common().get_media_volume()
    # 校验是否一致
    if cur_volume != chk_volume:
        Utils().raise_Exception_info('Media音量不一致，期望值为《' + chk_volume + '》，实际值为《' + cur_volume + '》')
@then(u'< 验证当前应用')
def step_impl(context):
    #获取期望应用名称
    chk_app_name = context.table[0]['chk_app_name']
    #获取当前应用名称
    cur_app_name = Common().get_current_package_name()
    # 校验
    if chk_app_name != cur_app_name:
        Utils().raise_Exception_info('期望应用和当前应用不一致，期望应用为《' + chk_app_name + '》，当前应用为《' + cur_app_name + '》')

@when(u'< 拔出U盘')
def step_impl(context):
    Common().controlPoweroff()
@when(u'< 插上U盘')
def step_impl(context):
    Common().controlPoweron()
@then(u'< 验证两个对象值')
def step_impl(context):
    #获取两个对象和一个比较字符
    param1 = context.table[0]['param1']
    param2 = context.table[0]['param2']
    opt = context.table[0]['option']

    if param1.startswith('o_'):
        param1 = Utils().get_context_map(param1)

    if param2.startswith('o_'):
        param2 = Utils().get_context_map(param2)

    if opt == '==':
        flag = param1.lower() == param2.lower()
    elif opt == '!=':
        flag = param1.lower() != param2.lower()
    elif opt == '%':
        flag = param1.lower().__contains__(param2.lower())
    elif opt == ">":
        flag = int(param1.lower()) > int(param2.lower())
    elif opt == "<":
        flag = int(param1.lower()) < int(param2.lower())
    else:
        raise ('暂时不支持改操作符，请联系脚本维护人员')

    if not flag:
        Utils().raise_Exception_info('比较失败《' + param1 + ' ' + opt + ' ' + param2 +  '》')
@then(u'< 验证当前界面包含文本')
def step_impl(context):
    txt = context.table[0]['contains_txt']
    ele = d(textContains = txt)
    if not ele.wait.exists(timeout=Utils().TIME_OUT):
        Utils().raise_Exception_info('文本信息《' + txt + '》没有包含在界面中')

@when(u'< 重启设备')
def step_impl(context):
    device_serial = Utils().get_conf_value('deviceSerial')
    os.popen('adb -s ' + device_serial + ' shell reboot')





