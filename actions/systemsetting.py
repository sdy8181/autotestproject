# -*- coding: UTF-8 -*-
import time

from support.global_vars import ver_flag, d
from utils.utils import Utils


class SysSetting:

    def __init__(self):
        global pkg_name
        if ver_flag:
            pkg_name = "pateo.dls.app.SystemSettingUI"
        else:
            pkg_name = "com.qinggan.app.setting"

        # if not pkg_name + ''.__eq__(d.info['currentPackageName']):
        #     Utils().raise_Exception_info('当前界面和预期界面不一致')

    # 获取网络菜单控件
    def __get_syssetting_menu_net_ele(self):
        ele = d(text = '网络')
        ele.wait.exists()
        return ele

    #获取蓝牙列表控件
    def __get_syssetting_bluetooth_list_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/bluetooth_device_list')
    #获取系统设置退出控件
    def __get_syssetting_exit_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name + ':id/btn_exit')
    #获取系统设置返回控件
    def __get_syssetting_back_ele(self):
        return Utils().get_ele_by_resourceId(pkg_name +':id/btn_back')

    # 连接制定蓝牙
    # True: 已经连接好
    # False: 新建连接
    def connect_syssetting_special_bluetooth(self, bt_name):
        ele = self.__get_syssetting_bluetooth_list_ele()
        if ele.scroll.vert.to(text = bt_name):
            e = d(text = bt_name)
            e_btn = e.sibling(resourceId = pkg_name + ':id/bluetooth_device_btn')
            if e_btn.text.strip() == '连接':
                e_btn.click()
                self.back_to_launcher()
                return False
            else:
                self.back_to_launcher()
                return True

    #点击设置界面的网络菜单
    def click_syssetting_menu_net_ele(self):
        ele = self.__get_syssetting_menu_net_ele()
        if ele.wait.exists():
            ele.click()
        else:
            Utils().raise_Exception_info('设置界面的网络菜单不存在')
    # 点击蓝牙菜单展开
    def click_syssetting_bluetooth_ele(self):
        ele = d(textContains = '蓝牙',  resourceId = pkg_name + ':id/bluetooth_title')
        ele_scan = d(text = '重新扫描', resourceId = pkg_name + ':id/btn_bluetooth_scan')
        # 防止有修复控件挡住控件点击
        if not ele.wait.exists(timeout=5000):
            d.click(1150, 80)
            self.click_syssetting_menu_net_ele()

        if ele.wait.exists(timeout = 5000):
            ele.click.wait()
            if not ele_scan.wait.exists():
                d.click(1150, 80)
                time.sleep(2)
                ele.click()

        else:
            Utils().raise_Exception_info('蓝牙菜单展开失败')

    # 从系统设置界面返回到主界面
    def back_to_launcher(self):
        ele = self.__get_syssetting_exit_ele()
        back_ele = self.__get_syssetting_back_ele()
        if ele.exists:
            ele.click.wait()
        elif back_ele.exists:
            back_ele.click.wait()
            ele.click.wait()
        else:
            Utils().raise_Exception_info('系统设置界面的退出控件不存在')

    def cancel_syssetting_special_bluetooth(self, bt_name):
        ele = self.__get_syssetting_bluetooth_list_ele()
        if ele.scroll.vert.to(text=bt_name):
            e = d(text=bt_name)
            e_btn = e.sibling(resourceId=pkg_name + ':id/bluetooth_device_btn')
            if e_btn.text.strip() == '断开':
                e_btn.click()
                time.sleep(2)
                d.click(110, 88)

                self.back_to_launcher()
                return False
            else:
                self.back_to_launcher()
                return True