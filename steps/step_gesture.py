# -*- coding: UTF-8 -*-
import os

from behave import when, then

from actions.gesture import Gesture
from utils.utils import Utils


@when(u'< 开始倒车')
def step_impl(context):
    Gesture().start_back_car()
@when(u'< 结束倒车')
def step_impl(context):
    Gesture().stop_back_car()
@then(u'< 验证正在倒车')
def step_impl(context):
    cur_png_name = Utils().take_screenshot()
    init_png_name = os.path.join(os.path.abspath('../support'), 'car_reverse.png')
    diff_data = Utils().get_image_diff_data(init_png_name, cur_png_name)
    if diff_data > 1.0:
        error_png = Utils().take_screenshot()
        context.execute_steps('''
        when < 结束倒车
        ''')
        raise Exception('车机不在倒车界面,请参考截图信息: file:///' + error_png)

@then(u'< 验证退出倒车')
def step_impl(context):
    cur_png_name = Utils().take_screenshot()
    init_png_name = os.path.join(os.path.abspath('../support'), 'car_reverse.png')
    diff_data = Utils().get_image_diff_data(init_png_name, cur_png_name)
    if not diff_data > 1000.0:
        error_png = Utils().take_screenshot()
        context.execute_steps('''
            when < 结束倒车
            ''')
        raise Exception('车机在倒车界面, 请参考截图信息: file:///' + error_png)
