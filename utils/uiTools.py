# -*- coding: utf-8 -*-

import os
import time
from utils.helpTools import ht


class UiTools:

    # 失败截图
    def take_screenshot(self):
        file_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        file_path = os.path.join(ht.get_conf_value('logPath'), time.strftime('%Y%m%d'), 'screenshots' , file_name)
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        ht.get_device_obj().screenshot(file_path)
        # self.__set_file_path('file://' + file_path)
        print(file_path)
        return file_path
    # crash监听
    def crash_handler(self):
        device = ht.get_device_obj()
        print('开始检查应用是否crash')
        if device(resourceId='android:id/message').wait.exists():
            print('应用crash')
            device(resourceId='android:id/button1').click.wait()
            return True
        else:
            return False

    # 抛出异常
    def raise_Exception_info(self, err_msg):
        png_path = self.take_screenshot()
        if self.crash_handler():
            raise Exception('应用crash，' + err_msg + '请参考截图信息: file:///' + png_path)
            # + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')
        else:
            raise Exception('用例运行失败，' + err_msg + '请参考截图信息: file:///' + png_path)
            # + ' 和:  http://10.10.99.87:9000/' + time.strftime('%Y%m%d') + '/' + sce_name + '.log' + ' 对应场景日志信息 ')

    # 根据resourceID获取控件
    # 5s时间等待控件存在
    def get_ele_by_resourceId(self, resource_id):
        ele = ht.get_device_obj()(resourceId= resource_id)
        ele.wait.exists()
        return ele

    # 根据resourceID获取控件
    # 5s时间等待控件存在
    def get_ele_by_text(self, txt):
        ele = ht.get_device_obj()(text=txt)
        ele.wait.exists()
        return ele

uit = UiTools()
