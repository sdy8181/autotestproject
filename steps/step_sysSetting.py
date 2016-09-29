# -*- coding: UTF-8 -*-
from behave import when

from actions.common import Common
from actions.launcher import Launcher
from actions.systemsetting import SysSetting
from utils.utils import Utils


@when(u'< 断开蓝牙连接')
def step_impl(context):
    Common().back_to_launcher()
    Launcher().click_system_setting_ele()
    SysSetting().click_syssetting_menu_net_ele()
    SysSetting().click_syssetting_bluetooth_ele()
    SysSetting().cancel_syssetting_special_bluetooth(Utils().get_conf_value('phoneBluetoothName'))

@when(u'< 连接蓝牙')
def step_impl(context):
    Common().back_to_launcher()
    Launcher().click_system_setting_ele()
    SysSetting().click_syssetting_menu_net_ele()
    SysSetting().click_syssetting_bluetooth_ele()
    SysSetting().connect_syssetting_special_bluetooth(Utils().get_conf_value('phoneBluetoothName'))