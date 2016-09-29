# -*- coding: UTF-8 -*-
import os
import random
import time
from utils.utils import Utils


class Phone:

    def __init__(self):
        global dPhone
        dPhone = Utils().get_phone_obj()



    def click_pair_ele(self):
        # 唤醒屏幕
        dPhone.wakeup()
        # 打开通知栏
        dPhone.open.notification()
        #打开配对框并点击配对
        if dPhone(text='配对请求').wait.exists(timeout = Utils().LONG_TIME_OUT):
            dPhone(text='配对请求').click.wait()
            if(dPhone(text='配对').wait.exists()):
                dPhone(text='配对').click.wait()
        # 取消else 防止已经链接了就不会收到请求了
        # else:
        #     self.raise_exception_for_phone('手机端没有收到配对请求')

    # 播放QQ音乐
    def play_qq_music(self):
        # 回到主界面
        dPhone.wakeup()
        dPhone.press.home()
        dPhone.press.home()
        # 点击播放qq音乐
        qqmusic_ele = dPhone(text = 'QQ音乐')
        if qqmusic_ele.wait.exists():
            qqmusic_ele.click.wait()
        else:
            self.raise_exception_for_phone('QQ音乐图标不存在')

        #判断是否已经连接成功
        conn_txt = dPhone(text = '连接成功')
        if not conn_txt.wait.exists():

            # 判断当前音乐是在播放还是暂停，如果是暂停，点击播放按钮
            # play_ele = dPhone(resourceId = 'com.tencent.qqmusic:id/alx')
            # pause_ele = dPhone(resourceId = 'com.tencent.qqmusic:id/alv')
            if dPhone(text = '关闭').wait.exists():
                dPhone(text = '关闭').click.wait()

            ele = dPhone(className = 'android.widget.ImageView')
            size = len(ele)
            ele[size - 1].click.wait()
            music_list_ele = dPhone(className = 'android.widget.TextView')
            if music_list_ele.wait.exists():
                size = len(music_list_ele)
                music_list_ele[size - random.randint(5, 10)].click.wait()
            else:
                self.raise_exception_for_phone('qq音乐列表不存在')

            #为暂停状态，点击播放
            # if play_ele.wait.exists():
            #     play_ele.click()
            # elif not pause_ele.exists:
            #     self.raise_exception_for_phone('手机端QQ音乐界面启动不正确')

    #点击和连接的 连接控件
    def click_conn_ele(self):
        ele = dPhone(text = '连接')
        ele.wait.exists()
        if ele.exists:
            ele.click()
    #校验是否手机和Qplay链接成功
    def check_device_conn_phone(self):
        ele = dPhone(text = '连接成功')
        ele.wait.exists(timeout=Utils().LONG_TIME_OUT)
        if not ele.exists:
            self.raise_exception_for_phone('Qplay和手机连接失败')

    #判断是否同步播放指定的歌曲
    def check_is_play_specil_music(self, name):
        ele = dPhone(text = name)
        if not ele.wait.exists(timeout = Utils().LONG_TIME_OUT):
            self.raise_exception_for_phone('音乐没有同步播放')
    # 点击退出车机模式
    def click_exit_qplay(self):
        ele = dPhone(text = '退出车机模式')
        if ele.exists:
            ele.click()
        else:
            self.raise_exception_for_phone('退出车机模式控件不存在')

    def raise_exception_for_phone(self, message):
        file_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        # file_path = os.path.join(Utils().get_conf_value('storePath'), time.strftime('%Y%m%d%H%M%S') + '.png')
        file_path = os.path.join(self.get_conf_value('logPath'), time.strftime('%Y%m%d'), 'screenshots', file_name)
        dPhone.screenshot(file_path)
        raise Exception(message + '，请参考截图信息: ' + 'file:///' + file_path)

    #拨打手机号码
    def dail_phone_no(self, phone_no):
        #唤醒屏幕
        dPhone.wakeup()
        #返回主界面
        dPhone.press.home()
        dPhone.press.home()
        dPhone(text = '拨号').click.wait()

        for n in phone_no:
            if n == '0':
                dPhone(resourceId = 'com.android.contacts:id/zero').click()
            elif n == '1':
                dPhone(resourceId='com.android.contacts:id/one').click()
            elif n == '2':
                dPhone(resourceId='com.android.contacts:id/two').click()
            elif n == '3':
                dPhone(resourceId = 'com.android.contacts:id/three').click()
            elif n == '4':
                dPhone(resourceId='com.android.contacts:id/four').click()
            elif n == '5':
                dPhone(resourceId='com.android.contacts:id/five').click()
            elif n == '6':
                dPhone(resourceId='com.android.contacts:id/six').click()
            elif n == '7':
                dPhone(resourceId='com.android.contacts:id/seven').click()
            elif n == '8':
                dPhone(resourceId='com.android.contacts:id/eight').click()
            elif n == '9':
                dPhone(resourceId='com.android.contacts:id/nine').click()
            else:
                self.raise_exception_for_phone('电话号码错误')
        dPhone(resourceId = 'com.android.contacts:id/nameDialButton2').click.wait()

    #结束通话
    def end_phone_call(self):
        ele = dPhone(resourceId = 'com.android.incallui:id/endButton')
        if ele.wait.exists():
            ele.click.wait()
        else:
            Utils().raise_Exception_info('挂断电话按键不存在')

# Phone().dail_phone_no('10086')
