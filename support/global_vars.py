# -*- coding: UTF-8 -*-
from utils.utils import Utils

global d
d = Utils().get_device_obj()
global ver_flag
ver_flag = Utils().is_old_ver()