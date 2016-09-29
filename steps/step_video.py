# -*- coding: UTF-8 -*-
import random
import time
from behave import when, then

from actions.video import Video
from support.global_vars import d
from utils.utils import Utils


@when(u'< 打开爱奇艺顶部菜单')
def step_impl(context):  # 新加步骤
    # 获取左侧菜单
    left_menu = Video().get_aqy_left_menu_frame()
    if left_menu.wait.exists():
        x = left_menu.info['bounds']['right']
        y = left_menu.info['bounds']['bottom']
        d.swipe(x, int(y) / 2, 0, int(y) / 2, 15)

    top_menu = Video().get_aqy_home_top_menu()
    if top_menu.wait.exists():
        top_menu.click.wait()
    else:
        Utils().raise_Exception_info('爱奇艺顶部菜单不存在')


@when(u'< 打开我的视频')
def step_impl(context):
    mine = Video().get_aqy_menu_mine()
    if mine.wait.exists():
        mine.click()
    else:
        Utils().raise_Exception_info('我的视频控件不存在')


@when(u'< 打开本地视频')
def step_impl(context):  # 新加步骤
    local = Video().get_aqy_menu_mine_local_video()
    if local.wait.exists():
        local.click.wait()
    else:
        Utils().raise_Exception_info('本地视频控件不存在')


@when(u'< 打开播放记录')
def step_impl(context):  # 新加步骤
    his = Video().get_aqy_menu_mine_his()
    if his.wait.exists():
        his.click.wait()
    else:
        Utils().raise_Exception_info('播放记录控件不存在')


@when(u'< 打开我的收藏')
def step_impl(context):  # 新加步骤
    fav = Video().get_aqy_menu_mine_fav()
    if fav.wait.exists():
        fav.click.wait()
    else:
        Utils().raise_Exception_info('我的收藏控件不存在')


@when(u'< 播放本地视频')
def step_impl(context):
    exists_flag = False
    # 获取视频名称
    video_name = context.table[0]['video_name']
    # 查找并播放本地视频
    local_video = Video().get_aqy_mine_local_video_title()
    if local_video.wait.exists():
        for lv in local_video:
            if lv.text == video_name:
                lv.click.wait()
                exists_flag = True
                break
    else:
        Utils().raise_Exception_info('本地视频列表为空')

    if not exists_flag:
        Utils().raise_Exception_info('没有找到指定视频')


@then(u'< 验证视频是否播放')
def step_impl(context):
    # 获取参数
    chk_is_playing = context.table[0]['chk_is_playing']

    # 获取视频广告控件
    adtime = Video().get_aqy_player_top_adtime()

    if adtime.exists:
        adtime.wait.gone(timeout=60000)

    # 获取当前播放时间控件
    oldTime = Video().get_aqy_player_currentTime()
    old_time = ''
    if oldTime.wait.exists():
        old_time = oldTime.text
    else:
        Utils().raise_Exception_info('当前播放时间控件不存在')

    time.sleep(5)

    newTime = Video().get_aqy_player_currentTime()
    new_time = ''
    if newTime.wait.exists():
        new_time = newTime.text
    else:
        Utils().raise_Exception_info('当前播放时间控件不存在')

    if str(new_time == old_time).lower() == str(chk_is_playing).lower():
        Utils().raise_Exception_info('视频播放状态不一致')


@then(u'< 验证视频播放名称一致')
def step_impl(context):
    # 获取参数
    param = context.table[0]['chk_name']
    if param.startswith('o_'):
        chk_video_name = Utils().get_context_map(param)
    else:
        chk_video_name = param

    video_title = Video().get_aqy_playing_title()
    if not video_title.wait.exists():
        Utils().raise_Exception_info('视频名称控件不存在')

    video_name = video_title.text

    if not chk_video_name == video_name:
        Utils().raise_Exception_info('视频文件名称不一致，期望值为《' + chk_video_name + '》，实际值为《' + video_name + '》')


@when(u'< 打开视频搜索')
def step_impl(context):
    # 获取视频搜索控件
    search = Video().get_aqy_search()
    if search.wait.exists():
        search.click.wait()
    else:
        Utils().raise_Exception_info('视频搜索控件不存在')


@when(u'< 输入视频搜索关键字')
def step_impl(context):
    # 获取入参
    key_word = context.table[0]['keyword']
    input_ele = Video().get_aqy_search_input()
    if input_ele.wait.exists():
        input_ele.clear_text()
        input_ele.set_text(Utils().unicode_input(key_word))
    else:
        Utils().raise_Exception_info('视频搜索输入框控件不存在')


@when(u'< 从搜索结果中播放指定视频')
def step_impl(context):
    # 获取入参
    video_name = context.table[0]['video_name']

    list_view = Video().get_aqy_search_result_list()
    title_ele = Video().get_aqy_search_result_title()

    if title_ele.wait.exists(timeout=Utils().LONG_TIME_OUT):
        if list_view.scroll.vert.to(text=video_name):
            for t in title_ele:
                if t.text.strip() == video_name:
                    t.click.wait()
                    break
        else:
            Utils().raise_Exception_info('搜索视频不存在')
    else:
        Utils().raise_Exception_info('视频搜索结果为空')


@when(u'< 清空视频搜索记录并验证')
def step_impl(context):  # 修改 清空视频搜索框并验证
    # 获取清除控件
    clear_ele = Video().get_aqy_search_his_clear()
    if clear_ele.wait.exists():
        clear_ele.click.wait()
    else:
        Utils().raise_Exception_info('清除搜索记录控件不存在')

    # 验证是否清除完成
    clear_ele = Video().get_aqy_search_his_clear()
    if clear_ele.exists:
        Utils().raise_Exception_info('清空搜索记录失败')


@when(u'< 从播放记录中播放指定视频')
def step_impl(context):
    # 获取播放视频名称
    video_name = context.table[0]['video_name']
    # 从列表中查找指定视频并播放
    ele = Video().get_aqy_mine_his_video_title()
    if ele.wait.exists():
        # if ele.scroll.vert.to(text=video_name):
        for e in ele:
            if e.text.strip() == video_name:
                d(text=video_name).click.wait()
                break
        else:
            Utils().raise_Exception_info('没有查找到指定《' + video_name + '》视频')
    else:
        Utils().raise_Exception_info('播放记录为空')

@when(u'< 获取最新播放记录视频')
def step_impl(context):
    # 获取出参
    param = context.table[0]['o_result']

    # 获取第一个视频名称
    ele = Video().get_aqy_mine_his_video_title()
    if ele.wait.exists():
        Utils().set_context_map(param, ele[0].text.strip())
    else:
        Utils().raise_Exception_info('播放记录为空')


@when(u'< 搜索热门搜索视频')
def step_impl(context):
    # 获取接受返回值参数
    param = context.table[0]['o_result']
    video_name = Video().get_aqy_search_hot_title()
    if video_name.wait.exists():
        idx = random.randint(0, len(video_name) - 1)
        Utils().set_context_map(param, video_name[idx].text)
        video_name[idx].click.wait()
    else:
        Utils().raise_Exception_info('热门搜索记录为空')


@when(u'< 获取最新搜索记录')
def step_impl(context):
    # 获取接受返回值的参数
    param = context.table[0]['o_result']
    video_name = Video().get_aqy_search_his_title()
    if video_name.wait.exists():
        Utils().set_context_map(param, video_name[0].text)
    else:
        Utils().raise_Exception_info('搜索记录为空')


@when(u'< 播放爱奇艺推荐视频')
def step_impl(context):  # 修改
    # 获取接受出参的参数
    param = context.table[0]['o_result']

    ele = Video().get_aqy_recommend_right_up_title()
    if ele.wait.exists():
        Utils().set_context_map(param, ele.text)
        ele.click.wait()
    else:
        Utils().raise_Exception_info('爱奇艺推荐视频不存在')


@then(u'< 验证视频搜索结果')
def step_impl(context):
    flag = False
    # 获取参数
    param = context.table[0]['search_word']
    ele = Video().get_aqy_search_result_title()
    for e in ele:
        if param in e.text.strip():
            flag = True
            break

    if not flag:
        Utils().raise_Exception_info('搜索视频没有期望的结果')


@when(u'< 收藏或取消收藏视频')
def step_impl(context):
    #获取收藏控件
    fav_ele = Video().get_aqy_player_fav()
    if fav_ele.wait.exists():
        fav_ele.click()
    else:
        Utils().raise_Exception_info('视频收藏控件不存在')


@then(u'< 验证视频是否被收藏')
def step_impl(context):
    flag = False
    # 获取入参 视频名称，是否收藏
    video_name = context.table[0]['chk_video_name']
    is_faved = context.table[0]['is_faved']
    if video_name.startswith('o_'):
        video_name = Utils().get_context_map(video_name)

    # 获取我的收藏视频title
    video_title = Video().get_aqy_mine_fav_video_title()
    if video_title.wait.exists():
        for vt in video_title:
            if video_name == vt.text.strip():
                flag = True
                break
    else:
        Utils().raise_Exception_info('我的收藏记录为空')

    if not str(flag).lower() == str(is_faved).lower():
        Utils().raise_Exception_info('视频是否收藏验证失败')

@when(u'< 暂停或者播放视频')
def step_impl(context):
    # 获取暂停或者播放控件
    pause_btn = Video().get_aqy_pause_btn()

    if pause_btn.wait.exists():
        pause_btn.click()
    else:
        Utils().raise_Exception_info('播放或者暂停控件不存在')
