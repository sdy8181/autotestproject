# -*- coding: UTF-8 -*-
from behave import when

from elements.common import Common
from elements.launcher import Launcher
from elements.systemsetting import SysSetting
from utils.helpTools import ht

@when(u'< 断开蓝牙连接')
def step_impl(context):
    Common().back_to_launcher()
    Launcher().click_system_setting_ele()
    SysSetting().click_syssetting_menu_net_ele()
    SysSetting().click_syssetting_bluetooth_ele()
    SysSetting().cancel_syssetting_special_bluetooth(ht.get_conf_value('phoneBluetoothName'))

@when(u'< 连接蓝牙')
def step_impl(context):
    Common().back_to_launcher()
    Launcher().click_system_setting_ele()
    SysSetting().click_syssetting_menu_net_ele()
    SysSetting().click_syssetting_bluetooth_ele()
    SysSetting().connect_syssetting_special_bluetooth(ht.get_conf_value('phoneBluetoothName'))