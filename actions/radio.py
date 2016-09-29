# -*- coding: UTF-8 -*-
import random

import time

from support.global_vars import d, ver_flag
from utils.utils import Utils


class Radio:


    # 初始化 判断是否为当前应用
    def __init__(self):
        # 新旧版本的pkgname判断
        global pkg_name
        if ver_flag:
            pkg_name = "pateo.dls.app.radio"
        else:
            pkg_name = "com.qinggan.app.radio"


            #     获取上一首控件
    def __get_radio_prev_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/prev')

    # 获取下一首控件
    def __get_radio_next_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/next')
    # 获取收音机台号的数字控件
    def __get_radio_no_ele(self):
        ele = d(resourceId = pkg_name + ':id/freq_tv', className = 'android.widget.TextView')
        ele.wait.exists()
        return ele
    # 获取收藏收音机控件
    def __get_radio_fav_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/local_radio_fav')
    # 获取听歌识曲控件 未识别到歌曲
    def __get_radio_ide_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/played_program_identify')
    # 获取正在播放的项目名称
    def __get_radio_name_playing_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/played_program')
    # 获取正在播放的收音机节目列表
    def __get_radio_list_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/played_program_list')
    # 获取播放控件
    def __get_radio_play_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/play')
    # 获取收音机播放时间控件
    def __get_radio_showtime_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/showtime')
    # 获取收音机播放总时间
    def __get_radio_alltime_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/alltime')
    # 获取FM/AM选择列表控件
    def __get_radio_selector_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/selector_fm')
    # 获取预览radio的控件
    def __get_radio_preview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/selector_play_all_radio')
    # 获取回到主界面控件
    def __get_radio_home_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/selector_home')
    # 获取蜻蜓FM的控件
    def __get_radio_qt_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/selector_net')
    # 获取收音机搜索控件
    def __get_radio_search_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_search')
    #获取FM选择tab控件
    def __get_radio_selector_fm_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/list_band_fm')
    # 获取FM列表的listview
    def __get_radio_selector_fm_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/gridview')
    # 获取FM列表中的节目栏容器
    def __get_radio_selector_fm_listview_container_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/container')
    # 获取FM/AM列表中的收藏控件
    def __get_radio_selector_fav_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/crown')
    # 获取FM/AM窗口控件
    def __get_radio_selector_drawer_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/drawer')
    # 获取蜻蜓FM的窗口控件
    def __get_radio_qt_drawer_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/drawer_net')
    # 获取精选电台控件
    def __get_radio_qt_category_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/category_selected')
    # 获取电台栏目控件
    def __get_radio_qt_category_title_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/display_name')
    # 获取电台栏目中节目列表窗口
    def __get_radio_qt_category_list_drawer_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/drawer_album_program')
    # 获取电台栏目节目列表标题控件
    def __get_radio_qt_category_list_title_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/album_title_name')
    # 获取电台栏目节目列表的节目名称
    def __get_radio_qt_category_list_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/album_program_name')
    # 获取蜻蜓FM的收藏控件
    def __get_radio_qt_fav_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favorite')
    # 获取蜻蜓FM的栏目控件
    def __get_radio_qt_title_playing_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/album_tv')
    # 获取蜻蜓FM窗口中的我的收藏
    def __get_radio_qt_collected_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/category_collected')
    # 获取收藏的标题控件
    def __get_radio_qt_collected_title_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favorite_album_name')
    # 获取最近收听的控件
    def __get_radio_qt_latest_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/category_latest')
    # 获取蜻蜓FM最近收听节目控件
    def __get_radio_qt_latest_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/latest_program_name')
    # 获取收音机列表窗口控件
    def __get_radio_list_drawer_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/drawer_program')
    # 获取收音机列表的listview控件
    def __get_radio_list_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/program_listview')
    # 获取收音机列表中的节目控件
    def __get_radio_list_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/program_name')
    # 获取搜索框控件
    def __get_radio_search_keyword_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_keyword')
    # 获取搜索清空控件
    def __get_radio_search_clear_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/icon_search_clear')
    # 获取取消搜索控件
    def __get_radio_search_cancel_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/lab_cancel')
    # 获取搜索列表中节目title
    def __get_radio_search_list_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取搜索列表中节目的FM/AM编号
    def __get_radio_search_list_title_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_detail')
    #获取收音机的微调控件
    def get_radio_weitiao_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/play_time')

    # 获取听歌识曲中的歌曲名称控件
    def __get_radio_ide_audio_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/gracenote_track_tv')

    # 点击上一首控件
    def click_radio_prev_ele(self):
        ele = self.__get_radio_prev_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('上一首控件不存在')

    # 点击下一首控件
    def click_radio_next_ele(self):
        ele = self.__get_radio_next_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('下一首控件不存在')
    # 点击播放或者暂停收音机
    def click_radio_pause_or_play_ele(self):
        next_ele = self.__get_radio_next_ele()
        prev_ele = self.__get_radio_prev_ele()
        if next_ele.wait.exists() and prev_ele.wait.exists():
            prev_x = (int(prev_ele.info['bounds']['left']) + int(prev_ele.info['bounds']['right'])) / 2
            prev_y = (int(prev_ele.info['bounds']['bottom']) + int(prev_ele.info['bounds']['top'])) / 2

            next_x = (int(next_ele.info['bounds']['left']) + int(next_ele.info['bounds']['right'])) / 2
            next_y = (int(next_ele.info['bounds']['bottom']) + int(next_ele.info['bounds']['top'])) / 2

            pause_x = (prev_x + next_x) / 2
            pause_y = (prev_y + next_y) / 2

            d.click(pause_x, pause_y)
        else:
            Utils().raise_Exception_info('上一首或下一首控件不存在')

    # 获取正在播放的收音机编号
    def get_radio_no_playing_txt(self):
        ele = self.__get_radio_no_ele()
        fm_no = ''
        if len(ele) > 0:
            for s in ele:
                fm_no += s.text.strip()
            return fm_no
        else:
            Utils().raise_Exception_info('收音机台为空')

    # 点击收藏或者取消收藏
    def click_radio_fav_or_cancel_ele(self):
        ele = self.__get_radio_fav_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('收藏控件不存在')
    # 点击听歌识曲控件
    def click_radio_ide_ele(self):
        ele = self.__get_radio_ide_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('听歌识曲控件不存在')

    # 获取正在播放的fm名称
    def get_radio_name_playing_txt(self):
        ele = self.__get_radio_name_playing_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('正在播放的收音机名称控件不存在')
    # 点击收音机列表控件
    def click_radio_list_ele(self):
        ele = self.__get_radio_list_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('收音机列表控件不存在')

    # 点击播放收音机控件
    def click_radio_play_ele(self):
        ele = self.__get_radio_play_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('收音机播放控件不存在')
    # 校验收音机是否播放
    # 播放：true 恢复播放控件不可见
    # 暂停：false 恢复播放控件可见
    def get_radio_is_playing(self):
        ele = self.__get_radio_play_ele()
        return not ele.exists
    # 点击FM/AM选择器
    def click_radio_selector_ele(self):
        ele = self.__get_radio_selector_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('FM/AM选择控件不存在')
    #点击预览radio控件
    def click_radio_preview_ele(self):
        ele = self.__get_radio_preview_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('收音机预览控件不存在')

    # 点击蜻蜓FM控件
    def click_radio_qt_ele(self):
        ele = self.__get_radio_qt_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('蜻蜓FM控件不存在')

    # 点击收音机的搜索控件
    def click_radio_search_ele(self):
        ele = self.__get_radio_search_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('收音机的搜索控件不存在')
    #点击收音机的fm tab页
    def click_radio_selector_fm_ele(self):
        ele = self.__get_radio_selector_fm_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('FM选择tab控件不存在')

    # 滑动列表到顶部
    def scroll_radio_selector_listview_to_beginning(self):
        ele = self.__get_radio_selector_fm_listview_ele()
        if ele.wait.exists():
            #     获取第一个fm的no
            ele_containers = self.__get_radio_selector_fm_listview_container_ele()
            if len(ele_containers) > 0:
                fm_no = ele_containers[0].child(resourceId = pkg_name + ':id/list_freq').text.strip()
            #     while里面判断
            while ele.scroll.vert.backward(steps = 5):
                ele_containers = self.__get_radio_selector_fm_listview_container_ele()
                if len(ele_containers) > 0:
                    fm_no1 = ele_containers[0].child(resourceId=pkg_name + ':id/list_freq').text.strip()
                    # 判断是否到达顶部
                    if fm_no == fm_no1:
                        break
                    fm_no = fm_no1
        else:
            Utils().raise_Exception_info('FM选择界面的listview不存在')

    # 刷新FM列表
    def refresh_radio_selector_listview(self):
        # 先滑动到顶部
        self.scroll_radio_selector_listview_to_beginning()
        # 获取listview 控件
        ele = self.__get_radio_selector_fm_listview_ele()
        if ele.wait.exists():
            ele.scroll.vert.backward(steps = 10)
            # 以上一曲控件来判断是否刷新结束
            ele_prev = self.__get_radio_prev_ele()
            ele_prev.wait.exists(timeout = Utils().LONG_TIME_OUT)
        else:
            Utils().raise_Exception_info('FM选择界面的listview不存在')
    # 根据fmno播放电台
    def click_radio_selector_fm_by_no_ele(self, fm_no):
        flag = True
        #先滑到顶部
        self.scroll_radio_selector_listview_to_beginning()
        # 获取listview
        ele = self.__get_radio_selector_fm_listview_ele()
        if ele.wait.exists():
            # 查找是否存在该fm_no  ele.scroll.vert.forward
            ele_fm = d(text=fm_no)

            if ele_fm.wait.exists():
                flag = False
                ele_fm.click.wait()
            else:
                while ele.scroll.vert.forward(steps = 5) and flag:
                    ele_fm = d(text = fm_no)
                    if ele_fm.wait.exists():
                        flag = False
                        ele_fm.click.wait()
                        break

            if flag:
                Utils().raise_Exception_info('指定《' + fm_no + '》不存在')
        else:
            Utils().raise_Exception_info('FM选择界面的listview不存在')
    #随机选择FM收听
    def click_radio_selector_fm_random_ele(self):
        ele = self.__get_radio_selector_fm_listview_container_ele()
        size = len(ele)
        if size > 0:
            index = random.randint(0, size - 1)
            fm_no = ele[index].child(resourceId = pkg_name + ':id/list_freq').text.strip()
            ele[index].click.wait()
            return fm_no
        else:
            Utils().raise_Exception_info('FM列表内容为空')
    # 隐藏FM/AM选择窗口
    def hide_radio_selector_drawer_ele(self):
        ele = self.__get_radio_selector_drawer_ele()
        if ele.wait.exists():
        #         获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
        # 滑动隐藏
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('FM/AM列表选择窗口不存在')

    # 验证指定电台是否被收藏
    def get_radio_selector_fm_is_faved_by_no(self, fm_no):
        # 切换到fm_tab页
        Radio().click_radio_selector_fm_ele()
        # 先滑到顶部
        self.scroll_radio_selector_listview_to_beginning()
        # 获取listview
        ele = self.__get_radio_selector_fm_listview_ele()
        if ele.wait.exists():
            # 判断当前界面是否含有指定电台
            ele_containers = self.__get_radio_selector_fm_listview_container_ele()
            if len(ele_containers) > 0:
                for c in ele_containers:
                    e = c.child(resourceId=pkg_name + ':id/list_freq')
                    if e.text.strip() == fm_no:
                        is_faved = e.sibling(resourceId = pkg_name + ':id/crown').exists
                        self.hide_radio_selector_drawer_ele()
                        return is_faved
                # 如果不存在滑动到下一屏
                while ele.scroll.vert.forward(steps=5):
                    ele_containers = self.__get_radio_selector_fm_listview_container_ele()
                    for c in ele_containers:
                        e = c.child(resourceId=pkg_name + ':id/list_freq')
                        if e.text.strip == fm_no:
                            is_faved = e.sibling(resourceId=pkg_name + ':id/crown').exists
                            self.hide_radio_selector_drawer_ele()
                            return is_faved
                # 判断有没有查找成功
                Utils().raise_Exception_info('指定《' + fm_no + "》不存在")
            else:
                Utils().raise_Exception_info('FM选择界面list为空')
        else:
            Utils().raise_Exception_info('FM选择界面的listview不存在')

    # 隐藏蜻蜓FM的窗口
    def hide_radio_qt_drawer_ele(self):
        ele = self.__get_radio_qt_drawer_ele()
        if ele.wait.exists():
            #         获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
            # 滑动隐藏
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('蜻蜓FM窗口不存在')
    # 点击精选电台
    def click_radio_qt_category_ele(self):
        ele = self.__get_radio_qt_category_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('精选电台控件不存在')
    # 随机点击栏目
    # 返回title 为了后面校验
    def click_radio_qt_category_title_ele(self):
        ele = self.__get_radio_qt_category_title_ele()
        size = len(ele)
        if size > 0:
            index = random.randint(0,size - 1)
            ret = ele[index].text.strip()
            ele[index].click.wait()
            return ret
        else:
            Utils().raise_Exception_info('栏目没有加载出来，可能是网络太慢')
    # 隐藏电台栏目节目列表窗口
    def hide_radio_qt_category_list_drawer_ele(self):
        ele = self.__get_radio_qt_category_list_drawer_ele()
        if ele.wait.exists():
            #         获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
            # 滑动隐藏
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('电台栏目节目窗口不存在')

    # 获取电台栏目中节目列表的标题内容
    def get_radio_qt_category_list_title_txt(self):
        ele = self.__get_radio_qt_category_list_title_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('蜻蜓FM电台节目列表标题控件不存在')
    # 随机选择节目收听
    def click_radio_qt_category_list_name_random_ele(self):
        ele = self.__get_radio_qt_category_list_name_ele()
        ele.wait.exists(timeout = Utils().LONG_TIME_OUT)
        size = len(ele)
        if size > 0:
            index = random.randint(0, size - 1)
            # 获取节目名称
            name = ele[index].text.strip()
            #     点击播放选中节目
            ele[index].click.wait()
            return name
        else:
            Utils().raise_Exception_info('节目列表为空，可能是网络原因')

    # 收藏或者取消收藏蜻蜓FM节目
    def click_radio_qt_fav_ele(self):
        ele = self.__get_radio_qt_fav_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('蜻蜓FM的收藏控件不存在')
    # 获取蜻蜓FM正在播放的栏目名称
    def get_radio_qt_title_playing_txt(self):
        ele = self.__get_radio_qt_title_playing_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('正在播放的蜻蜓FM栏目名称控件不存在')
    # 点击进入蜻蜓FM的我的收藏tab页
    def click_radio_qt_collected_ele(self):
        ele = self.__get_radio_qt_collected_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('蜻蜓FM我的收藏控件不存在')
    # 查看指定蜻蜓FM是否被收藏
    # true: 返回被收藏
    # false: 返回没有被收藏
    def get_radio_qt_collected_title_is_exists(self, qt_title):
        ele = self.__get_radio_qt_collected_title_ele()
        is_exists = False
        for e in ele:
            if e.text.strip == qt_title:
                is_exists = True
                break
        self.hide_radio_qt_drawer_ele()
        return is_exists
    #播放收藏的蜻蜓FM
    def click_radio_qt_collected_title_ele(self):
        ele = self.__get_radio_qt_collected_title_ele()
        size = len(ele)
        if size > 0:
            ele[0].click.wait()
            return ele[0].text.strip()
        else:
            Utils().raise_Exception_info('收藏的蜻蜓FM列表为空')
    # 点击蜻蜓FM的最近收听
    def click_radio_qt_latest_ele(self):
        ele = self.__get_radio_qt_latest_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('蜻蜓FM最近收听控件不存在')
    # 查看指定蜻蜓FM节目是否在收听历史中
    def get_radio_qt_latest_name_ele(self, qt_name):
        ele = self.__get_radio_qt_latest_name_ele()
        return ele
    # 隐藏收音机列表窗口
    def hide_radio_list_drawer_ele(self):
        ele = self.__get_radio_list_drawer_ele()
        if ele.wait.exists():
            #         获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
            # 滑动隐藏
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('收音机列表窗口不存在')

    #随机选择网络回听节目
    def click_radio_list_his_name_random_ele(self):
        # 滑动到顶部
        ele_listview = self.__get_radio_list_listview_ele()
        if ele_listview.exists:
            ele_listview.scroll.vert.toBeginning()
        else:
            Utils().raise_Exception_info('网络回听listview控件不存在')

        ele_name = self.__get_radio_list_name_ele()
        if len(ele_name) > 0:
            idx = random.randint(0, len(ele_name) - 1)
            if ele_name[idx].sibling(text = '网络回听').exists:
                ret = ele_name[idx].text.strip()
                ele_name[idx].click.wait()
                return ret
            else:
                Utils().raise_Exception_info('没有找到网络回听节目')
        else:
            Utils().raise_Exception_info('节目列表为空')
    #点击清空搜索框控件
    def click_radio_search_clear_ele(self):
        ele = self.__get_radio_search_clear_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('清空搜索框控件不存在')

    # 在输入框输入内容
    def input_radio_search_keyword_ele(self, input_text):
    #     清空搜索框
        self.click_radio_search_clear_ele()
    #     输入内容
        ele = self.__get_radio_search_keyword_ele()
        if ele.wait.exists():
            ele.set_text(Utils().unicode_input(input_text))
        else:
            Utils().raise_Exception_info('搜索框控件不存在')

    # 点击取消控件
    def click_radio_search_cancel_ele(self):
        ele = self.__get_radio_search_cancel_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('取消控件不存在')

    # 获取搜索框内容
    def get_radio_search_keyword_txt(self):
        ele = self.__get_radio_search_keyword_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('收音机搜索框控件不存在')
    # 验证当前界面为收音机主界面
    def chk_radio_is_home_page(self):
        ele = self.__get_radio_home_ele()
        if not ele.wait.exists():
            Utils().raise_Exception_info('当前界面不是收音机主界面')

    # 随机选择搜索结果收听
    # 返回fm台号
    def click_radio_search_list_title_random_ele(self):
        ele_name = self.__get_radio_search_list_name_ele()
        ele_title = self.__get_radio_search_list_title_ele()
        size_name = len(ele_name)
        if size_name > 0:
            idx = random.randint(0, size_name - 1)
            # 获取FM编号和节目
            name_txt = ele_name[idx].text.strip()
            title_txt = ele_title[idx].text.strip()
            # 保存在上下文变量中
            Utils().set_context_map(title_txt, name_txt)
            ele_name[idx].click.wait()
            # 返回标题名称
            return title_txt

        else:
            Utils().raise_Exception_info('收音机搜索结果为空')
    # 播放收藏的电台
    def click_radio_selector_fm_faved(self):
        # 进入到FM页签
        self.click_radio_selector_fm_ele()
        self.click_radio_selector_fm_ele()
    #   获取listview
        ele_listview = self.__get_radio_selector_fm_listview_ele()
        if ele_listview.exists:
            if ele_listview.scroll.vert.to(resourceId =pkg_name + ':id/crown'):
                ele = d(resourceId = pkg_name + ':id/crown')
                ele.click.wait()
                # 返回收藏的台号
                # return ele.sibling(resourceId=pkg_name + ':id/list_freq').text.strip()
            else:
                Utils().raise_Exception_info('没有找到收藏的电台')
        else:
            Utils().raise_Exception_info('FM选择界面的listview不存在')

    #调整微调
    def scroll_radio_weitiao_ele(self):
        ele = Radio().get_radio_weitiao_ele()
        if ele.wait.exists():
            x = (int(ele.info['bounds']['left']) + int(ele.info['bounds']['right'])) / 2
            y = (int(ele.info['bounds']['bottom']) + int(ele.info['bounds']['top'])) / 2
            d.swipe(x, y, x + 200, y)
        else:
            Utils().raise_Exception_info('微调控件不存在')

    # 点击返回主界面HOME键
    def click_radio_home_ele(self):
        ele = self.__get_radio_home_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('返回主界面的HOME控件不存在')

    #回到launcher
    def back_to_launcher(self):
        # 等待界面稳定
        time.sleep(3)
        # 判断是否在FM/AM选择窗口

        if self.__get_radio_selector_drawer_ele().exists:
            self.hide_radio_selector_drawer_ele()
            self.click_radio_home_ele()
        #     判断是否蜻蜓FM窗口
        elif self.__get_radio_qt_drawer_ele().exists:
            self.hide_radio_qt_drawer_ele()
            self.click_radio_home_ele()
        #     判断是否蜻蜓FM的list窗口
        elif self.__get_radio_qt_category_list_drawer_ele().exists:
            self.hide_radio_qt_category_list_drawer_ele()
            self.click_radio_home_ele()
        #     判断是否为list窗口
        elif self.__get_radio_list_drawer_ele().exists:
            self.hide_radio_list_drawer_ele()
            self.click_radio_home_ele()
        #     判断是否在搜索界面
        elif self.__get_radio_search_keyword_ele().exists:
            self.click_radio_search_cancel_ele()
            self.click_radio_home_ele()
        else:
            self.click_radio_home_ele()

    #获取听歌识曲状态
    #true: 识别到
    #false: 未识别到
    def get_radio_ide_status(self):
        ele = d(text = '未识别到歌曲')
        return not ele.wait.exists(timeout = Utils().LONG_TIME_OUT)

    # 点击听歌识曲中的歌曲
    #返回识别到的歌曲名
    def click_radio_ide_audio(self):
        ele = self.__get_radio_ide_audio_name_ele()

        if ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
            name = ele.text.strip()
            ele.click.wait()
            return name
        else:
            Utils().raise_Exception_info('未识别到歌曲')

