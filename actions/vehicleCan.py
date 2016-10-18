# -*- coding:utf-8 -*-
'''
Created on 2016年9月19日

@author: wangzhiyuan
'''

from support.global_vars import d
from utils.CANSignalSets import TocFunctionMap
from utils.PcanHandler import *
from utils.helpTools import HT


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


class CAN_Start():
    def __init__(self, PCAN_BAUD=PCAN_BAUD_100K):

        self.can = PcanHandler(PCAN_BAUD)
        self.flag = True

        self.SWITCH = True


    ########
    ##function details
    ##########
    def addVolume(self):
        self.can.writeCommand(TocFunctionMap['Vol+'][0], TocFunctionMap['Vol+'][1])
        time.sleep(0.2)
        self.can.writeCommand(TocFunctionMap['SWC_up'][0], TocFunctionMap['SWC_up'][1])
        time.sleep(0.2)

    def reduceVolume(self):

        self.can.writeCommand(TocFunctionMap['Vol-'][0], TocFunctionMap['Vol-'][1])
        time.sleep(0.2)
        self.can.writeCommand(TocFunctionMap['SWC_up'][0], TocFunctionMap['SWC_up'][1])
        time.sleep(1)

    def ivoka(self):
        self.can.writeCommand(TocFunctionMap['iVoka'][0], TocFunctionMap['iVoka'][1])
        time.sleep(0.2)
        self.can.writeCommand(TocFunctionMap['SWC_up'][0], TocFunctionMap['SWC_up'][1])
        time.sleep(1)

    def seeknext(self):
        self.can.writeCommand(TocFunctionMap['Seek+'][0], TocFunctionMap['Seek+'][1])
        time.sleep(0.2)
        self.can.writeCommand(TocFunctionMap['SWC_up'][0], TocFunctionMap['SWC_up'][1])
        time.sleep(1)

    def seekpre(self):
        self.can.writeCommand(TocFunctionMap['Seek-'][0], TocFunctionMap['Seek-'][1])
        time.sleep(0.2)
        self.can.writeCommand(TocFunctionMap['SWC_up'][0], TocFunctionMap['SWC_up'][1])
        time.sleep(1)



    #左前门
    def openlfdoor(self):

        for i in range(10):
            self.can.writeCommand(TocFunctionMap['LFDoor'][0], TocFunctionMap['LFDoor'][1])
            time.sleep(0.2)

    def openrfdoor(self):

        for i in range(10):
            self.can.writeCommand(TocFunctionMap['RFDoor'][0], TocFunctionMap['RFDoor'][1])
            time.sleep(0.2)

    def openlrdoor(self):

        for i in range(10):
            self.can.writeCommand(TocFunctionMap['LRDoor'][0], TocFunctionMap['LRDoor'][1])
            time.sleep(0.2)

    def openrrdoor(self):

        for i in range(10):
            self.can.writeCommand(TocFunctionMap['RRDoor'][0], TocFunctionMap['RRDoor'][1])
            time.sleep(0.2)

    def opentrunk(self):

        for i in range(10):
            self.can.writeCommand(TocFunctionMap['Trunk'][0], TocFunctionMap['Trunk'][1])
            time.sleep(0.2)

    def openhood(self):
        for i in range(10):
            self.can.writeCommand(TocFunctionMap['HOOD'][0], TocFunctionMap['HOOD'][1])
            time.sleep(0.2)

    def closealldoor(self):
        for i in range(10):
            self.can.writeCommand(TocFunctionMap['CloseDoor'][0], TocFunctionMap['CloseDoor'][1])
            time.sleep(0.2)

    def openpositionlight(self):
        self.can.writeCommand(TocFunctionMap['postionlight'][0], TocFunctionMap['postionlight'][1])
        time.sleep(0.2)

    def initlight(self):
        self.can.writeCommand(TocFunctionMap['Instrument'][0], TocFunctionMap['Instrument'][1])
        time.sleep(0.2)

    ##################################
    ##档位
    ###############
    def gearsP(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Park'][0], TocFunctionMap['Park'][1])
            time.sleep(0.5)

    def reverse(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Reverse'][0], TocFunctionMap['Reverse'][1])
            time.sleep(0.5)

    def exitreverse(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Park'][0], TocFunctionMap['Park'][1])
            time.sleep(0.2)

    def gearsN(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Park'][0], TocFunctionMap['Park'][1])
            time.sleep(0.2)

    def gearD(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Drive'][0], TocFunctionMap['Drive'][1])
            time.sleep(0.2)

    def drive40(self):
        for i in range(20):
            self.can.writeCommand(TocFunctionMap['Drive_40KM'][0], TocFunctionMap['Drive_40KM'][1])
            time.sleep(0.2)



    ##########
    # power acc
    ##########
    def accoff(self):
        '''
            use this function to turn off devices
        '''
        self.can.writeCommand(TocFunctionMap['AccOff'][0], TocFunctionMap['AccOff'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['AccOff'][0], TocFunctionMap['AccOff'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['LFDoor'][0], TocFunctionMap['LFDoor'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['LFDoor'][0], TocFunctionMap['LFDoor'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['DoorBackLight'][0], TocFunctionMap['DoorBackLight'][1])

    def accOnState(self):
        '''
        use this function to keep devices acc on
        '''
        self.can.writeCommand(TocFunctionMap['AccOn'][0], TocFunctionMap['AccOn'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['AccOn'][0], TocFunctionMap['AccOn'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['BasicInfo'][0], TocFunctionMap['BasicInfo'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['Instrument'][0], TocFunctionMap['DoorBackLight'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['AccOn'][0], TocFunctionMap['AccOn'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['AccOn'][0], TocFunctionMap['AccOn'][1])
        time.sleep(0.1)
        self.can.writeCommand(TocFunctionMap['AccOn'][0], TocFunctionMap['AccOn'][1])
        time.sleep(0.1)

    def close_connect(self):
        self.can.finish_OnClosing()

    ########################
    # 用于保持车载信号一直通信中
    #########################
    def keepHeart(self):
        # keep subprocess alive
        try:
            while True:
                # check send message or not
                if self.SWITCH:
                    if self.flag:
                        self.accOnState()
                    else:
                        self.accoff()

        finally:
            self.close_connect()



###########################################################################################################
#class: vehecle signal
##############

@singleton
class CAN_action():

    def __init__(self):
        baud = HT().get_conf_value('devicePcanBaudrate').upper()

        if '100' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_100K)
        elif '250' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_250K)
        elif '500' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_500K)
        elif '800' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_800K)
        elif '1M' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_1M)
        elif '1000' in baud:
            self.pcan = CAN_Start(PCAN_BAUD_1M)
        else:
            print("Pcan 波特率设置不正确")

        canthread = threading.Thread(target=self.pcan.keepHeart)
        canthread.setDaemon(True)
        canthread.start()

    def addVolume(self):
        self.pcan.addVolume()

    def reduceVolume(self):
        self.pcan.reduceVolume()

    def ivoka(self):
        self.pcan.ivoka()

    def reverse(self):
        self.pcan.reverse()

    def exitreverse(self):
        self.pcan.exitreverse()

    def Pgears(self):
        self.pcan.gearsP()

    def Ngears(self):
        self.pcan.gearsN()

    def Dgears(self):
        self.pcan.gearD()

    def drive40(self):
        self.pcan.drive40()

    def openlfdoor(self):
        self.pcan.openlfdoor()

    def openrfdoor(self):
        self.pcan.openrfdoor()

    def openlrdoor(self):
        self.pcan.openlfdoor()

    def openrrdoor(self):
        self.pcan.openrrdoor()

    def opentrunk(self):
        self.pcan.opentrunk()

    def openhood(self):
        self.pcan.openhood()

    def closealldoor(self):
        self.pacn.closealldoor()



    def seeknext(self):
        self.pcan.seeknext()

    def seekpre(self):
        self.pcan.seekpre()

    def openpositonlight(self):
        self.pcan.openpositionlight()

    def initlight(self):
        self.pcan.initlight()


    def release(self):
        self.pcan.close_connect()



#############
# UiAutomator
#########
class UI_Action():

    def au_next(self):
        d(resourceId='com.qinggan.app.launcher:id/app_music').click()
        time.sleep(2)
        d(resourceId='com.qinggan.app.music:id/img_next', ).click()
        time.sleep(2)

        d.click(640,656)
        time.sleep(2)
        d.click(880, 656)
        time.sleep(2)
        d.click(880,656)
        time.sleep(2)


if __name__ == '__main__':

    ui = UI_Action()
    canAction = CAN_action()
    time.sleep(2)
    canAction.reduceVolume()
    ui.au_next()
    canAction.reverse()
    time.sleep(5)
    canAction.exitreverse()
    canAction.release()



