# -*- coding: UTF-8 -*-
import time
from behave import when, then

from actions.launcher import Launcher
from actions.radio import Radio
from utils.utils import Utils


@when(u'< 打开FM_AM选择界面')
def step_impl(context):
    # 点击fm标签页
    Radio().click_radio_selector_ele()

@when(u'< 播放指定FM节目')
def step_impl(context):
    fm_no = context.table[0]['fm_no']
    Radio().click_radio_selector_fm_ele()
    Radio().click_radio_selector_fm_by_no_ele(fm_no)

@then(u'< 验证播放的FM编号一致')
def step_impl(context):
    # 获取参数
    param = context.table[0]['chk_fm_no']
    if str(param).startswith('o_'):
        chk_fm_no = Utils().get_context_map(param)
    else:
        chk_fm_no = param

    fm_no = Radio().get_radio_no_playing_txt()
    if fm_no != chk_fm_no:
        Utils().raise_Exception_info('收音机编号不一致，期望值为《' + chk_fm_no + '》，实际值为《' + fm_no + '》')

@then(u'< 验证播放的FM编号不一致')
def step_impl(context):
    # 获取参数
    param = context.table[0]['chk_fm_no']
    if str(param).startswith('o_'):
        chk_fm_no = Utils().get_context_map(param)
    else:
        chk_fm_no = param

    fm_no = Radio().get_radio_no_playing_txt()
    if fm_no == chk_fm_no:
        Utils().raise_Exception_info('收音机编号不一致，期望值不应该为《' + chk_fm_no + '》，实际值为《' + fm_no + '》')

@when(u'< 切换上一台')
def step_impl(context):
    Radio().click_radio_prev_ele()

@when(u'< 切换下一台')
def step_impl(context):
    Radio().click_radio_next_ele()
@when(u'< 预览电台并随机收听')
def step_impl(context):
#     获取出参
    param = context.table[0]['o_result']
    # 点击预览电台控件
    Radio().click_radio_preview_ele()
    #判断当前是否在刷新
    # fm_no = Radio().get_radio_no_playing_txt()
    #等待8s
    time.sleep(8)
    # fm_no1 = Radio().get_radio_no_playing_txt()
    # if fm_no == fm_no1:
    #     Utils().raise_Exception_info('预览电台失败，电台没有在预览')
    #点击预览控件停止预览
    Radio().click_radio_preview_ele()
    fm_no2 = Radio().get_radio_no_playing_txt()
    #存放选中电台
    Utils().set_context_map(param, fm_no2)

@when(u'< 收藏或取消收藏电台')
def step_impl(context):
    Radio().click_radio_fav_or_cancel_ele()
@then(u'< 验证FM是否被收藏')
def step_impl(context):
    # 获取第一个参数
    param = context.table[0]['chk_fm_no']
    if str(param).startswith('o_'):
        chk_fm_no = Utils().get_context_map(param)
    else:
        chk_fm_no = param
    # 获取第二个参数
    chk_is_faved = context.table[0]['chk_is_faved']
    # 切换到fm_tab页
    Radio().click_radio_selector_fm_ele()
    #查询是否被收藏
    is_faved = Radio().get_radio_selector_fm_is_faved_by_no(chk_fm_no)

    if not str(is_faved).lower().__eq__(str(chk_is_faved).lower()):
        Utils().raise_Exception_info('验证指定FM《' + chk_fm_no + '》 是否被收藏失败')

@when(u'< 播放已经收藏的电台')
def step_impl(context):

    Radio().click_radio_selector_fm_faved()
@then(u'< 验证电台是否播放')
def step_impl(context):
    # 获取参数
    chk_is_playing = context.table[0]['chk_is_playing']
    # 获取当前播放状态
    time.sleep(2)
    is_playing = Radio().get_radio_is_playing()
    if not str(chk_is_playing).lower().__eq__(str(is_playing).lower()):
        Utils().raise_Exception_info('电台播放状态不一致')

@when(u'< 打开搜索界面')
def step_impl(context):
    Radio().click_radio_search_ele()

@when(u'< 输入电台搜索关键字')
def step_impl(context):
    # 获取参数信息
    key_word = context.table[0]['key_word']
    Radio().input_radio_search_keyword_ele(key_word)

@then(u'< 验证当前为收音机主界面')
def step_impl(context):
    Radio().chk_radio_is_home_page()
@when(u'< 清空电台搜索框')
def step_impl(context):
    Radio().click_radio_search_clear_ele()
@then(u'< 验证电台搜索框内容')
def step_impl(context):
    # 获取参数内容
    chk_key_word = context.table[0]['chk_key_word']
    # 获取当前输入框内容
    key_word = Radio().get_radio_search_keyword_txt()
#     校验是否相同
    if chk_key_word != key_word:
        Utils().raise_Exception_info('输入框内容不一致，期望值为《' + chk_key_word + '》, 实际值为《' + key_word + '》')
@when(u'< 取消电台搜索')
def step_impl(context):
    Radio().click_radio_search_cancel_ele()

@when(u'< 随机播放搜索电台')
def step_impl(context):
    # 获取参数
    param = context.table[0]['o_result']
    fm_no = Radio().click_radio_search_list_title_random_ele()
    if str(fm_no).startswith('FM') or str(fm_no).startswith('AM'):
        Utils().set_context_map(param, fm_no[2:])
    else:
        Utils().set_context_map(param, fm_no)
@when(u'< 打开蜻蜓FM')
def step_impl(context):
    Radio().click_radio_qt_ele()
@when(u'< 随机播放蜻蜓FM栏目')
def step_impl(context):
    #获取参数信息
    param = context.table[0]['o_result']
    # 点击精选电台
    Radio().click_radio_qt_category_ele()
    #点击栏目
    title = Radio().click_radio_qt_category_title_ele()
    # 保存到上下文变量中
    Utils().set_context_map(param, title)
@when(u'< 随机播放蜻蜓FM节目')
def step_impl(context):
    #获取参数信息
    param = context.table[0]['o_result']

    name = Radio().click_radio_qt_category_list_name_random_ele()
    # 保存到上下文变量中
    Utils().set_context_map(param, name)
@then(u'< 验证播放蜻蜓FM标题一致')
def step_impl(context):
    #获取参数
    param = context.table[0]['chk_qt_title']
    if str(param).startswith('o_'):
        chk_qt_title = Utils().get_context_map(param)
    else:
        chk_qt_title = param
    # 获取当前的标题
    qt_title = Radio().get_radio_qt_title_playing_txt()

    if chk_qt_title != qt_title:
        Utils().raise_Exception_info('正在播放的蜻蜓FM栏目标题不一致，期望值为《' + chk_qt_title + '》，实际值为《' + qt_title + '》')
@then(u'< 验证播放FM节目一致')
def step_impl(context):
    #获取参数
    param = context.table[0]['chk_name']
    if str(param).startswith('o_'):
        chk_name = Utils().get_context_map(param)
    else:
        chk_name = param
    #获取当前播放的节目 名称
    name = Radio().get_radio_name_playing_txt()

    if chk_name != name:
        Utils().raise_Exception_info('正在播放的FM节目名称不一致，期望值为《' + chk_name + '》，实际值为《' + name + '》')

@then(u'< 验证播放FM节目不一致')
def step_impl(context):
    # 获取参数
    param = context.table[0]['chk_name']
    if str(param).startswith('o_'):
        chk_name = Utils().get_context_map(param)
    else:
        chk_name = param
    # 获取当前播放的节目 名称
        name = Radio().get_radio_name_playing_txt()
    if chk_name == name:
        Utils().raise_Exception_info('正在播放的FM节目名称不一致，期望值不应该为《' + chk_name + '》，实际值为《' + name + '》')
@then(u'< 验证最近收听含有节目')
def step_impl(context):
    #获取参数
    param = context.table[0]['chk_qt_name']
    if str(param).startswith('o_'):
        chk_qt_name = Utils().get_context_map(param)
    else:
        chk_qt_name = param
    #获取最近收听数据
    ele = Radio().get_radio_qt_latest_name_ele()
    #校验第一个应该为最近收听内容
    size = len(ele)
    if size > 0:
        qt_name = ele[0].text.strip()
        if chk_qt_name != qt_name:
            Utils().raise_Exception_info('验证最近收听记录失败，期望值为《' + chk_qt_name + '》，实际值为《' + qt_name + '》')
        else:
            Radio().hide_radio_qt_drawer_ele()
    else:
        Utils().raise_Exception_info('最近收听记录为空')
@when(u'< 收藏或取消蜻蜓FM电台')
def step_impl(context):
    Radio().click_radio_qt_fav_ele()
@then(u'< 验证蜻蜓FM是否被收藏')
def step_impl(context):
    #获取参数--蜻蜓FM栏目名称
    param1 = context.table[0]['chk_qt_title']
    param2 = context.table[0]['chk_is_faved']
    if str(param1).startswith('o_'):
        chk_qt_title = Utils().get_context_map(param1)
    else:
        chk_qt_title = param1
    #获取是否被收藏
    if str(param2).startswith('o_'):
        chk_is_faved = Utils().get_context_map(param2)
    else:
        chk_is_faved = param2
    # 获取收藏记录
    Radio().click_radio_qt_collected_ele()
    is_faved = Radio().get_radio_qt_collected_title_is_exists(chk_qt_title)
    # 验证是否被收藏
    if not str(is_faved).lower().__eq__(str(chk_is_faved).lower()):
        Utils().raise_Exception_info('验证蜻蜓FM是否被收藏失败')
@when(u'< 播放收藏的蜻蜓FM')
def step_impl(context):
    #获取出参
    o_title_faved = context.table[0]['o_result']
    title_faved = Radio().click_radio_qt_collected_title_ele()
    #     存入上下文变量
    Utils().set_context_map(o_title_faved, title_faved)
@when(u'< 播放或暂停FM电台')
def step_impl(context):
    Radio().click_radio_pause_or_play_ele()
@when(u'< 随机播放FM节目')
def step_impl(context):
    #获取参数信息
    param = context.table[0]['o_result']
    Radio().click_radio_selector_fm_ele()

    fm_no = Radio().click_radio_selector_fm_random_ele()
    #存入上下文变量
    Utils().set_context_map(param, fm_no)
@when(u'< 调整收音机微调')
def step_impl(context):
    #获取对象
    Radio().scroll_radio_weitiao_ele()
@when(u'< 点击听歌识曲')
def step_impl(context):
    Radio().click_radio_ide_ele()
@then(u'< 验证听歌识曲正确')
def step_impl(context):
    if not Radio().get_radio_ide_status():
        Utils().raise_Exception_info('听歌识曲验证失败，未识别到歌曲')

@when(u'< 点击听歌识曲并播放')
def step_impl(context):
    # 获取参数
    param = context.table[0]['o_result']

    context.execute_steps('''
    当< 点击听歌识曲
    ''')
    name = Radio().click_radio_ide_audio()
    #保存歌曲名到上下文
    Utils().set_context_map(param, name)

@when(u'< 打开电台节目列表')
def step_impl(context):
    Radio().click_radio_list_ele()

@when(u'< 随机播放网络回听节目')
def step_impl(context):
    #获取参数
    param = context.table[0]['o_result']
    value = Radio().click_radio_list_his_name_random_ele()
    # 保存到上下文变量
    Utils().set_context_map(param, value)

