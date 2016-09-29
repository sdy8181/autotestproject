# -*- coding: UTF-8 -*-
import os, time
from datetime import datetime

from uiautomator import Device

device_serial = 'P008000150000127'

d = Device(device_serial)

def calc_sys_start_time():
    flag = False
    os.system('adb reboot')
    start_time = None

    ret = os.popen('adb devices').read()
    while not flag:
      for l in ret.split('\n'):
          if l.__contains__(device_serial):
              flag = True
              start_time = datetime.utcnow()
              break
          else:
              ret = os.popen('adb devices').read()

    # print(time.time())

    ele = d(textContains = '你好，语音助理')
    if ele.wait.exists(timeout = 180000):
        end_time = datetime.utcnow()

    time = end_time - start_time


    print('应用启动时间为: ' + str(start_time))
    print('应用启动成功加载完主界面时间为: ' + str(end_time))
    print('中间所耗时为: ' + str(time))

def back_to_menue():
    package = d.info['currentPackageName']
    if package.__eq__('com.qinggan.app.video'):
        ele = d(resourceId = 'com.qinggan.app.video:drawable/net_video_menu_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.app.naviapp'):
        ele = d(resourceId='com.pateonavi.naviapp:id/go_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.app.music'):
        ele = d(resourceId='com.qinggan.app.music:drawable/menu_selector_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.app.radio'):
        ele = d(resourceId='com.qinggan.app.radio:drawable/selector_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.bluetoothphone'):
        ele = d(resourceId='com.qinggan.bluetoothphone:drawable/menu_home_selector')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.qgservice'):
        ele = d(resourceId='com.qinggan.qgservice:drawable/selector_button_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('com.qinggan.app.carmodule'):
        ele = d(resourceId='com.qinggan.app.carmodule:drawable/menu_home_selector')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.audioui'):
        ele = d(resourceId='pateo.dls.audioui:drawable/menu_selector_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.app.radio'):
        ele = d(resourceId='pateo.dls.app.radio:drawable/selector_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.app.videoui'):
        ele = d(resourceId='pateo.dls.app.videoui:drawable/net_video_menu_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.carmodule.ui'):
        ele = d(resourceId='pateo.dls.carmodule.ui:drawable/menu_home_selector')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.serviceui'):
        ele = d(resourceId='pateo.dls.serviceui:drawable/selector_button_home')
        if ele.wait.exists():
            ele.click.wait()
    elif package.__eq__('pateo.dls.bluetooth'):
        ele = d(resourceId='pateo.dls.bluetooth:drawable/menu_home_selector')
        if ele.wait.exists():
            ele.click.wait()

    ele = d(textContains = '唤醒我')
    if ele.wait.exists():
        ele = d(resourceId='com.qinggan.app.launcher:id/all_app_home_button')
        # ele = d(resourceId='pateo.dls.app.launcher:id/all_app_home_button')

        if ele.wait.exists():
            ele.click.wait()

# music, radio, video,navi
def calc_app_start_time(app_name):
    time.sleep(30)
    back_to_menue()
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    if app_name.__eq__('music'):
        e = d(text = '音乐')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId = 'com.qinggan.app.music:id/img_next')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' %(str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('radio'):
        e = d(text='电台')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='com.qinggan.app.radio:id/next')
        if e_chk.wait.exists(timeout = 5000):
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('video'):
        e = d(text='视频')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='com.qinggan.app.video:drawable/net_video_menu_search')
        if e_chk.wait.exists(timeout = 5000):
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('navi'):
        pass
    elif app_name.__eq__('car'):
        e = d(text='车辆')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='com.qinggan.app.carmodule:id/car_home_bg_click')
        if e_chk.wait.exists(timeout = 5000):
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('service'):
        e = d(text='服务')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='com.qinggan.qgservice:id/button_call')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('phone'):
        e = d(text='电话')
        if e.wait.exists(timeout = 5000):
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='com.qinggan.bluetoothphone:id/callout_btn_call')
        if e_chk.wait.exists(timeout = 5000):
            end_time = datetime.utcnow()
        t = end_time - start_time
        print(app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    else:
        raise ('启动应用名不存在')

def calc_app_start_time_for_1(app_name):
    time.sleep(30)
    back_to_menue()
    start_time = datetime.utcnow()
    end_time = datetime.utcnow()
    if app_name.__eq__('music'):
        e = d(text='音乐')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.audioui:id/next')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('radio'):
        e = d(text='电台')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.app.radio:id/next')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('video'):
        e = d(text='视频')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.app.videoui:drawable/net_video_menu_search')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('navi'):
        pass
    elif app_name.__eq__('car'):
        e = d(text='车辆')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.carmodule.ui:id/car_home_bg_click')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('service'):
        e = d(text='服务')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.serviceui:id/button_call')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    elif app_name.__eq__('phone'):
        e = d(text='电话')
        if e.wait.exists():
            e.click()
            start_time = datetime.utcnow()
        e_chk = d(resourceId='pateo.dls.bluetooth:id/callout_btn_call')
        if e_chk.wait.exists():
            end_time = datetime.utcnow()
        t = end_time - start_time
        print('OS1.0 ' + app_name + '应用的启动时间开始时间为: %s, 结束时间为: %s, 消耗总时间为: %s' % (str(start_time), str(end_time), str(t)))
    else:
        raise ('启动应用名不存在')


# calc_sys_start_time()

# calc_app_start_time_for_1('music')
# calc_app_start_time_for_1('radio')
# calc_app_start_time_for_1('video')
# calc_app_start_time_for_1('service')
# calc_app_start_time_for_1('car')
# calc_app_start_time_for_1('phone')

calc_app_start_time('music')
# for i in range(10):
#     calc_app_start_time('radio')
calc_app_start_time('radio')
calc_app_start_time('video')
calc_app_start_time('service')
calc_app_start_time('car')
calc_app_start_time('phone')

# calc_app_start_time('navi')
