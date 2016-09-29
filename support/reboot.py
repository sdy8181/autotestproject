# -*- coding: UTF-8 -*-
import os

import time

def reboot_device():
    command = 'adb devices'

    res = os.popen(command).read()
    for s in res.split('\n'):
        # 跳过第一行
        if s.__contains__('devices'):
            continue

        if s.__contains__('device'):
            serial = str(s.replace('device', '').replace(' ', '')).strip()
            if serial.__contains__('P00'):
                cmd = 'adb -s ' + serial + ' shell reboot'
                os.popen(cmd)
                time.sleep(60)
                os.system('adb -s ' + serial + ' shell "echo 1 > /sys/devices/virtual/misc/cis_mcu/acc"')

reboot_device()