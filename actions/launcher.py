# -*- coding: UTF-8 -*-

# from uiautomator import device as d
import time

from support.global_vars import ver_flag, d
from utils.utils import Utils


class Launcher:

    def __init__(self):

                # 新旧版本的pkgname判断
        global pkg_name
        if ver_flag:
            pkg_name = "pateo.dls.app.launcher"
        else:
            pkg_name = "com.qinggan.app.launcher"

        # # 判断新旧版本界面
        # if not pkg_name.__eq__(d.info['currentPackageName']):
        #     Utils().raise_Exception_info('当前界面和预期界面不一致')

    # 获取ivoka控件
    def __get_ivoka_ele(self):
        # return Utils().get_ele_by_resourceId(pkg_name + ':id/ivoka_icon')
        return Utils().get_ele_by_text('你好，语音助理')

    # 获取九宫格菜单
    def __get_menu_ele(self):

        return Utils().get_ele_by_resourceId(pkg_name + ':id/all_app_home_button')
        
    #  获取主界面提示语元素
    def __get_tip_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/air_quality_text')
        
    # 获取主界面温度控件
    def __get_temperature_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/temperature_icon')

    # 获取主界面时钟控件
    def __get_clock_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/ivoka_time_text')
        

    # 获取主界面的导航控件
    def __get_navi_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_nav')


    # 获取音乐控件
    def __get_audio_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_music')

    # 获取收音机控件
    def __get_radio_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_radio')

    # 获取蓝牙电话控件
    def __get_phone_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_phone')

    # 获取车辆控件
    def __get_car_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_car')

    # 获取服务控件
    def __get_service_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_service')

    # 获取视频控件
    def __get_video_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_video')

    # 获取其他控件
    def __get_others_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/app_mobile')

    # 获取其他的返回home控件
    def __get_others_home_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/home')

    # 点击Ivoka控件
    def click_ivoka_ele(self):
        if self.__get_ivoka_ele().exists:
            self.__get_ivoka_ele().click.wait()
        else:
            Utils().raise_Exception_info('Ivoka控件不存在')

    # 点击进入九宫格菜单
    def click_menu_ele(self):
        if self.__get_ivoka_ele().exists:
            if self.__get_menu_ele().exists:
                self.__get_menu_ele().click.wait()
            else:
                Utils().raise_Exception_info("进入九宫格菜单的控件不存在")
    # 从菜单界面返回
    def back_from_menu(self):
        if self.__get_menu_ele().exists:
            self.__get_menu_ele().click.wait()
        else:
            Utils().raise_Exception_info("九宫格菜单返回的控件不存在")

    # 获取主界面提示语
    def get_tip_txt(self):
        if self.__get_tip_ele().exists:
            return self.__get_tip_ele().text.strip()
        else:
            Utils().raise_Exception_info("主界面提示语控件不存在")

    # 获取温度文本信息
    def get_temperature_txt(self):
        if self.__get_temperature_ele().exists:
            return self.__get_temperature_ele().text.strip()
        else:
            Utils().raise_Exception_info('温度控件不存在')

    # 获取时钟控件
    def get_clock_txt(self):
        if self.__get_clock_ele().exists:
            return self.__get_clock_ele().text.strip()
        else:
            Utils().raise_Exception_info('时钟控件不存在')

    # 点击导航控件打开导航
    def click_navi_ele(self):
        if self.__get_navi_ele().exists:
            self.__get_navi_ele().click.wait()
            # 是否需要激活
            serial_number = d(resourceId='com.pateonavi.naviapp:id/et_serialnum')
            active_number = d(resourceId='com.pateonavi.naviapp:id/et_activenum')
            confirm = d(resourceId='com.pateonavi.naviapp:id/tv_active_confirmorcancel')
            if serial_number.exists:
                time.sleep(2)
                if len(serial_number.text) and len(active_number.text):
                    confirm.click.wait()
                    self.__get_navi_ele().click.wait()
                else:
                    Utils().raise_Exception_info('导航激活失败')
        else:
            Utils().raise_Exception_info('主界面导航控件不存在')

    # 点击音乐控件打开音乐
    def click_audio_ele(self):
        if self.__get_audio_ele().exists:
            self.__get_audio_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面音乐控件不存在')

    # 点击收音机控件打开收音机
    def click_radio_ele(self):
        if self.__get_radio_ele().exists:
            self.__get_radio_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面收音机控件不存在')

    # 点击蓝牙电话打开应用
    def click_phone_ele(self):
        if self.__get_phone_ele().exists:
            self.__get_phone_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面蓝牙电话控件不存在')

    # 点击车辆控件进入车辆
    def click_car_ele(self):
        if self.__get_car_ele().exists:
            self.__get_car_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面车辆控件不存在')

    # 点击服务控件进入服务
    def click_service_ele(self):
        if self.__get_service_ele().exists:
            self.__get_service_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面服务控件不存在')

    # 点击视频进入视频界面
    def click_video_ele(self):
        if self.__get_video_ele().exists:
            self.__get_video_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面视频控件不存在')

    # 点击其他控件进入其他界面
    def click_others_ele(self):
        if self.__get_others_ele().exists:
            self.__get_others_ele().click.wait()
        else:
            Utils().raise_Exception_info('主界面其他控件不存在')

    #

    # 点击其他界面的home
    def click_others_home_ele(self):
        if self.__get_others_home_ele().exists:
            self.__get_others_home_ele().click.wait()
        else:
            Utils().raise_Exception_info('其他界面的Home控件不存在')

    # 点击打开Qplay
    def click_qplay_ele(self):
        ele = d(text = 'QPlay')
        ele.wait.exists()
        if ele.exists:
            ele.click.wait()
        else:
            Utils().raise_Exception_info('QPlay图标不存在')
    # 打开设置并进入设置界面
    def click_system_setting_ele(self):

        d.swipe(640,0,640,720,15)
        time.sleep(2)
        d.click(1200, 90)
        time.sleep(2)

    # 主界面返回
    def back_to_main(self):
        # 从其他界面返回
        if self.__get_others_home_ele().exists:
            self.click_others_home_ele()
        # 如果在menu界面再次点击返回主界面
        if not self.__get_ivoka_ele().exists:
            self.back_from_menu()








