# -*- coding: utf-8 -*-

import os
import sys

# file = open('procranktest.log', 'a')
# file.writelines(' Vss      Rss      Pss      Uss \n')
print(' Vss      Rss      Pss      Uss  \n')
# file.close()

for i in range(100):
    ret = os.popen('adb shell procrank | grep com.autonavi.amapauto').readlines()
    vss = 0
    rss = 0
    pss = 0
    uss = 0
    for r in ret:
        if len(r) > 0:
            while r.__contains__('  '):
                r = r.replace('  ', ' ')
            retlist = r.split(' ')
            # print(retlist)
            vss += int(retlist[2][:-1])
            rss += int(retlist[3][:-1])
            pss += int(retlist[4][:-1])
            uss += int(retlist[5][:-1])

    retStr = str(vss) + '   ' + str(rss) + '   ' + str(pss) + '   ' + str(uss)
    print(retStr)
            # file = open('/home/ogq/procranktest.log', 'a')
            # file.writelines(r)
            # file.close()
