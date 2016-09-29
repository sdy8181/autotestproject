# -*- coding: UTF-8 -*-
import time

from support.global_vars import ver_flag, d
from utils.utils import Utils


class Navi:
    def __init__(self):
        # 新旧版本的pkgname判断
        global pkg_name
        if ver_flag:
            pkg_name = "com.pateonavi.naviapp"
        else:
            pkg_name = "com.pateonavi.naviapp"

        skip = Utils().get_ele_by_resourceId(pkg_name + ':id/skip')
        if skip.wait.exists():
            skip.click.wait()

    # 获取激活序列号控件
    def __get_navi_et_serialnum_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/et_serialnum')

    # 获取激活码控件
    def __get_navi_et_activenum_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/et_activenum')

    # 获取导航激活确定控件
    def __get_navi_active_confirmorcancel(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/tv_active_confirmorcancel')

    # 获取当前道路名称控件
    def get_navi_current_road_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/ll_current_name')

    # 获取指南针控件
    def get_navi_Compass_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/llCompass')

    # 获取卫星控件
    def get_navi_satellite_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/iv_satellite')

    # 获取zoom控件
    def get_navi_zoomSeekBar_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/zoomSeekBar')

    # 获取回到主界面控件
    def __get_navi_home_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/go_home')

    # 获取导航倒计时控件
    def get_navi_to_dest_time_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/tv_navigation_number')

    # 验证当前为导航主界面
    def chk_navi_is_home(self):
        ele = self.get_navi_current_road_name_ele()
        ele1 = self.__get_navi_home_ele()
        if not (ele.wait.exists() or ele1.wait.exists()):
            Utils().raise_Exception_info('当前不是导航主界面')

    # 点击返回系统主界面
    def click_navi_home_ele(self):
        ele = self.__get_navi_home_ele()
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('返回主界面控件不存在')

    # 点击当前道路控件
    def click_navi_current_road_ele(self):
        ele = self.get_navi_current_road_name_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('当前道路控件不存在')

    # 获取导航搜索控件
    def get_navi_search_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/menu_search')

    # 获取附近控件
    def get_navi_nearby_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/menu_nearby')

    # 获取城市选择控件
    def get_navi_search_city_bar_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_bar_img1')

    # 获取搜索输入框控件
    def get_navi_search_key_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_key')

    # 获取搜索取消控件
    def get_navi_search_cancel_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/search_cancel')

    # 获取查询城市列表条目信息
    def get_navi_search_city_list_item(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/list_item_tip')

    # 获取查询地址列表条目信息
    def get_navi_search_addr_list_title(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/list_item_title')

    # 获取查询结果列表list视图
    def get_navi_search_listview_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/searchtip')

    # 获取准备导航的目的地地址
    def get_navi_ready_dest_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/tv_name')

    # 获取地址收藏控件
    def get_navi_ready_dest_fav_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/iv_save')

    # 获取导航到目的地控件
    def get_navi_ready_to_dest_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/iv_dest')

    # 获取导航界面的导航指示图
    def get_navi_navipager_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/pager')

    # 获取导航界面的实时路况控件
    def get_navi_time_indicator_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/fl_tmc_indicator')

    #获取导航搜索界面的收藏控件
    def get_navi_search_fav_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/li_layout2')

    #获取附近的XXX 的标题
    def get_navi_nearby_title_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/tv_title')

    # 获取附近的XXX的列表名称
    def get_navi_nearby_name_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/tv_name')

    def get_navi_nearby_back_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/btn_back')

    # 获取查询结果条目控件
    def __get_navi_search_result_all_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/ll_result_all')

    # 根据名称获取相应的删除控件
    def get_navi_his_fav_del_ele(self, addr):
        result_ele = self.__get_navi_search_result_all_ele()
        if result_ele.wait.exists():
            for e in result_ele:
                ele = e.child(text=addr)
                if ele.wait.exists():
                    ele.long_click()
                    return e.child(resourceId=pkg_name +':id/ll_right_part')
        else:
            Utils().raise_Exception_info('列表控件不存在或者列表为空')
    # 获取返回地图控件mapback
    def __get_navi_mapback_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/iv_mapback')

    # 获取关闭附近的控件
    def __get_navi_nearby_close_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/btn_close')

    # 激活地图
    def active_navi(self):
        serial_num = self.__get_navi_et_serialnum_ele()
        active_num = self.__get_navi_et_activenum_ele()
        confirmorcancel_ele = self.__get_navi_active_confirmorcancel()

        if confirmorcancel_ele.wait.exists(timeout=Utils().LONG_TIME_OUT):
            time.sleep(5)
            if len(serial_num.text.strip()) > 0 and len(active_num.text.strip()) > 0:
                confirmorcancel_ele.click.wait()

    # 返回主界面
    def back_to_launcher(self):
        #如果在删除地址界面就点击完成以便退出(如：在收藏地址删除界面）
        ele = d(text='完成')
        if ele.wait.exists():
            ele.click()

        nearby_ele = self.__get_navi_nearby_close_ele()
        if nearby_ele.wait.exists():
            nearby_ele.click()

        # 判断是否在二级界面
        search_cancel = self.get_navi_search_cancel_ele()
        if search_cancel.wait.exists():
            search_cancel.click.wait()

        btn_back = self.get_navi_nearby_back_ele()
        if btn_back.wait.exists():
            btn_back.click.wait()

        map_back = self.__get_navi_mapback_ele()
        if map_back.wait.exists():
            map_back.click.wait()

        cr = self.get_navi_current_road_name_ele()
        navi_home = self.__get_navi_home_ele()

        if cr.wait.exists():
            cr.click()
            navi_home.click.wait()
        elif navi_home.wait.exists():
            navi_home.click.wait()
        else:  # 激活界面
            # 取消激活
            confirmorcancel_ele = self.__get_navi_active_confirmorcancel()
            if confirmorcancel_ele.wait.exists():
                confirmorcancel_ele.click.wait()

# Navi().back_to_launcher()
