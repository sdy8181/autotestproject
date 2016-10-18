# -*- coding: utf-8 -*-
import os
import time
import math
import platform
import operator
import subprocess
from PIL import Image
from functools import reduce
from uiautomator import Device,Adb
from configparser import ConfigParser

#DEVICE_IP = "192.168.95.2:5578"


class HT:

    TIME_OUT = 5000
    LONG_TIME_OUT = 30000

    # 上下文 用于存放数据
    global context_map
    context_map = {}

    def initWifiADB(self):

        '''
            通过wifi方式建立adb连接，避免了通过usb连接adb繁琐的设置以及无法使用user版本
             环境：PC与车机同一个局域网
        adb.exe需要同一个进程调用，不然会被打断，所以统一用uiautomator方法初始化
        '''

        adb = Adb()
        try:
            line = adb.raw_cmd("connect", self.get_conf_value("deviceIPaddress").strip()+":5578").communicate()[0].decode("utf-8")
            if "connected to" in line:
                return True
            else:
                raise Exception('Connect to adb fail via wifi ')
        except IOError as e:
            return False



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
    def get_phone_obj(self):
        phone_serialNum = self.get_conf_value('phoneSerial')

        return Device(phone_serialNum)

    # 获取设备操作实例
    def get_device_obj(self):
        serial_number = self.get_conf_value('deviceSerial')
        #判断设备是否连接
        if self.check_is_connected(serial_number):
            return Device(serial_number)
        else:
            raise Exception('车机没有连接PC')

    # 输入中文 采用utf7ime 调用jar包实现中文输入
    def unicode_input(self, text):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))

        jar_path = os.path.join(os.path.dirname(CURR_DIR), 'support', 'utf7ime4py.jar')
        unicode_str = os.popen('java -jar ' + jar_path + ' ' + text).read()
        return unicode_str

    # 获取当前的放音通道
    def get_cur_tinymix(self):
        result = os.popen('adb -s ' + self.get_conf_value('deviceSerial') + ' shell tinymix 0').read()
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


     # 获取usb音乐
    def get_usb_music(self):
        usbMusic_value = self.get_conf_value('usbMusic')
        usb_music = tuple(usbMusic_value.split(','))
        return usb_music

    # 校验设备是否连接，没有链接抛出异常
    def check_is_connected(self, serial_num):

        command = 'adb devices'

        res = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.readlines()
        for s in res:
            s = s.decode().strip()
            if serial_num in s:
                return True
        return self.initWifiADB()


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


ht = HT()

if __name__ == '__main__':
    print(ht.LONG_TIME_OUT)
