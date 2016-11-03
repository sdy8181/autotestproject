# -*- coding: UTF-8 -*-
import random
import time
from behave import then
from behave import when

from elements.vehicleCan import CAN_action

@when(u'< 方向盘调起ivoka')
def step_impl(context):
    CAN_action().ivoka()

@when(u'< 方向盘增加音量')
def step_impl(context):
    CAN_action().addVolume()

@when(u'< 方向盘降低音量')
def step_impl(context):
    CAN_action().reduceVolume()

@when(u'< 方向盘seek+')
def step_impl(context):
    CAN_action().seeknext()

@when(u'< 方向盘seek-')
def step_impl(context):
    CAN_action().seekpre()



@when(u'< 挂倒车档')
def step_impl(context):
    CAN_action().reverse()

@when(u'< 退出倒车档')
def step_impl(context):
    CAN_action().exitreverse()

@when(u'< 挂P档')
def step_impl(context):
    CAN_action().Pgears()

@when(u'< 挂N档')
def step_impl(context):
    CAN_action().Ngears()

@when(u'< 挂D档')
def step_impl(context):
    CAN_action().Dgears()

@when(u'< D档车速40KM')
def step_impl(context):
    CAN_action().drive40()



@when(u'< 打开左前门')
def step_impl(context):
    CAN_action().openlfdoor()

@when(u'< 打开右前门')
def step_impl(context):
    CAN_action().openrfdoor()

@when(u'< 打开左后门')
def step_impl(context):
    CAN_action().openlrdoor()

@when(u'< 打开右后门')
def step_impl(context):
    CAN_action().openrrdoor()

@when(u'< 打开后备箱门')
def step_impl(context):
    CAN_action().opentrunk()

@when(u'< 打开引擎盖门')
def step_impl(context):
    CAN_action().opentrunk()

@when(u'< 关闭所有车门')
def step_impl(context):
    CAN_action().closealldoor()

@when(u'< 打开示阔灯')
def step_impl(context):
    CAN_action().openpositonlight()

@when(u'< 关闭示阔灯')
def step_impl(context):
    CAN_action().initlight()
