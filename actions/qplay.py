# -*- coding: UTF-8 -*-
import random

import time

from utils.utils import Utils


class Qplay:

    def __init__(self):
        global d
        d = Utils().get_device_obj()

        if not 'pateo.dls.qplay'.__eq__(d.info['currentPackageName']):
            Utils().raise_Exception_info('当前界面和预期界面不一致')

    # 获取本地音乐控件
    def __get_qplay_selector_ele(self):
        return Utils().get_ele_by_resourceId('pateo.dls.qplay:drawable/selector_menu_local')
    # 获取qplay本地歌曲窗口
    def __get_qplay_local_drawer_ele(self):
        return Utils().get_ele_by_resourceId('pateo.dls.qplay:id/drawer')

    # 获取音乐名称控件
    def __get_qplay_local_name_ele(self):
        return Utils().get_ele_by_resourceId('pateo.dls.qplay:id/drawer_list_category_text')

    # 获取当前播放的控件名称
    def __get_qplay_play_name_ele(self):
        return Utils().get_ele_by_resourceId('pateo.dls.qplay:id/title')
    # 获取qplay返回主界面控件
    def __get_qplay_home_ele(self):
        return Utils().get_ele_by_resourceId('pateo.dls.qplay:drawable/selector_button_home')
    # 点击本地音乐选择控件
    def click_qplay_selector_ele(self):
        ele = self.__get_qplay_selector_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('本地音乐选择控件不存在')
    # 获取当前播放的音乐名称
    def get_qplay_play_name(self):
        ele = self.__get_qplay_play_name_ele()
        if ele.exists:
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('当前没有音乐播放')
    # 点击返回主界面
    def click_qplay_home_ele(self):
        ele = self.__get_qplay_home_ele()
        if ele.exists:
            ele.click.wait()
        else:
            Utils().raise_Exception_info('qplay返回主界面控件不存在')

    #随机播放qplay本地音乐
    def click_qplay_local_name_random(self):
        # 判断是否已经播放音乐
        ele_name = self.__get_qplay_local_drawer_ele()
        if not ele_name.exists:
            self.click_qplay_selector_ele()
        # 随机选择
        ele = self.__get_qplay_local_name_ele()
        if ele.wait.exists() > 0:
            size = len(ele)
            idx = random.randint(0, size - 1)
            name = ele[idx].text.strip()
            ele[idx].click.wait()
            return name
        else:
            Utils().raise_Exception_info('qplay音乐列表为空')

    # 隐藏qplay本地歌曲窗口
    def hide_qplay_local_drawer_ele(self):
        ele = self.__get_qplay_local_drawer_ele()
        if ele.exists:
            #         获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
            # 滑动隐藏
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('qplay本地歌曲窗口不存在')

    # 验证当前是qplay初始界面
    def check_qplay_init(self):
        # 等待3s
        time.sleep(3)
        if not d(text = '连接QPlay').wait.exists():
            Utils().raise_Exception_info('当前不是QPlay初始界面')
    # 从音乐界面返回到launcher界面

    def back_to_launcher(self):
        # 判断是否在我的音乐库或音乐列表界面或者酷我，今日歌单
        if self.__get_qplay_local_drawer_ele().exists:
            self.hide_qplay_local_drawer_ele()
            self.click_qplay_home_ele()
        else:
            self.click_qplay_home_ele()
