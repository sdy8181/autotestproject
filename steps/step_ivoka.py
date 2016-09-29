# -*- coding: UTF-8 -*-
from behave import then

from actions.ivoka import Ivoka
from support.global_vars import d
from utils.utils import Utils


@then(u'< 验证天气信息')
def step_impl(context):
    # 校验最高温度控件 最低温度控件  天气提示文本是否存在
    ele_high = Ivoka().get_weather_temperature_high_ele()
    ele_low = Ivoka().get_weather_temperature_low_ele()
    ele_tip = Ivoka().get_weather_tip_ele()

    if not  (ele_high.wait.exists() and ele_low.wait.exists() and ele_tip.wait.exists()):
        Utils().raise_Exception_info('天气信息验证失败')

@then(u'< 验证航班信息')
def step_impl(context):
    ele1 = d(textContains = '航空')
    ele2 = d(textContains='-->')
    ele3 = d(textContains=':')

    if not (ele1.wait.exists(timeout = Utils().LONG_TIME_OUT) and ele2.wait.exists(timeout = Utils().LONG_TIME_OUT) and ele3.wait.exists(timeout = Utils().LONG_TIME_OUT)):
        Utils().raise_Exception_info('航班信息验证失败')

@then(u'< 验证证券信息')
def step_impl(context):
    ele1 = d(textContains='%')
    ele2 = d(textContains='指数')
    ele3 = d(textContains='当前')
    ele4 = d(textContains='点')

    if not (ele1.wait.exists(timeout = Utils().LONG_TIME_OUT) and ele2.wait.exists(timeout = Utils().LONG_TIME_OUT) and ele3.wait.exists(timeout = Utils().LONG_TIME_OUT) and ele4.wait.exists(timeout = Utils().LONG_TIME_OUT)):
        Utils().raise_Exception_info('证券信息验证失败')