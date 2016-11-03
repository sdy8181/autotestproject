# -*- coding: UTF-8 -*-
import os
import random
import time
from utils.helpTools import ht
from utils.uiTools import uit
from support.global_vars import dphone
class Phone:


    def click_pair_ele(self):
        # 唤醒屏幕
        dphone.wakeup()
        # 打开通知栏
        dphone.open.notification()
        #打开配对框并点击配对
        if dphone(text='配对请求').wait.exists(timeout=ht.LONG_TIME_OUT):
            dphone(text='配对请求').click.wait()
            if(dphone(text='配对').wait.exists()):
                dphone(text='配对').click.wait()
        # 取消else 防止已经链接了就不会收到请求了
        # else:
        #     self.raise_exception_for_phone('手机端没有收到配对请求')

    # 播放QQ音乐
    def play_qq_music(self):
        # 回到主界面
        dphone.wakeup()
        dphone.press.home()
        dphone.press.home()
        # 点击播放qq音乐
        qqmusic_ele = dphone(text='QQ音乐')
        if qqmusic_ele.wait.exists():
            qqmusic_ele.click.wait()
        else:
            self.raise_exception_for_phone('QQ音乐图标不存在')

        #判断是否已经连接成功
        conn_txt = dphone(text='连接成功')
        if not conn_txt.wait.exists():
            # 判断当前音乐是在播放还是暂停，如果是暂停，点击播放按钮
            if dphone(text='关闭').wait.exists():
                dphone(text = '关闭').click.wait()

            ele = dphone(className = 'android.widget.ImageView')
            size = len(ele)
            ele[size - 1].click.wait()
            music_list_ele = dphone(className = 'android.widget.TextView')
            if music_list_ele.wait.exists():
                size = len(music_list_ele)
                music_list_ele[size - random.randint(5, 10)].click.wait()
            else:
                self.raise_exception_for_phone('qq音乐列表不存在')

    #点击和连接的 连接控件
    def click_conn_ele(self):
        ele = dphone(text='连接')
        ele.wait.exists()
        if ele.exists:
            ele.click()
    #校验是否手机和Qplay链接成功
    def check_device_conn_phone(self):
        ele = dphone(text = '连接成功')
        ele.wait.exists(timeout=ht.LONG_TIME_OUT)
        if not ele.exists:
            self.raise_exception_for_phone('Qplay和手机连接失败')

    #判断是否同步播放指定的歌曲
    def check_is_play_specil_music(self, name):
        ele = dphone(text=name)
        if not ele.wait.exists(timeout=ht.LONG_TIME_OUT):
            self.raise_exception_for_phone('音乐没有同步播放')
    # 点击退出车机模式
    def click_exit_qplay(self):
        ele = dphone(text='退出车机模式')
        if ele.exists:
            ele.click()
        else:
            self.raise_exception_for_phone('退出车机模式控件不存在')

    def raise_exception_for_phone(self, message):
        file_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        # file_path = os.path.join(Utils().get_conf_value('storePath'), time.strftime('%Y%m%d%H%M%S') + '.png')
        file_path = os.path.join(ht.get_conf_value('logPath'), time.strftime('%Y%m%d'), 'screenshots', file_name)
        dphone.screenshot(file_path)
        raise Exception(message + '，请参考截图信息: ' + 'file:///' + file_path)

    #拨打手机号码
    def dail_phone_no(self, phone_no):
        #唤醒屏幕
        dphone.wakeup()
        #返回主界面
        dphone.press.home()
        dphone.press.home()
        dphone(text='拨号').click.wait()

        for n in phone_no:
            if n == '0':
                dphone(resourceId = 'com.android.contacts:id/zero').click()
            elif n == '1':
                dphone(resourceId='com.android.contacts:id/one').click()
            elif n == '2':
                dphone(resourceId='com.android.contacts:id/two').click()
            elif n == '3':
                dphone(resourceId = 'com.android.contacts:id/three').click()
            elif n == '4':
                dphone(resourceId='com.android.contacts:id/four').click()
            elif n == '5':
                dphone(resourceId='com.android.contacts:id/five').click()
            elif n == '6':
                dphone(resourceId='com.android.contacts:id/six').click()
            elif n == '7':
                dphone(resourceId='com.android.contacts:id/seven').click()
            elif n == '8':
                dphone(resourceId='com.android.contacts:id/eight').click()
            elif n == '9':
                dphone(resourceId='com.android.contacts:id/nine').click()
            else:
                self.raise_exception_for_phone('电话号码错误')
        dphone(resourceId='com.android.contacts:id/nameDialButton2').click.wait()

    #结束通话
    def end_phone_call(self):
        ele = dphone(resourceId='com.android.incallui:id/endButton')
        if ele.wait.exists():
            ele.click.wait()
        else:
            uit.raise_Exception_info('挂断电话按键不存在')

