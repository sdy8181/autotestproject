# -*- coding: UTF-8 -*-
from support.global_vars import d, ver_flag
from utils.utils import Utils


class Video:

    def __init__(self):
        # 新旧版本的pkgname判断
        global pkg_name
        if ver_flag:
            pkg_name = "pateo.dls.app.videoui"
        else:
            pkg_name = "com.qiyi.video.auto"

    # 获取爱奇艺顶部菜单
    def get_aqy_home_top_menu(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/home_top_menu')

    # 获取右上角推荐视频文件名
    def get_aqy_recommend_right_up_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/recommend_focus_item_right_title_up')

    # 获取顶部菜单栏frame
    def get_aqy_left_menu_frame(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/id_left_menu_frame2')

    # 获取爱奇艺我的视频
    def get_aqy_menu_mine(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/menu_my_iv')

    # 获取爱奇艺我的视频的本地视频
    def get_aqy_menu_mine_local_video(self):
        return Utils().get_ele_by_text('本地视频')
    # 获取爱奇艺我的视频的我的收藏
    def get_aqy_menu_mine_fav(self):
        return Utils().get_ele_by_text('我的收藏')
    # 获取爱奇艺我的视频的播放记录
    def get_aqy_menu_mine_his(self):
        return Utils().get_ele_by_text('播放记录')

    # 获取退出爱奇艺视频播放界面
    def get_aqy_playing_back(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/player_top_back')

    # 获取正在播放的视频标题
    def get_aqy_playing_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/player_top_title')

    # 获取广告时间控件
    def get_aqy_player_top_adtime(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/player_top_adtime')

    # 获取视频播放时间
    def get_aqy_player_currentTime(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/currentTime')

    # 获取视频收藏控件
    def get_aqy_player_fav(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favor_check')

    # 获取视频播放，暂停控件
    def get_aqy_pause_btn(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/btn_pause')

    # 获取视频搜索控件
    def get_aqy_search(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/menu_search')

    # 获取视频搜索输入框
    def get_aqy_search_input(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_border_search_input')

    # 获取视频搜索取消
    def get_aqy_search_cancel(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/activity_search_title_cancel')

    # 获取清除搜索记录列表
    def get_aqy_search_his_clear(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/activity_search_clear')
    # 获取搜索记录
    def get_aqy_search_his_title(self):
        view = Utils().get_ele_by_resourceId(pkg_name + ':id/activity_search_flowlayout_history')
        if view.wait.exists():
            return Utils().get_ele_by_resourceId(pkg_name + ':id/item_search_hotandhistory_tv')
        else:
            Utils().raise_Exception_info('搜索记录视图为空')


    # 获取热门搜索记录视图
    def get_aqy_search_hot_title(self):
        view = Utils().get_ele_by_resourceId(pkg_name + ':id/activity_search_flowlayout_hot')
        if view.wait.exists():
            return Utils().get_ele_by_resourceId(pkg_name + ':id/item_search_hotandhistory_tv')
        else:
            Utils().raise_Exception_info('热门搜索记录视图为空')


    # 获取视频搜索界面的视频名
    def get_aqy_search_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/item_search_hotandhistory_tv')

    # 获取爱奇艺频道控件
    def get_aqy_menu_category(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/menu_category_iv')

    # 获取爱奇艺推荐视频频道
    def get_aqy_menu_category_recommend(self):
        return Utils().get_ele_by_text('推荐')

    # 获取爱奇艺搜索历史列表
    def get_aqy_search_result_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_result_title')

    # 获取本地视频名称
    def get_aqy_mine_local_video_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favor_title')

    # 获取播放记录视频名称
    def get_aqy_mine_his_video_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favor_title')

    # 获取我的收藏视频名称
    def get_aqy_mine_fav_video_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/favor_title')

    # 获取视频搜索列表
    def get_aqy_search_result_list(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_result_nfilm_recv')

    # 返回主界面
    def back_to_launcher(self):

        #  判断当前是否在视频播放界面
        video_back = self.get_aqy_playing_back()
        if video_back.wait.exists():
            video_back.click.wait()

        d.click(641, 641)





