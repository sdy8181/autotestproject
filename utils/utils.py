# -*- coding: UTF-8 -*-
import os
import platform
import socket
import subprocess
import time
import math

import sys
from PIL import Image
import operator
from functools import reduce
from configparser import ConfigParser

from uiautomator import Device



class Utils:

    TIME_OUT = 5000
    LONG_TIME_OUT = 30000

    # 上下文 用于存放数据
    global context_map
    context_map = {}

    # global usb_music
    # usb_music = ('拒绝再玩', '友谊之光', '无心睡眠')


    # 上下文存放数据
    def set_context_map(self, key, value):
        context_map[key] = value
    # 获取上下文中的数据
    def get_context_map(self, key):
        return context_map.get(key)
    # 清空上下文数据
    def clear_context_map(self):
        context_map.clear()

    # 获取设备操作实例
    def get_device_obj(self):
        serial_number = self.get_conf_value('deviceSerial')
        #判断设备是否连接
        if Utils().check_is_connected(serial_number):
            return Device(serial_number)
        else:
            Utils().raise_Exception_info('车机没有连接PC')

    # 获取设备操作实例
    def get_phone_obj(self):
        phone_serialNum = Utils().get_conf_value('phoneSerial')
        if Utils().check_is_connected(phone_serialNum):
            return Device(phone_serialNum)
        else:
            Utils().raise_Exception_info('手机没有连接PC')

    # 获取usb音乐
    def get_usb_music(self):
        usbMusic_value = self.get_conf_value('usbMusic')
        usb_music = tuple(usbMusic_value.split(','))
        return usb_music
    # 设置截图文件路径信息
    def __set_file_path(self, filepath):
        global file_path
        file_path = filepath

    # 获取截图文件路径信息
    def get_file_path(self):
        return file_path

    # 失败截图
    def take_screenshot(self):
        file_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        file_path = os.path.join(self.get_conf_value('logPath'), time.strftime('%Y%m%d'), 'screenshots' , file_name)
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        self.get_device_obj().screenshot(file_path)
        # self.__set_file_path('file://' + file_path)
        print(file_path)
        return file_path
    # crash监听
    def crash_handler(self):
        device = self.get_device_obj()
        print('开始检查应用是否crash')
        if device(resourceId='android:id/message').wait.exists():
            print('应用crash')
            # Utils().take_screenshot()
            device(resourceId='android:id/button1').click.wait()
            return True
        else:
            return False
        # 启动crash监听

    # def on_crash_handler(self):
    #     d.handlers.on(self.crash_handler)
    #     # d.handlers.on(self.phone_call_handler)
    #
    # # 关闭crash监听
    # def off_crash_handler(self):
    #     d.handlers.off(self.crash_handler)

    def raise_Exception_info(self, err_msg):
        png_path = self.take_screenshot()
        if self.crash_handler():
            raise Exception('应用crash，' + err_msg + '请参考截图信息: file:///' + png_path)
            # + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')
        else:
            raise Exception('用例运行失败，' + err_msg + '请参考截图信息: file:///' + png_path)
            # + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')

            # self.take_screenshot()
        # if self.crash_handler():
        #     raise Exception('应用crash，请参考截图信息: ' + self.get_file_path() + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '  对应场景日志信息 ')
        # else:
        #     raise Exception(err_msg + '，请参考截图信息: ' + self.get_file_path() + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '  对应场景日志信息 ')

    # 校验设备是否连接，没有链接抛出异常
    def check_is_connected(self, serial_num):

        command = 'adb devices'

        #res = os.popen(command).read()
        res = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.readlines()

        for s in res:
            s = s.decode().strip()
            # 跳过第一行
            # if s.__contains__('devices'):
            #     continue

            # if s.__contains__('device'):
            #     serial = str(s.replace('device','').replace(' ','')).strip()
            #
            #     if serial.__eq__(serial_num):
            #         return True
            if serial_num in s:
                return True
        return False

    # 根据resourceID获取控件
    # 5s时间等待控件存在
    def get_ele_by_resourceId(self, resource_id):
        ele = self.get_device_obj()(resourceId= resource_id)
        ele.wait.exists()
        return ele

    # 根据resourceID获取控件
    # 5s时间等待控件存在
    def get_ele_by_text(self, txt):
        ele = self.get_device_obj()(text=txt)
        ele.wait.exists()
        return ele
    # 输入中文 采用utf7ime 调用jar包实现中文输入
    def unicode_input(self, text):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))

        jar_path = os.path.join(os.path.dirname(CURR_DIR), 'support', 'utf7ime4py.jar')
        unicode_str = os.popen('java -jar ' + jar_path + ' ' + text).read()
        return unicode_str
    # 获取当前的放音通道
    def get_cur_tinymix(self):
        result = os.popen('adb -s ' + Utils().get_conf_value('deviceSerial') + ' shell tinymix 0').read()
        print('查询的tinymix的结果为: ' + result)
        tmp = str(result).split('>')[1]
        idx = tmp.index('ASP',len('ASP'), len(tmp) - 1)
        ret = tmp[:idx].strip()
        print('获取当前的放音通道为: ' + ret)
        return ret

    # 播放音乐
    def play_voice(self, voice_name):
        cmd = self.get_conf_value('player') + ' ' + os.path.join(self.get_conf_value('voiceDir'), voice_name)
        os.popen(cmd)

    # 根据key获取配置文件的值
    def get_conf_value(self, key):

        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        ini_path = os.path.join(os.path.dirname(CURR_DIR), 'support', 'config.ini')

        cf = ConfigParser()
        cf.read(ini_path)
        ret_val = cf.get('baseconf', key)
        # print('获取配置项《' + key + '》的值为: ' + ret_val)
        return str(ret_val)

    # 连接蓝牙
    def connect_bluetooth(self):
        os.popen('adb -s ' + self.get_conf_value('deviceSerial') + ' shell am instrument -w -r -e class com.pateo.attools.ApplicationTest#testBlue com.pateo.attools.test/android.test.InstrumentationTestRunner')

    #返回是否为老版本
    # true:为老版本
    # false: 为新版本
    def is_old_ver(self):
        version = self.get_conf_value("version")
        return str(version).__eq__("1.0")
    # 记录运行top信息
    def get_top_info_to_file(self, sce_name):
        device_num = self.get_conf_value("deviceSerial")
        log_dir = self.get_conf_value("logPath")

        file = open(os.path.join(log_dir, 'calc_cpu_info' + time.strftime('%Y%m%d') + '.log'), 'a+')
        filewarn = open(os.path.join(log_dir, 'calc_cpu_warn_info' + time.strftime('%Y%m%d') + '.log'), 'a+')
        file.write('=' * 20 + sce_name + '=' * 20 + '\n')
        filewarn.write('=' * 20 + sce_name + '=' * 20 + '\n')
        time.sleep(20)
        ret = os.popen('adb -s ' + device_num + ' shell top -m 5 -n 1').read().split('\n')
        for r in ret:
            if len(r) == 0:
                continue

            if 'User' not in r:
                file.write(r + '\n')
                if 'PID' not in r:
                    if int(r.split()[2][:-1]) > 10:
                        filewarn.write(r + '\n')
                else:
                    filewarn.write(r + '\n')

        filewarn.close()
        file.close()

    # 记录日志信息
    def logcat_to_file(self, sce_name):
        device_num = self.get_conf_value("deviceSerial")
        # log_path = os.path.join(self.get_conf_value('logPath'), time.strftime('%Y%m%d'), sce_name + '.log')
        log_path = os.path.join(self.get_conf_value('logPath'), sce_name + '.log')
        log_dir = os.path.dirname(log_path)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_cmd = 'adb -s ' + device_num + ' logcat'

        # 开始记录日志
        os.popen(log_cmd + ' -c ')

        file_logcat = open(log_path, 'w', encoding='utf-8')
        if sys.platform == 'linux':
            p_logcat = subprocess.Popen(log_cmd + ' *:D', stdout=file_logcat, stderr=subprocess.PIPE, shell=True)
        else:
            p_logcat = subprocess.Popen(log_cmd + ' *:D', stdout=file_logcat, stderr=subprocess.PIPE)

        self.set_context_map('file_logcat', file_logcat)
        self.set_context_map('p_logcat', p_logcat)

    # 发送记录日志操作
    def send_logcat_flag(self, status):
        # 杀掉logcat进程
        if self.get_context_map('file_logcat'):
            print('关闭文件')
            self.get_context_map('file_logcat').close()

        if sys.platform == 'linux':
            print('杀掉进程')
            # self.get_context_map('p_logcat').terminate()
            subprocess.call('kill -9 ' + str(self.get_context_map('p_logcat').pid), shell=True)
            ret = subprocess.Popen('ps -ef | grep logcat', stdout=subprocess.PIPE, shell=True).stdout.readlines()
            for r in ret:
                r = r.decode().strip()
                while '  ' in r:
                    r = r.replace('  ', ' ')
                rlist = r.split(' ')
                pid = rlist[1]
                try:
                    subprocess.call('kill -9 ' + pid, shell=True)
                except:
                    pass
        else:
            if self.get_context_map('p_logcat'):
                print('杀掉进程')
                self.get_context_map('p_logcat').terminate()
        #     print('杀掉进程')
            # subprocess.call('taskkill /F /pid ' + str(self.get_context_map('p_logcat').pid), shell=True)
            # self.get_context_map('p_logcat').terminate()
            # ret = subprocess.Popen('tasklist -V | findstr adb', stdout=subprocess.PIPE, shell=True).stdout.readlines()
            # for r in ret:
            #     r = r.decode('unicode_escape').strip()
            #     while '  ' in r:
            #         r = r.replace('  ', ' ')
            #     rlist = r.split(' ')
            #     pid = rlist[1]
            #     try:
            #         if rlist[6] == 'Unknown':
            #             print(rlist[1])
            #             subprocess.call('taskkill /T /F /pid ' + pid, shell=True)
            #     except:
            #         pass

    # 获取wifi连接状态
    # true 连接
    # false 没有连接

    def get_wifi_conn_status(self):

        device_serial = self.get_conf_value('deviceSerial')

        if platform.system() == 'Linux':
            ret = os.popen('adb -s ' + device_serial + ' shell netcfg | grep wlan0').read()
        else:
            ret = os.popen('adb -s ' + device_serial + ' shell netcfg | findstr wlan0').read()

        while ret.__contains__('  '):
            ret = ret.replace('  ', ' ')
        retList = ret.split(' ')
        print(retList[2])
        if retList[2].__contains__('0.0.0.0'):
            print('没有连接wifi')
            return False
        else:
            print('已经连接wifi')
            return True

    # 获取图片比对数据结果
    def get_image_diff_data(self, image1, image2):
        # get init image
        img1 = Image.open(image1)
        img2 = Image.open(image2)

        h1 = img1.histogram()
        h2 = img2.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        return result

# print(Utils().get_conf_value('player'))
#
# >>> path = os.getcwd()
# >>> print(path)
# C:\Users\guangqian
# >>> path1 = os.path.dirname(path)
# >>> print(path1)
# C:\Users
# >>> path2 = os.path.join(path1, 'support')
# >>> print(path2)
# C:\Users\support
# >>>
