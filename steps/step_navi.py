# -*- coding: UTF-8 -*-
import random

import time
from behave import then, when

from actions.navi import Navi
from support.global_vars import d
from utils.utils import Utils


@then(u'< 验证当前为导航主界面')
def step_impl(context):
    Navi().chk_navi_is_home()


@then(u'< 验证导航启动界面元素')
def step_impl(context):
    compass = Navi().get_navi_Compass_ele()
    sitelite = Navi().get_navi_satellite_ele()
    curroad = Navi().get_navi_current_road_name_ele()
    zoomseekbar = Navi().get_navi_zoomSeekBar_ele()

    if not compass.wait.exists() and sitelite.wait.exists() \
            and \
            (curroad.wait.exists() or zoomseekbar.wait.exists()):
        Utils().raise_Exception_info('导航主界面元素校验失败')


@when(u'< 打开导航搜索')
def step_impl(context):
    curroad = Navi().get_navi_current_road_name_ele()
    search = Navi().get_navi_search_ele()
    if search.wait.exists():
        search.click.wait()
    elif curroad.wait.exists():
        curroad.click()
        search.click.wait()
    else:
        Utils().raise_Exception_info('导航搜索控件打开失败')


@when(u'< 选择导航搜索城市')
def step_impl(context):
    city_name = context.table[0]['city_name']

    city_search = Navi().get_navi_search_city_bar_ele()
    # 点击城市控件
    if city_search.wait.exists():
        city_search.click.wait()
    else:
        Utils().raise_Exception_info('搜索城市控件不存在')

    search_key = Navi().get_navi_search_key_ele()
    if search_key.wait.exists():
        search_key.set_text(Utils().unicode_input(city_name))
    else:
        Utils().raise_Exception_info('搜索框控件不存在')
    # 搜索列表
    list_item = Navi().get_navi_search_city_list_item()
    if list_item.wait.exists(timeout=Utils().LONG_TIME_OUT):
        for e in list_item:
            if e.text.strip() == city_name:
                e.click.wait()
                break
    else:
        Utils().raise_Exception_info('没有搜索到对应的城市')


@when(u'< 选择搜索的导航地址')
def step_impl(context):
    address = context.table[0]['address']
    o_result = context.table[0]['o_result']

    search_key = Navi().get_navi_search_key_ele()
    if search_key.wait.exists():
        search_key.set_text(Utils().unicode_input(address))
    else:
        Utils().raise_Exception_info('搜索框控件不存在')

    list_item = Navi().get_navi_search_addr_list_title()

    if list_item.wait.exists(timeout=Utils().LONG_TIME_OUT):
        size = len(list_item)
        idx = random.randint(0, size - 1)
        e = list_item[idx]
        ret = e.text.strip()
        e.click.wait()
        # 返回选择的地址并存入上下文
        Utils().set_context_map(o_result, ret)
    else:
        Utils().raise_Exception_info('没有搜索到对应的城市')


@when(u'< 获取将要导航目的地地址')
def step_impl(context):
    # 获取目的地地址出参
    param = context.table[0]['o_result']
    ele = Navi().get_navi_ready_dest_ele()
    if ele.wait.exists():
        Utils().set_context_map(param, ele.text.strip())
    else:
        Utils().raise_Exception_info('导航目的地控件不存在')


@then(u'< 验证导航界面的元素')
def step_impl(context):
    compass = Navi().get_navi_Compass_ele()
    curroad = Navi().get_navi_current_road_name_ele()
    pager = Navi().get_navi_navipager_ele()
    time_indicator = Navi().get_navi_time_indicator_ele()

    if not compass.wait.exists() and curroad.wait.exists() and pager.wait.exists() and time_indicator.wait.exists():
        Utils().raise_Exception_info('导航界面元素检查失败，缺少元素信息')


@when(u'< 导航到目的地')
def step_impl(context):
    navi_dest = Navi().get_navi_ready_to_dest_ele()
    dest_time = Navi().get_navi_to_dest_time_ele()
    if navi_dest.wait.exists():
        navi_dest.click.wait()
        if dest_time.wait.exists(timeout=20000):
            dest_time.wait.gone(timeout=15000)
    else:
        Utils().raise_Exception_info('导航到指定地址控件不存在')


@when(u'< 收藏或取消收藏导航地址')
def step_impl(context):
    fav_ele = Navi().get_navi_ready_dest_fav_ele()
    if fav_ele.wait.exists():
        fav_ele.click()
    else:
        Utils().raise_Exception_info('地址收藏控件不可见')


@when(u'< 打开导航收藏')
def step_impl(context):
    fav_ele = Navi().get_navi_search_fav_ele()
    if fav_ele.wait.exists():
        fav_ele.click.wait()
    else:
        Utils().raise_Exception_info('收藏控件不可见')


@then(u'< 验证地址是否被收藏')
def step_impl(context):
    # 获取参数信息
    addr = context.table[0]['address']
    is_faved = context.table[0]['is_faved']
    if str(addr).startswith('o_'):
        addr = Utils().get_context_map(addr)

    list_view = Navi().get_navi_search_listview_ele()
    if list_view.wait.exists():
        if list_view.info['scrollable']:
            flag = list_view.scroll.vert.to(text=addr)

        else:
            ele = d(text=addr)
            flag = ele.wait.exists()

        if str(flag).lower() != is_faved.lower():
            Utils().raise_Exception_info('验证是否被收藏状态不一致，期望值为:' + is_faved + ', 实际值为：' + str(flag))
    else:
        Utils().raise_Exception_info('收藏列表不存在')


@when(u'< 删除指定地址')
def step_impl(context):
    addr = context.table[0]['address']
    if str(addr).startswith('o_'):
        addr = Utils().get_context_map(addr)

    # 获取删除控件并点击
    del_ele = Navi().get_navi_his_fav_del_ele(addr)
    if del_ele.wait.exists():
        del_ele.click()
    # 点击完成控件 完成删除操作
    ok_ele = d(text='完成')
    if ok_ele.wait.exists():
        ok_ele.click()


@when(u'< 选择收藏的导航地址')
def step_impl(context):
    addr = context.table[0]['address']
    if str(addr).startswith('o_'):
        addr = Utils().get_context_map(addr)

    list_view = Navi().get_navi_search_listview_ele()
    if list_view.wait.exists():
        if list_view.info['scrollable']:
            flag = list_view.scroll.vert.to(text=addr)
            if flag:
                ele = d(text=addr)
                if ele.wait.exists():
                    ele.click.wait()
                else:
                    Utils().raise_Exception_info('指定收藏地址不存在')
            else:
                Utils().raise_Exception_info('指定收藏地址不存在')
        else:
            ele = d(text=addr)
            if ele.wait.exists():
                ele.click.wait()
    else:
        Utils().raise_Exception_info('收藏列表不存在')


@then(u'< 验证附近查询结果')
def step_impl(context):
    title = context.table[0]['nearby_title']
    if str(title).startswith('o_'):
        title = Utils().get_context_map(title)

    # 验证搜索结果的标题是否一致
    nearby_title = Navi().get_navi_nearby_title_ele()
    if nearby_title.wait.exists():
        txt = nearby_title.text.strip()
        if txt != title:
            Utils().raise_Exception_info('搜索附近的XXX标题不一致，期望值为：' + title + ', 实际值是: ' + txt)
    else:
        Utils().raise_Exception_info('搜索附近的XXX的标题控件不存在')

    # 验证是否有查询结果
    nearby_name = Navi().get_navi_nearby_name_ele()
    if not nearby_name.wait.exists():
        Utils().raise_Exception_info('搜索附近的XXX的结果为空')
