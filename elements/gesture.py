# -*- coding: UTF-8 -*-
import os
from support.global_vars import d
from utils.helpTools import ht
from utils.uiTools import uit

class Gesture:


    # 开始倒车
    def start_back_car(self):
        # 先上电
        os.popen('adb -s ' + ht.get_conf_value('deviceSerial') + ' shell "echo 1 > /sys/devices/virtual/misc/cis_mcu/acc"')
        # 倒车
        os.popen('adb -s ' + ht.get_conf_value('deviceSerial') + ' shell "echo 1 > /sys/devices/virtual/misc/cis_mcu/reverse"')

    # 停止倒车
    def stop_back_car(self):
        # 先上电
        os.popen('adb -s ' + ht.get_conf_value('deviceSerial') + ' shell "echo 1 > /sys/devices/virtual/misc/cis_mcu/acc"')
        # 倒车
        os.popen('adb -s ' + ht.get_conf_value('deviceSerial') + ' shell "echo 0 > /sys/devices/virtual/misc/cis_mcu/reverse"')


    def back_to_launcher(self):
        self.stop_back_car()
