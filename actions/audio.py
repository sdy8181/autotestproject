# -*- coding: UTF-8 -*-
import random

import time

from support.global_vars import ver_flag, d
from utils.utils import Utils


class Audio:

    def __init__(self):

        # 新旧版本的pkgname判断
        global pkg_name
        if ver_flag:
            pkg_name = "pateo.dls.audioui"
        else:
            pkg_name = "com.qinggan.app.music"

        # if not d(packageName = pkg_name).wait.exists(timeout  = Utils().LONG_TIME_OUT):
        #     Utils().raise_Exception_info('当前界面和预期界面不一致')

    # 获取下一首控件
    def __get_next_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/next')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/img_next')

    # 获取上一首控件
    def __get_prev_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/prev')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/img_previous')
        
    # 获取正在播放的歌曲名字控件
    def __get_audio_name_playing_ele(self):
        # 最新酷我音乐界面分析
        package_name = d.info['currentPackageName']
        if package_name == 'cn.kuwo.kwmusiccar':
            return Utils().get_ele_by_resourceId(package_name + ':id/tv_songname')

        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/name')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    
    # 获取正在播放的演唱者控件
    def __get_audio_artist_playing_ele(self):
         # 最新酷我音乐界面分析
        package_name = d.info['currentPackageName']
        if package_name == 'cn.kuwo.kwmusiccar':
            return Utils().get_ele_by_resourceId(package_name + ':id/tv_artist')

        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/artist')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_artist')
        
    # 获取音乐列表控件
    def __get_audio_list_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/control_name')
        
    # 获取音乐播放时间控件
    def __get_audio_showtime_ele(self):
         # 最新酷我音乐界面分析
        package_name = d.info['currentPackageName']
        if package_name == 'cn.kuwo.kwmusiccar':
            return Utils().get_ele_by_resourceId(package_name + ':id/tvTime')

        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/showtime')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_currenttime')
        
    # 获取音乐播放总时间控件
    def __get_audio_alltime_ele(self):
         # 最新酷我音乐界面分析
        package_name = d.info['currentPackageName']
        if package_name == 'cn.kuwo.kwmusiccar':
            return Utils().get_ele_by_resourceId(package_name + ':id/tvTime')

        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/alltime')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_alltime')

    # 获取我的音乐库控件
    def __get_audio_mine_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_mine')

    # 获取酷我音乐控件
    def __get_audio_kuwo_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_baidu')

    # 获取返回主界面控件
    def __get_audio_home_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_home')
    #获取今日歌单控件
    def __get_audio_smart_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_smart')

    # 获取音乐搜索控件
    def __get_audio_search_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_search')

    # 我的音乐库窗口控件
    # 获取我的音乐库窗口控件
    def __get_audio_mine_drawer_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/blurDrawer')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/drawer')

    # 获取音乐库中的我的音乐
    def __get_audio_mine_my_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_local')
        else:
            return Utils().get_ele_by_text('我的音乐')

    # 获取音乐库中的我的收藏
    def __get_audio_mine_fav_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_fav')
        else:
            return Utils().get_ele_by_text('我的收藏')
    # 获取音乐库中的听歌识曲
    def __get_audio_mine_ide_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_ide')
        else:
            return Utils().get_ele_by_text('听歌识曲')
    # 获取音乐库中的全部歌曲
    def __get_audio_mine_all_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_all')
        else:
            return Utils().get_ele_by_text('全部歌曲')

    # 获取音乐列表控件
    def __get_audio_mine_all_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/play_listview')

    # 获取USB歌曲控件
    def __get_audio_mine_usb_ele(self):
        ele = d(text = 'USB歌曲', resourceId = pkg_name + ':id/txt_title')
        ele.wait.exists()
        return ele

    # 获取USB歌曲同级的歌曲数目
    def __get_audio_mine_usb_cnt_ele(self):
        ele = self.__get_audio_mine_usb_ele()
        if ele.wait.exists():
            ele1 = ele.sibling(resourceId = pkg_name + ':id/txt_artist')
            ele1.wait.exists()
            return ele1
        else:
            Utils().raise_Exception_info('USB音乐控件不存在')

    # 获取USB歌曲播放控件
    def __get_audio_mine_usb_play_ele(self):
        ele = self.__get_audio_mine_usb_ele()
        if ele.wait.exists():
            ele1 = ele.sibling(resourceId = pkg_name + ':id/mltImage')
            ele1.wait.exists()
            return ele1
        else:
            Utils().raise_Exception_info('USB音乐控件不存在')

    # 获取蓝牙歌曲播放控件
    def __get_audio_mine_bluetooth_play_ele(self):
        ele = Utils().get_ele_by_resourceId(pkg_name + ':drawable/menu_selector_bluetooth')
        return ele

    # 获取音乐收藏控件
    def __get_audio_fav_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/fav_ibn')
        else:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/img_fav')

    # 获取听Ta的歌曲
    def __get_audio_list_ta_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_ide')
        else:
            return Utils().get_ele_by_text('听Ta的歌')
    # 获取听ta的歌曲的listview控件
    def __get_audio_list_ta_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/play_listview')
    # 获取听ta的歌曲的音乐名称控件
    def __get_audio_list_ta_listview_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取我的收藏的音乐名称控件
    def get_audio_mine_fav_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取听ta的歌曲的歌手控件
    def __get_audio_list_ta_listview_artist_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_artist')
    # 获取相似歌曲控件
    def __get_audio_list_similar_ele(self):
        if ver_flag:
            return Utils().get_ele_by_resourceId(pkg_name + ':id/tab_all')
        else:
            return Utils().get_ele_by_text('相似歌曲')

    # 获取列表中的歌曲名字控件
    def get_audio_list_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取列表中演唱者名字控件
    def __get_audio_list_artist_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_artist')
    # 获取酷我窗口的专辑控件
    def __get_audio_kuwo_name_ele(self):
        # 针对新版酷我音乐
        package_name = d.info['currentPackageName']
        if package_name == 'cn.kuwo.kwmusiccar':
            home = Utils().get_ele_by_resourceId(package_name + ':id/layout_home')
            if home.wait.exists():
                home.click.wait()

            ele = Utils().get_ele_by_text('精选电台')
            if ele.wait.exists():
                ele.click.wait()
                tj_ele = Utils().get_ele_by_text('推荐')
                if tj_ele.wait.exists():
                    tj_ele.click.wait()
                    return Utils().get_ele_by_text('一人一首成名曲')

        # return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取今日歌单音乐名称
    def __get_audio_smart_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取今日歌单演唱者名字
    def __get_audio_smart_artist_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_artist')
    # 获取搜索框
    def __get_audio_search_keyword_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_keyword')
    # 获取清空搜索框控件
    def __get_audio_search_clear_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/icon_search_clear')
    # 获取取消搜索控件
    def __get_audio_search_cancel_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/lab_cancel')
    # 获取音乐搜索列表
    def __get_audio_search_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_listview')
    # 获取音乐搜索列表中的音乐名
    def __get_audio_search_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_title')
    # 获取音乐搜索列表中的演唱者
    def __get_audio_search_artist_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/txt_artist')

    # 获取听歌识曲返回到radio控件
    def __get_audio_back_to_radio_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/radio_back_btn')

    # 点击暂停或播放控件
    def click_pause_or_play_ele(self):
        next_ele = self.__get_next_ele()
        prev_ele = self.__get_prev_ele()
        if next_ele.exists and prev_ele.wait.exists():
            prev_x = (int(prev_ele.info['bounds']['left']) + int(prev_ele.info['bounds']['right'])) / 2
            prev_y = (int(prev_ele.info['bounds']['bottom']) + int(prev_ele.info['bounds']['top'])) / 2

            next_x = (int(next_ele.info['bounds']['left']) + int(next_ele.info['bounds']['right'])) / 2
            next_y = (int(next_ele.info['bounds']['bottom']) + int(next_ele.info['bounds']['top'])) / 2

            play_or_pause_x = (prev_x + next_x) / 2
            play_or_pause_y = (prev_y + next_y) / 2

            d.click(play_or_pause_x, play_or_pause_y)
        else:
            Utils().raise_Exception_info('上一首或者下一首控件不存在')

    # 点击下一首控件
    def click_next_ele(self):
        ele = self.__get_next_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('下一首控件不存在')
    # 点击上一首控件
    def click_prev_ele(self):
        ele = self.__get_prev_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('上一首控件不存在')

    # 获取正在播放的歌曲名字内容
    def get_audio_name_playing_txt(self):
        ele = self.__get_audio_name_playing_ele()
        if ele.wait.exists():
            return str(ele.text).strip()
        else:
            Utils().raise_Exception_info('音乐名字控件不存在')

    # 获取正在播放的歌曲演唱者的名字
    def get_audio_artist_playing_txt(self):
        ele = self.__get_audio_artist_playing_ele()
        if ele.wait.exists():
            return str(ele.text).strip()
        else:
            Utils().raise_Exception_info('音乐演唱者控件不存在')

    # 点击音乐列表打开列表
    def click_audio_list_ele(self):
        ele = self.__get_audio_list_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('音乐列表控件不存在')

    # 获取音乐播放时间文本
    def get_audio_showtime_txt(self):
        ele = self.__get_audio_showtime_ele()
        if ele.wait.exists():
            return ele.text.strip().split('|')[0]
        else:
            Utils().raise_Exception_info('音乐播放时间控件不存在')

    # 获取音乐播放总时间文本
    def get_audio_alltime_txt(self):

        ele = self.__get_audio_alltime_ele()
        if ele.wait.exists():
            allTime = ele.text.strip().split('|')
            if len(allTime) > 1:
                return allTime[1]
            else:
                return allTime[0]
            # return ele.text.strip()
        else:
            Utils().raise_Exception_info('音乐播放总时间控件不存在')

    # 点击我的音乐库控件打开
    def click_audio_mine_ele(self):
        ele = self.__get_audio_mine_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('我的音乐库控件不存在')

    # 点击酷我音乐控件
    def click_audio_kuwo_ele(self):
        ele = self.__get_audio_kuwo_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('酷我音乐控件不存在')

    # 点击回到主界面控件
    def click_audio_home_ele(self):
        ele = self.__get_audio_home_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('音乐的Home控件不存在')
    # 点击今日歌单控件
    def click_audio_smart_ele(self):
        ele = self.__get_audio_smart_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('今日歌单控件不存在')

    # 点击音乐搜索控件
    def click_audio_search_ele(self):
        ele = self.__get_audio_search_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('音乐搜索控件不存在')

    # 隐藏我的音乐库
    def hide_audio_mine_drawer(self):
        ele = self.__get_audio_mine_drawer_ele()
        if ele.wait.exists():
            # 获取窗口坐标
            x = ele.info['bounds']['right']
            y = int(ele.info['bounds']['bottom']) / 2
            # 滑动
            d.swipe(x, y, 0, y, 30)
        else:
            Utils().raise_Exception_info('我的音乐库窗口不存在')

    # 点击音乐库中我的音乐tab
    def click_audio_mine_my_ele(self):
        ele = self.__get_audio_mine_my_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('我的音乐控件不存在')

    # 点击音乐库中的我的收藏
    def click_audio_mine_fav_ele(self):
        ele = self.__get_audio_mine_fav_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('我的收藏控件不存在')

    # 点击音乐库中的听歌识曲
    def click_audio_mine_ide_ele(self):
        ele = self.__get_audio_mine_ide_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('听歌识曲控件不存在')

    # 点击音乐库中的全部歌曲
    def click_audio_mine_all_ele(self):
        ele = self.__get_audio_mine_all_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('本地全部歌曲控件不存在')

    # 播放全部音乐中的指定歌曲
    def click_audio_mine_all_by_name(self, music_name):
        ele = self.__get_audio_mine_all_listview_ele()
        if ele.wait.exists():
            if ele.scroll.vert.to(text = music_name):
                d(text = music_name).click.wait()
            #     1s时间等待音乐播放界面刷新
                time.sleep(1)
            else:
                Utils().raise_Exception_info('指定音乐《' + music_name + '》不存在')
        else:
            Utils().raise_Exception_info('音乐列表控件不存在')

    # 获取USB音乐条数
    def get_audio_mine_usb_cnt_txt(self):
        ele = self.__get_audio_mine_usb_cnt_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('USB音乐条数控件不存在')

    # 点击USB音乐播放控件
    def click_audio_mine_usb_play_ele(self):
        ele = self.__get_audio_mine_usb_play_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('USB音乐播放控件不存在')
    # 点击音乐收藏控件
    def click_audio_fav_ele(self):
        ele = self.__get_audio_fav_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('音乐收藏控件不存在')

    # 点击听Ta的歌曲控件
    def click_audio_list_ta_ele(self):
        ele = self.__get_audio_list_ta_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('听Ta的歌控件不存在')
    # 点击相似歌曲
    def click_audio_list_similar_ele(self):
        ele = self.__get_audio_list_similar_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('相似歌曲控件不存在')

    # 随机播放酷我音乐专辑
    def click_audio_kuwo_name_random_ele(self):
        ele = self.__get_audio_kuwo_name_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('酷我专辑不存在')
        '''
        if len(ele) > 0:
            idx = random.randint(0,len(ele)-1)
            ele[idx].click.wait()
        else:
            Utils().raise_Exception_info('酷我专辑为空')
            '''
    # 随机播放今日歌单音乐
    def click_audio_smart_name_random_ele(self):
        ele = self.__get_audio_smart_name_ele()
        ele_artist = self.__get_audio_smart_artist_ele()
        if len(ele) > 0:
            idx = random.randint(0, len(ele) - 1)
            # 存放到全局变量中
            name_txt = ele[idx].text.strip()
            artist_txt = ele_artist[idx].text.strip()
            Utils().set_context_map(name_txt, artist_txt)

            ele[idx].click.wait()
            # 返回音乐名称
            return name_txt
        else:
            Utils().raise_Exception_info('今日歌单为空')

    # 点击清空搜索框控件
    def click_audio_search_clear_ele(self):
        ele = self.__get_audio_search_clear_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('清空搜索框控件不存在')

    # 输入关键词搜索音乐
    def input_audio_search_keyword_ele(self, text):
        # 先清空搜索框
        self.click_audio_search_clear_ele()
        time.sleep(1)
        #
        ele = self.__get_audio_search_keyword_ele()
        if ele.wait.exists():
            ele.set_text(Utils().unicode_input(text))
        else:
            Utils().raise_Exception_info('搜索框控件不存在')

    # 点击搜索界面的取消控件
    def click_audio_search_cancel_ele(self):
        ele = self.__get_audio_search_cancel_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('取消控件不存在')

    # 根据歌手播放搜索结果
    def click_audio_search_result_by_artist(self, artist):
        ele = self.__get_audio_search_listview_ele()
        music_search = self.__get_audio_search_name_ele()
        if music_search.wait.exists(timeout = Utils().LONG_TIME_OUT):


            if ele.scroll.vert.to(text = artist):
                d(text = artist).click.wait()
            # 1s时间音乐播放界面刷新
                time.sleep(1)
            else:
                Utils().raise_Exception_info('指定歌手名字不存在')
        else:
            Utils().raise_Exception_info('在线音乐搜索结果为空，可能是搜索时间过长')

    # 根据音乐名字播放搜索结果
    def click_audio_search_result_by_name(self, name):
        ele = self.__get_audio_search_listview_ele()
        music_search = self.__get_audio_search_name_ele()
        if music_search.wait.exists(timeout=Utils().LONG_TIME_OUT):
            if ele.scroll.vert.to(text=name):
                d(text=name).click.wait()
                # 1s时间音乐播放界面刷新
                time.sleep(1)
            else:
                Utils().raise_Exception_info('指定音乐不存在')
        else:
            Utils().raise_Exception_info('在线音乐搜索结果为空，可能是搜索时间过长')
    # 获取搜索框内容
    def get_audio_search_keyword_txt(self):
        ele = self.__get_audio_search_keyword_ele()
        if ele.wait.exists():
            return ele.text.strip()
        else:
            Utils().raise_Exception_info('音乐搜索框控件不存在')


    # 验证当前界面为音乐主界面
    def chk_audio_is_home_page(self):
        ele = self.__get_audio_home_ele()
        if not ele.wait.exists():
            Utils().raise_Exception_info('当前界面不是音乐主界面')
    # 滚动listview
    def scroll_audio_list_ta_listview_forward(self):
        ele = self.__get_audio_list_ta_listview_ele()
        if ele.wait.exists():
            ele.scroll.vert.forward()
        else:
            Utils().raise_Exception_info('听ta的歌，列表控件不存在')
    # 根据歌手名字验证听ta的歌列表是否正确
    def chk_audio_list_ta_listview_by_artist(self, chk_artist):
        """
        滚动两屏 如果一致则通过，如果没有指定演唱者的歌曲 失败
        :return:
        """
        ele_artist = self.__get_audio_list_ta_listview_artist_ele()
        ele_artist.wait.exists(timeout = Utils().LONG_TIME_OUT)
        if len(ele_artist) > 0:
            for e in ele_artist:
                # 判断不存在就报错
                if not str(e.text.strip()).__contains__(chk_artist):
                    Utils().raise_Exception_info('听ta的歌列表校验失败，期望歌手为: ' + chk_artist + ', 实际歌手为: ' + e.text.strip())

        else:
            Utils().raise_Exception_info('听ta的歌列表为空')
    # 从音乐界面返回到launcher界面
    def back_to_launcher(self):
        # 判断是否在酷我音乐界面
        # package_name = d.info['currentPackageName']
        # if package_name == 'cn.kuwo.kwmusiccar':
        #     self.back_from_kuwo()
        # 判断是否在我的音乐库或音乐列表界面或者酷我，今日歌单
        if self.__get_audio_mine_drawer_ele().exists:
            self.hide_audio_mine_drawer()
            self.click_audio_home_ele()
        #     判断是否在音乐搜索界面
        elif self.__get_audio_search_cancel_ele().exists:
            self.click_audio_search_cancel_ele()
            self.click_audio_home_ele()
        else:
            self.click_audio_home_ele()

    # 点击播放蓝牙音乐
    def click_audio_mine_bluetooth_play_ele(self):
        ele = self.__get_audio_mine_bluetooth_play_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('蓝牙音乐播放控件不存在')

    # 点击听歌识曲返回控件
    def click_audio_back_to_radio_ele(self):
        ele = self.__get_audio_back_to_radio_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('听歌识曲返回控件不存在')

    #验证U盘已经拔出
    def chk_audio_usb_gone(self):
        ele = d(text = '请接入U盘')
        time.sleep(Utils().TIME_OUT)
        return ele.exists

    def back_from_kuwo(self):
        # package_name = d.info['currentPackageName']
        back = Utils().get_ele_by_resourceId('cn.kuwo.kwmusiccar:id/layoutPlayControlPanel')
        if back.wait.exists():
            back.click.wait()
        else:
            Utils().raise_Exception_info('从酷我返回到音乐控件不存在')


# print(Audio().get_audio_name_playing_txt())







