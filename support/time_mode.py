# -*- coding: UTF-8 -*-
import time
from uiautomator import Device

d = Device('P008000150000127')

def switch_time_mode():
    d.click(1200, 90)
    time.sleep(2)
    d.swipe(640, 0, 640, 720, 15)
    time.sleep(2)
    d.click(1200, 90)
    time.sleep(2)
#     点击进入系统设置界面
    ele = d(text = '系统')
    if ele.wait.exists():
        ele.click.wait()
    soft_ver_ele = d(text = '软件版本')
    if soft_ver_ele.wait.exists():
        soft_ver_ele.click()
        soft_ver_ele.click()
        soft_ver_ele.click()
        soft_ver_ele.click()
        soft_ver_ele.click()
    time_mode_ele = d(text = 'Time Mode 开关')
    if time_mode_ele.wait.exists():
        time_mode_ele.sibling(resourceId = 'com.qinggan.app.setting:id/time_mode_switcher').click()
def connect_wifi(ssid, pwd):

    d.swipe(640, 0, 640, 720, 15)
    time.sleep(2)
    d.click(1200, 90)
    time.sleep(2)
    ele_net = d(text='网络')
    ele_net.wait.exists()
    ele_net.click.wait()

    ele = d(resourceId='com.qinggan.app.setting:id/wifi_header')
    ele1 = ele.child(text='WIFI', resourceId='com.qinggan.app.setting:id/wifi_title')

    if not ele1.wait.exists():
        flag_ele = ele.child(resourceId='com.qinggan.app.setting:id/wifi_switcher')
        flag_ele.click()

    ele.click.wait()
    scan_ele = d(text='重新扫描', resourceId='com.qinggan.app.setting:id/btn_wifi_scan')
    while not scan_ele.wait.exists():
        ele.click.wait()

    wifi_ssid_ele = d(resourceId='com.qinggan.app.setting:id/wifi_scanresult_name')
    if wifi_ssid_ele.wait.exists(timeout=30000):
        ele = d(resourceId='com.qinggan.app.setting:id/wifi_device_list')
        if not ele.scroll.vert.to(text=ssid):
            scan_ele.click()
            wifi_ssid_ele.wait.exists(timeout=30000)
            ele.scroll.vert.to(text=ssid)

        ele1 = d(text=ssid)
        con_ele = ele1.sibling(text='连接')
        if con_ele.wait.exists():
            con_ele.click()

        pwd_ele = d(resourceId='com.qinggan.app.setting:id/wifi_pwd_input')
        if pwd_ele.wait.exists():
            pwd_ele.set_text(pwd)
            ele1.sibling(text='连接').click()
    else:
        raise ('刷新时间过长')

switch_time_mode()



