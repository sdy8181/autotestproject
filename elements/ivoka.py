# -*- coding: UTF-8 -*-
from utils.uiTools import uit

class Ivoka:

    def __init__(self):
        # 新旧版本的pkgname判断
        global pkg_name
        pkg_name = "com.qinggan.ivoka"

    # 获取最高温度控件
    def get_weather_temperature_high_ele(self):
        return uit.get_ele_by_resourceId(pkg_name + ':id/weather_temperature_high')

    # 获取最低温度控件
    def get_weather_temperature_low_ele(self):
        return uit.get_ele_by_resourceId(pkg_name + ':id/weather_temperature_low')

    # 获取温度提示文本
    def get_weather_tip_ele(self):
        return uit.get_ele_by_resourceId(pkg_name + ':id/tips_text')
