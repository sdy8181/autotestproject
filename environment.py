# -*- coding: UTF-8 -*-
import os
import subprocess
import threading

import time

import sys

from actions.common import Common
from actions.launcher import Launcher
from actions.navi import Navi
from actions.phone import Phone
from actions.radio import Radio
from actions.systemsetting import SysSetting
from support.global_vars import d
from utils.utils import Utils


# 前处理检查设备是否连接
def before_all(context):
    print('校验设备是否连接')
    serialNum = Utils().get_conf_value('deviceSerial')
    if not Utils().check_is_connected(serialNum):
        Utils().raise_Exception_info('车机没有连接请检查')
    print('设备已经连接')
    # phone_serialNum = Utils().get_conf_value('phoneSerial')
    # if not Utils().get_wifi_conn_status():
    #     Common().connect_special_wifi('WiFiTEST', '123454321')
    # 链接设备大于1个时候连接蓝牙
    # if Utils().check_is_connected(phone_serialNum):
    #     print('连接蓝牙设备')
        # Common().back_to_launcher()
        # Launcher().click_system_setting_ele()
        # SysSetting().click_syssetting_menu_net_ele()
        # SysSetting().click_syssetting_bluetooth_ele()
        # flag = SysSetting().connect_syssetting_special_bluetooth(Utils().get_conf_value('phoneBluetoothName'))
        # if not flag:
        #     Phone().click_pair_ele()

    # 清空logcat日志记录
    log_path = Utils().get_conf_value('logPath')
    if sys.platform == 'linux':
        subprocess.call('rm -rf ' + log_path, shell=True)
    else:
        subprocess.call('rd /q/s ' + log_path, shell=True)

# 场景前处理
# 每个场景之前确保设备在主界面
def before_scenario(context, scenario):
    sce_name = scenario.name
    print('=' * 60)
    print('场景《' + sce_name + '》开始执行！')
    # print('开始记录CPU信息 >>>')
    # global t
    # t = threading.Thread(target=Utils().get_top_info_to_file,args=(sce_name,))
    # t.setDaemon(True)
    # t.start()
    # print('开始记录logcat日志信息')
    # global t_logcat
    # t_logcat = threading.Thread(target=Utils().logcat_to_file, args=(sce_name,))
    # t_logcat.setDaemon(True)
    # t_logcat.start()
    print('执行场景前处理，回到主界面')
    try:
        Common().back_to_launcher()
    except Exception as e:
        if Utils().crash_handler():
            print('回到主界面有CRASH')
            print(e)
        else:
            print('回到主界面异常输出：')
            print(e)
    print('清空上下文数据')
    Utils().clear_context_map()
    print('场景前处理执行结束')
    # print('启动crash监听')
    # Common().on_crash_handler()


# 场景后处理
def after_scenario(context, scenario):
    # 获取场景名称
    sce_name = scenario.name
    status = scenario.status
    try:
        # t._stop()
        # t.join()
        # Utils().send_logcat_flag(status)
        print(' ')

    except Exception as e:
        print(e)
    finally:
        # t_logcat._stop()
        # t_logcat.join()

        # if not 'passed' == status:
        #     png_name = Utils().take_screenshot()
        #
        #     if Utils().crash_handler():
        #         print('应用crash，请参考截图信息: http://10.10.99.27:9000/' + time.strftime('%Y%m%d') + '/screenshots/' + png_name + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')
        #     else:
        #         print('用例运行失败，请参考截图信息: http://10.10.99.27:9000/' + time.strftime('%Y%m%d')+ '/screenshots/' + png_name + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')
        print('场景《' + sce_name + '》执行结束！')
    # if scenario.status == 'passed':
    #     Utils().del_logcat_file(sce_name + '.log')
    print('=' * 60)
    # print('场景后处理，关闭crash监听')
    # Common().off_crash_handler()
