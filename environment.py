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
from utils.helpTools import ht
from utils.uiTools import uit


# 前处理检查设备是否连接
def before_all(context):
    print('校验设备是否连接')
    serialNum = ht.get_conf_value('deviceSerial')
    if not ht.check_is_connected(serialNum):
        uit.raise_Exception_info('车机没有连接请检查')
    print('设备已经连接')

    # 清空logcat日志记录
    log_path = ht.get_conf_value('logPath')
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
    print('场景《' + sce_name + '》执行结束！')
    print('=' * 60)
