# -*- coding: UTF-8 -*-
import os
import platform
import time

import serial

from actions.audio import Audio
from actions.gesture import Gesture
from actions.launcher import Launcher
from actions.navi import Navi
from actions.qplay import Qplay
from actions.radio import Radio
from actions.systemsetting import SysSetting
from actions.video import Video
from support.global_vars import ver_flag, d
from utils.utils import Utils



class Common:

    # 回到主界面
    def back_to_launcher(self):
        # 获取当前包名
        package_name = d.info['currentPackageName']
        if ver_flag:
            while package_name != 'pateo.dls.app.launcher':
                if 'pateo.dls.carmodule.ui'.__eq__(package_name):
                    pass
                elif 'pateo.dls.serviceui'.__eq__(package_name):
                    pass
                elif 'com.qiyi.video.auto'.__eq__(package_name):
                    Video().back_to_launcher()
                elif 'com.pateonavi.naviapp'.__eq__(package_name):
                    Navi().back_to_launcher()
                elif 'pateo.dls.audioui'.__eq__(package_name):
                    Audio().back_to_launcher()
                elif 'cn.kuwo.kwmusiccar'.__eq__(package_name):
                    Audio().back_from_kuwo()
                elif 'pateo.dls.app.radio'.__eq__(package_name):
                    Radio().back_to_launcher()
                elif 'pateo.dls.qplay'.__eq__(package_name):
                    Qplay().back_to_launcher()
                elif 'pateo.dls.app.SystemSettingUI'.__eq__(package_name):
                    SysSetting().back_to_launcher()
                elif 'pateo.dls.app.ivokaUI'.__eq__(package_name):
                    time.sleep(10)
                elif 'pateo.dls.gesture'.__eq__(package_name):
                    Gesture().back_to_launcher()
                else:
                # Utils().raise_Exception_info('当前包名获取异常')
                    if Utils().crash_handler():
                        print('回到主界面有CRASH')
                package_name = d.info['currentPackageName']
        else:

            while package_name != 'com.qinggan.app.launcher':
                if 'com.qinggan.app.carmodule.ui'.__eq__(package_name):
                    pass
                elif 'com.qinggan.app.serviceui'.__eq__(package_name):
                    pass
                elif 'com.qiyi.video.auto'.__eq__(package_name):
                    Video().back_to_launcher()
                elif 'com.pateonavi.naviapp'.__eq__(package_name):
                    Navi().back_to_launcher()
                elif 'com.qinggan.app.music'.__eq__(package_name):
                    Audio().back_to_launcher()
                elif 'cn.kuwo.kwmusiccar'.__eq__(package_name):
                    Audio().back_from_kuwo()
                elif 'com.qinggan.app.radio'.__eq__(package_name):
                    Radio().back_to_launcher()
                elif 'com.qinggan.app.qplay'.__eq__(package_name):
                    Qplay().back_to_launcher()
                elif 'com.qinggan.app.setting'.__eq__(package_name):
                    SysSetting().back_to_launcher()
                elif 'com.qinggan.app.ivokaUI'.__eq__(package_name):
                    time.sleep(10)
                elif 'com.qinggan.app.gesture'.__eq__(package_name):
                    Gesture().back_to_launcher()
                else:
                    # Utils().raise_Exception_info('当前包名获取异常')
                    if Utils().crash_handler():
                        print('回到主界面有CRASH')
                package_name = d.info['currentPackageName']
        # 在主界面
        Launcher().back_to_main()
        # 升级后取消修复
        d.click(1150, 80)
        time.sleep(2)

    # 播放语音文件唤醒应用
    def ivoka_start_app(self, voice_name):
        ivoka_flag = False

        Utils().play_voice('你好语音助理.m4a')
        ele = d(text = '你好，请说')
        ele1 = d(text = '没听清，请再说一次')
        loop = 0
        while (loop <= 3) and (not ivoka_flag):
            if ele.wait.exists(timeout = 8000):
                Utils().play_voice(voice_name)
                ivoka_flag = True

                if ele1.wait.exists(timeout = 8000):
                    Utils().play_voice(voice_name)
                    ivoka_flag = True
            else:
                Utils().play_voice('你好语音助理.m4a')
                loop += 1

        if not ivoka_flag:
            Utils().raise_Exception_info('ivoka唤醒失败')

    # 获取media音量
    def get_media_volume(self):
        if platform.system() == 'Linux':
            cmd = '''adb  -s ''' + Utils().get_conf_value('deviceSerial')  + ''' shell "echo 'select * from system;'|sqlite3 /data/data/com.android.providers.settings/databases/settings.db" | grep "volume_music_speaker"'''
        else:
            cmd = '''adb  -s ''' + Utils().get_conf_value('deviceSerial')  + ''' shell "echo 'select * from system;'|sqlite3 /data/data/com.android.providers.settings/databases/settings.db" | findstr "volume_music_speaker"'''
        volume_ret = os.popen(cmd).read().strip()
        volume_value = volume_ret.split('|')[2].strip()
        print(volume_value)
        return volume_value

    #返回当前应用名称
    def get_current_package_name(self):
        package_name = d.info['currentPackageName']
        if ver_flag:
            if 'pateo.dls.carmodule.ui'.__eq__(package_name):
                return '车辆'
            elif 'pateo.dls.serviceui'.__eq__(package_name):
                return '服务'
            elif 'com.qiyi.video.auto'.__eq__(package_name):
                return '视频'
            elif 'com.pateonavi.naviapp'.__eq__(package_name):
                return '导航'
            elif 'pateo.dls.audioui'.__eq__(package_name) or 'cn.kuwo.kwmusiccar'.__eq__(package_name):
                return '音乐'
            elif 'pateo.dls.app.radio'.__eq__(package_name):
                return '电台'
            elif 'pateo.dls.qplay'.__eq__(package_name):
                return 'QPlay'
            elif 'pateo.dls.app.SystemSettingUI'.__eq__(package_name):
                return '设置'
            elif 'pateo.dls.app.ivokaUI'.__eq__(package_name):
                return 'ivoka'
            else:
                return '主界面'
        else:
            if 'com.qinggan.app.carmodule.ui'.__eq__(package_name):
                return '车辆'
            elif 'com.qinggan.app.serviceui'.__eq__(package_name):
                return '服务'
            elif 'com.qiyi.video.auto'.__eq__(package_name):
                return '视频'
            elif 'com.pateonavi.naviapp'.__eq__(package_name):
                return '导航'
            elif 'com.qinggan.app.music'.__eq__(package_name) or 'cn.kuwo.kwmusiccar'.__eq__(package_name):
                return '音乐'
            elif 'com.qinggan.app.radio'.__eq__(package_name):
                return '电台'
            elif 'com.qinggan.app.qplay'.__eq__(package_name):
                return 'QPlay'
            elif 'com.qinggan.app.setting'.__eq__(package_name):
                return '设置'
            elif 'com.qinggan.app.ivokaUI'.__eq__(package_name):
                return 'ivoka'
            elif 'com.qinggan.app.gesture'.__eq__(package_name):
                Gesture().back_to_launcher()
            else:
                return '主界面'



    def phone_call_handler(self, device):
        print('开始监听咯。。。。')
        if device(resourceId='com.android.incallui:id/endButton').exists:
            print('发现在打电话。。。')
            Utils().take_screenshot()
            # d(text='拒绝').click()
            device(resourceId='com.android.incallui:id/endButton').click()
            Utils().raise_Exception_info('Crash is occurred')
        else:
            print('毛都没有。。。')
        return True


    #模拟拔出U盘
    def controlPoweroff(self):
        s = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None)
        poweroff = '005A560005010000B7'.decode("hex")
        if not s.isOpen():
            s.open()
        s.write(poweroff)
        s.close()
    # 模拟插上U盘
    def controlPoweron(self):
        s = serial.Serial(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None)
        poweron = '005A560005010000B6'.decode("hex")
        if not s.isOpen():
            s.open()
        s.write(poweron)
        s.close()

    #连接指定无线网
    def connect_special_wifi(self, ssid, pwd):
        Common().back_to_launcher()
        Launcher().click_system_setting_ele()
        SysSetting().click_syssetting_menu_net_ele()
        ele = d(resourceId = 'com.qinggan.app.setting:id/wifi_header')
        ele1 = ele.child(text = 'WIFI', resourceId = 'com.qinggan.app.setting:id/wifi_title')

        if not ele1.wait.exists():
            d.click(1150, 80)
            SysSetting().click_syssetting_menu_net_ele()
            # flag_ele = ele.child(resourceId = 'com.qinggan.app.setting:id/wifi_switcher')
            # flag_ele.click()

        ele.click.wait()
        scan_ele = d(text='重新扫描', resourceId = 'com.qinggan.app.setting:id/btn_wifi_scan')
        while not scan_ele.wait.exists():
            ele.click.wait()

        wifi_ssid_ele = d(resourceId = 'com.qinggan.app.setting:id/wifi_scanresult_name')
        if wifi_ssid_ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
            ele = d(resourceId='com.qinggan.app.setting:id/wifi_device_list')
            if not ele.scroll.vert.to(text= ssid):
                scan_ele.click()
                wifi_ssid_ele.wait.exists(timeout=Utils().LONG_TIME_OUT)
                ele.scroll.vert.to(text=ssid)

            ele1 = d(text= ssid)
            con_ele = ele1.sibling(text='连接')
            if con_ele.wait.exists():
                con_ele.click()

            pwd_ele = d(resourceId = 'com.qinggan.app.setting:id/wifi_pwd_input')
            if pwd_ele.wait.exists():
              pwd_ele.set_text(pwd)
              ele1.sibling(text='连接').click()

        else:
            Utils().raise_Exception_info('刷新时间过长')


