# -*- coding: UTF-8 -*-
import os
import subprocess
import threading
import socket
import time

import sys

from elements.common import Common
from utils.helpTools import ht
from utils.uiTools import uit


# 前处理检查设备是否连接
def before_all(context):
    print('校验设备是否连接')
    serialNum = ht.get_conf_value('deviceSerial')
    if not ht.check_is_connected(serialNum):
        uit.raise_Exception_info('车机没有连接请检查')

    print('设备已经连接')
    #安装utf7ime输入法并设置为默认输入法
    print('开始设置输入法')
    try:
        utf7apk_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'support', 'Utf7Ime.apk')
        subprocess.call('adb -s ' + serialNum + 'install -r ' + utf7apk_path, shell=True)
        # 设置输入法
        subprocess.call('adb -s ' + serialNum + ' shell settings put secure default_input_method jp.jun_nama.test.utf7ime/.Utf7ImeService', shell=True)
        print('输入法设置完成')
    except Exception as e:
        print(e)



    # 清空logcat日志记录
    log_path = ht.get_conf_value('logPath')

    if sys.platform == 'linux':
        subprocess.call('rm -rf ' + log_path, shell=True)
    else:
        subprocess.call('rd /q/s ' + log_path, shell=True)

# 还原设置
def after_all(context):
    # 恢复输入法
    try:
        print('还原输入法')
        serialNum = ht.get_conf_value('deviceSerial')
        subprocess.call('adb -s ' + serialNum + ' shell settings put secure default_input_method com.android.inputmethod.qingganime/.QingganIME', shell=True)
        print('还原输入法完成')
    except Exception as e:
        print('还原输入法失败')
        print(e)

# 场景前处理
# 每个场景之前确保设备在主界面
def before_scenario(context, scenario):
    sce_name = scenario.name
    print('=' * 60)
    print('场景《' + sce_name + '》开始执行！')
    print('执行场景前处理，回到主界面')
    try:
        Common().back_to_launcher()
    except Exception as e:
        if uit.crash_handler():
            print('回到主界面有CRASH')
            print(e)
        else:
            print('回到主界面异常输出：')
            print(e)
    print('清空上下文数据')
    ht.clear_context_map()
    print('场景前处理执行结束')


# 场景后处理
def after_scenario(context, scenario):
    # 获取场景名称
    sce_name = scenario.name
    # 发送消息到客户端执行结束一条用例
    try:
        cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli.connect(('localhost', 8899))
        cli.send(sce_name.encode('utf-8'))
        time.sleep(2)
    except:
        pass
    finally:
        cli.close()

    print('场景《' + sce_name + '》执行结束！')
    print('=' * 60)
