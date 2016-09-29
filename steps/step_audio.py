# -*- coding: UTF-8 -*-
import random
import time
from behave import then
from behave import when

from actions.audio import Audio
from utils.utils import Utils


@when(u'< 打开我的音乐库')
def step_impl(context):
    Audio().click_audio_mine_ele()

@when(u'< 播放本地指定音乐')
def step_impl(context):
    text = context.table[0]['music_name']
    Audio().click_audio_mine_all_ele()
    Audio().click_audio_mine_all_by_name(text)

@then(u'< 验证音乐名称不一致')
def step_impl(context):
    # 获取入参数据
    param = context.table[0]['chk_music_name']
    if str(param).startswith('o_'):
        chk_music_name = Utils().get_context_map(param)
    else:
        chk_music_name = param
    # 获取当前音乐名称
    cur_music_name = Audio().get_audio_name_playing_txt()
    print("期望音乐名称为: " + chk_music_name)
    print("实际音乐名称为: " + cur_music_name)
    # 校验
    if cur_music_name == chk_music_name:
        Utils().raise_Exception_info('音乐验证失败，期望值不应该是《' + chk_music_name + "》，实际值是《 " + cur_music_name + "》" )
@then(u'< 验证音乐名称一致')
def step_impl(context):
    # 获取入参数据
    param = context.table[0]['chk_music_name']

    if str(param).startswith('o_'):
        chk_music_name = Utils().get_context_map(param)
    else:
        chk_music_name = param
    # 获取当前音乐名称
    cur_music_name = Audio().get_audio_name_playing_txt()
    print("期望音乐名称为: " + chk_music_name)
    print("实际音乐名称为: " + cur_music_name)
    # 校验包含
    if not str(cur_music_name).__contains__(chk_music_name):
        Utils().raise_Exception_info('音乐验证失败，期望值是《' + chk_music_name + "》，实际值是《" + cur_music_name + "》" )

@then(u'< 验证歌手名字一致')
def step_impl(context):
    """
    :param context: o_开头的 先获取歌曲名称，再根据歌曲名称获取歌手名字
    :return:
    """
    #     获取入参数据
    param = context.table[0]['chk_artist']
    # 判断入参是否为上一个步骤的出参
    if str(param).startswith('o_'):
        chk_artist = Utils().get_context_map(param)
    else:
        chk_artist = param
    # 获取当前歌手名字
    cur_artist = Audio().get_audio_artist_playing_txt()
    print("期望歌手为: " + chk_artist)
    print("实际歌手为: " + cur_artist)
    # 校验
    if not str(cur_artist).__contains__(chk_artist):
        Utils().raise_Exception_info('歌手验证失败，期望值是《' + chk_artist + "》，实际值是《 " + cur_artist + "》" )

@then(u'< 验证音乐是否播放')
def step_impl(context):
    # 获取入参
    flag = context.table[0]['is_playing']
    #获取当前歌曲总时间
    all_time = Audio().get_audio_alltime_txt()
    loop_cnt = 0
    while '00:00'.__eq__(all_time):
        time.sleep(10)
        all_time = Audio().get_audio_alltime_txt()
        loop_cnt += 1

        if loop_cnt > 3:
            Utils().raise_Exception_info('歌曲播放总时间为00：00')
            break
    # 获取当前的showtime
    start_show_time = Audio().get_audio_showtime_txt()
    cnt = 0
    # 处理缓冲
    while '00:00'.__eq__(start_show_time):
        time.sleep(10)
        start_show_time = Audio().get_audio_showtime_txt()
        cnt += 1
        # 限制次数 15s后抛异常
        if(3 == cnt):
            Utils().raise_Exception_info('网络问题，音乐缓冲卡住')
            break

    # 暂停5s
    time.sleep(3)
    # 获取当前的showtime
    end_show_time = Audio().get_audio_showtime_txt()
    # 校验
    if flag == 'true':
        if start_show_time == end_show_time:
            Utils().raise_Exception_info('音乐没有在播放或者播放过程中卡住')
    else:
        if start_show_time != end_show_time:
            Utils().raise_Exception_info('音乐没有在暂停')
@when(u'< 打开音乐搜索')
def step_impl(context):
    Audio().click_audio_search_ele()

@when(u'< 根据关键字搜索网络音乐')
def step_impl(context):
    key_word = context.table[0]['key_word']
    Audio().input_audio_search_keyword_ele(key_word)

@when(u'< 根据歌手播放搜索结果')
def step_impl(context):
    artist = context.table[0]['artist']
    Audio().click_audio_search_result_by_artist(artist)

@when(u'< 根据音乐播放搜索结果')
def step_impl(context):
    music_name = context.table[0]['music_name']
    Audio().click_audio_search_result_by_name(music_name)
@when(u'< 切换上一首音乐')
def step_impl(context):
    Audio().click_prev_ele()
@when(u'< 切换下一首音乐')
def step_impl(context):
    Audio().click_next_ele()
@then(u'< 验证音乐搜索框内容')
def step_impl(context):
    chk_key_word = context.table[0]['chk_key_word']
    keyword_txt = Audio().get_audio_search_keyword_txt()
    if chk_key_word != keyword_txt:
        Utils().raise_Exception_info('搜索框内容不一致，期望值为《' + chk_key_word + '》，实际值为《' + keyword_txt + '》')
@when(u'< 取消音乐搜索')
def step_impl(context):
    Audio().click_audio_search_cancel_ele()
@then(u'< 验证当前为音乐主界面')
def step_impl(context):
    Audio().chk_audio_is_home_page()
@when(u'< 清空音乐搜索框')
def step_impl(context):
    Audio().click_audio_search_clear_ele()

@when(u'< 打开今日歌单')
def step_impl(context):
    Audio().click_audio_smart_ele()
@when(u'< 随机播放今日歌单')
def step_impl(context):
    param = context.table[0]['o_result']
    name = Audio().click_audio_smart_name_random_ele()
    print("选中的今日歌单的歌曲名字为: " + name)
    # 保存在上下文变量中
    Utils().set_context_map(param, name)

@when(u'< 打开音乐列表')
def step_impl(context):
    Audio().click_audio_list_ele()

@then(u'< 验证听ta的歌是否一致')
def step_impl(context):
    param = context.table[0]['chk_artist']
    if str(param).startswith('o_'):
        chk_artist = Utils().get_context_map(param)
    else:
        chk_artist = param
    # 点击进入听ta的歌界面
    Audio().click_audio_list_ta_ele()
    Audio().chk_audio_list_ta_listview_by_artist(chk_artist)
    i = 0
    # 滚动两屏校验
    while i < 2:
        Audio().scroll_audio_list_ta_listview_forward()
        Audio().chk_audio_list_ta_listview_by_artist(chk_artist)
        i += 1
@when(u'< 打开酷我音乐')
def step_impl(context):
    Audio().click_audio_kuwo_ele()

@when(u'< 随机播放网络音乐')
def step_impl(context):
    Audio().click_audio_kuwo_name_random_ele()

@then(u'< 验证U盘音乐数量')
def step_impl(context):
    chk_usb_cnt = context.table[0]['chk_usb_cnt']
    # 点击我的音乐tab
    Audio().click_audio_mine_my_ele()
    # 获取数量
    usb_cnt = Audio().get_audio_mine_usb_cnt_txt()
    if chk_usb_cnt != usb_cnt:
        Utils().raise_Exception_info('验证U盘音乐数量失败，期望数量:' + chk_usb_cnt + ", 实际数量:" + usb_cnt )
    else:
        Audio().hide_audio_mine_drawer()

@when(u'< 播放U盘音乐')
def step_impl(context):
    # 点击我的音乐
    Audio().click_audio_mine_my_ele()
    # 点击播放USB音乐
    Audio().click_audio_mine_usb_play_ele()

@then(u'< 验证当前为U盘音乐')
def step_impl(context):
    # 获取当前播放的音乐名称
    name = Audio().get_audio_name_playing_txt()
    if not tuple(Utils().get_usb_music()).__contains__(name):
        Utils().raise_Exception_info('当前音乐不是U盘音乐')
@when(u'< 获取当前音乐名称')
def step_impl(context):
    #获取参数
    param = context.table[0]['o_result']
    ele_name = Audio().get_audio_name_playing_txt()
    Utils().set_context_map(param, ele_name)
@when(u'< 获取当前音乐歌手')
def step_impl(context):
    #获取参数
    param = context.table[0]['o_result']
    ele_artist = Audio().get_audio_artist_playing_txt()
    Utils().set_context_map(param, ele_artist)
@when(u'< 播放或暂停音乐')
def step_impl(context):
    Audio().click_pause_or_play_ele()
@when(u'< 播放蓝牙音乐')
def step_impl(context):
    # 点击我的音乐
    # Audio().click_audio_mine_my_ele()

    Audio().click_audio_mine_bluetooth_play_ele()

@when(u'< 等待音乐播放即将结束')
def step_impl(context):
    #获取音乐当前的播放时间和音乐总时间
    cur_showtime = str(Audio().get_audio_showtime_txt())
    all_time = str(Audio().get_audio_alltime_txt())
    # 将时间转化为秒
    cur_showtime_sec = int(cur_showtime.split(':')[0]) * 60 + int(cur_showtime.split(':')[1])
    all_time_sec = int(all_time.split(':')[0]) * 60 + int(all_time.split(':')[1])
    #计算还剩下多少时间 音乐结束
    left_sec = all_time_sec - cur_showtime_sec
    # 预留10s后面来校验是否跳转
    if left_sec > 10:
        time.sleep(left_sec - 10)
@when(u'< 从听歌识曲返回收音机')
def step_impl(context):
    Audio().click_audio_back_to_radio_ele()
@then(u'< 验证U盘已拔出')
def step_impl(context):
    if not Audio().chk_audio_usb_gone():
        Utils().raise_Exception_info('U盘拔出失败')
@when(u'< 随机播放相似歌曲')
def step_impl(context):
    #获取出参参数
    param = context.table[0]['o_result']
    Audio().click_audio_list_similar_ele()
    ele = Audio().get_audio_list_name_ele()
    if ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
        size = len(ele)
        idx = random.randint(0, size - 1)
        e = ele[idx]
        # 设置上下文变量 返回播放的音乐名称
        name = e.text.strip()
        Utils().set_context_map(param, name)
        e.click.wait()
    else:
        Utils().raise_Exception_info('网络刷新过慢，相似歌曲没有刷新出来')
@when(u'< 随机播放听TA的歌')
def step_impl(context):
    #获取出参参数
    param = context.table[0]['o_result']
    Audio().click_audio_list_ta_ele()
    ele = Audio().get_audio_list_name_ele()
    if ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
        size = len(ele)
        idx = random.randint(0, size - 1)
        e = ele[idx]
        # 设置上下文变量 返回播放的音乐名称
        name = e.text.strip()
        Utils().set_context_map(param, name)
        e.click.wait()
    else:
        Utils().raise_Exception_info('网络刷新过慢，听TA的歌没有刷新出来')
@when(u'< 点击音乐收藏或取消收藏')
def step_impl(context):
    Audio().click_audio_fav_ele()
@then(u'< 验证我的收藏记录')
def step_impl(context):
    flag = False
    # 获取参数信息
    chk_name = context.table[0]['name']
    if chk_name.__contains__('o_'):
        chk_name = Utils().get_context_map(chk_name)
    chk_faved = context.table[0]['is_faved']

    Audio().click_audio_mine_fav_ele()
    # 获取收藏歌曲名称
    ele = Audio().get_audio_mine_fav_name_ele()
    if ele.wait.exists():
        for e in ele:
            if e.text.strip().__eq__(chk_name):
                flag = True
                break
    else:
        Utils().raise_Exception_info('我的收藏音乐记录为空')

    if not str(flag).lower().__eq__(chk_faved.lower()):
        Utils().raise_Exception_info('音乐名称《' + chk_name + '》是否收藏校验失败')
    else:
        Audio().hide_audio_mine_drawer()
@when(u'< 从酷我返回到音乐')
def step_impl(context):
    Audio().back_from_kuwo()

