# -*- coding:utf-8 -*-
'''
Created on 2014.8.5
@author: wangzhiyuan
'''


######################################################################
#  PCAN-Basic Example
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Keneth Wagner
#  Language: Python 2.6
#  ------------------------------------------------------------------
#
#  Copyright (C) 1999-2013  PEAK-System Technik GmbH, Darmstadt
######################################################################

from utils.PCANBasic import *        ## PCAN-Basic library import

## Imports for UI

import traceback               ## Error-Tracing library

import string                  ## String functions

import time                    ## Time-related library
import threading               ## Threading-based Timer library
import signal
import sys




TCL_DONT_WAIT           = 1<<1
TCL_WINDOW_EVENTS       = 1<<2
TCL_FILE_EVENTS         = 1<<3
TCL_TIMER_EVENTS        = 1<<4
TCL_IDLE_EVENTS         = 1<<5
TCL_ALL_EVENTS          = 0


COL_TYPE = 0
COL_ID = 1
COL_LENGTH = 2
COL_DATA = 3
COL_COUNT = 4
COL_TIME = 5

###*****************************************************************
### Message Status structure used to show CAN Messages
### in a ListView
###*****************************************************************
class MessageStatus:
    def __init__(self, canMsg = TPCANMsg(), canTimestamp = TPCANTimestamp(), listIndex = -1):
        self.__m_Msg = canMsg
        self.__m_TimeStamp = canTimestamp
        self.__m_iIndex = listIndex
        self.__m_iCount = 1

    def getCANMessage(self):
        return self.__m_Msg

    def getTimestamp(self):
        return self.__m_TimeStamp

    def getPosition(self):
        return self.__m_iIndex

    def getCount(self):
        return self.__m_iCount

    def Actualize(self,canMsg,canTimestamp):
        self.__m_Msg = canMsg
        self.__m_TimeStamp = canTimestamp        
        self.__m_iCount = self.__m_iCount + 1
###*****************************************************************




###*****************************************************************
### PCAN-basic Example app
###*****************************************************************
class PcanHandler(object):
    """
    Pcan message handler class,
    args: BAUDRATES
         
    """
    ## Constructor
    ##
    def __init__(self,BAUDRATES=PCAN_BAUD_250K,PCANHW=PCAN_USBBUS1):
        """
        init:
        BAUDRATES
        
        """
        self.m_BAUDRATES =BAUDRATES
        self.m_HWTYPES=PCAN_TYPE_ISA
        
        self.m_IOPORTS = 0x2A0
        self.interrupt = 11
    
        self.m_objPCANBasic = PCANBasic()
   
        #  pcanusb channel import
        self.m_PcanHandle =PCANHW
        
        #the connect data status
        self.heartOn=True
        # status switch tag: Reverse to gear,gear to Reverse
        self.statusSwitch=True
        self.count=0

        # Connects a selected PCAN-Basic channel
        #
        self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)

        result =  self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.m_BAUDRATES,self.m_HWTYPES,self.m_IOPORTS,self.interrupt)
        
        self.connect=result
        if result != PCAN_ERROR_OK:
            print ("conncet Error!!!!!!!!!!!!!!\n")
            raise IOError  
            self.openOk=False
            
        else:
            # Prepares the PCAN-Basic's PCAN-Trace file
            #
            self.ConfigureTraceFile()
            self.openOk=True

        # Sets the connection status of the form
        #
        
    
    def connectBUS(self):
        
        #再次建立连接，PC端易出现CAN bus无法释放的情况
        result =  self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.m_BAUDRATES,self.m_HWTYPES,self.m_IOPORTS,self.interrupt)
        
        self.connect=result
        if result != PCAN_ERROR_OK:
            print (result )
            self.openOk=False
            
        else:
            # Prepares the PCAN-Basic's PCAN-Trace file
            #
            self.ConfigureTraceFile()
            self.openOk=True
        
    
    
    ##  All id and parameter use this send            
    def writeCommand(self,mID,mParameter):
        '''
        @param mID: the hex string
        @param mParameter: the parameter list
        '''
        if self.openOk: 
            self.btnWrite_Click(mID,mParameter)
         
            
        
    ## read result
    def readHeartbeat(self):
        while self.openOk:
            self.btnRead_Click()
            time.sleep(1)
  
  
            
    '''
    'Do not change below method!!!!!!!!!
    '''
    ## Button btnRead handler
    ##
    def btnRead_Click(self):
        # We execute the "Read" function of the PCANBasic
        #
        result = self.m_objPCANBasic.Read(self.m_PcanHandle)

        if result[0] == PCAN_ERROR_OK:
            # We show the received message
            #
            self.ProcessMessage(result[1:])
        elif result[0] ==32:
            # If an error occurred, an information message is included
            #
            print("Receive queue is empty\n")
            print (result[0])
        else:
            print (str(result[0])+": Read error!!!!!!!!!!\n")

            
    ## Configures the Debug-Log file of PCAN-Basic
    ##
    def ConfigureLogFile(self):
        # Sets the mask to catch all events
        #
        iBuffer = LOG_FUNCTION_ALL

        # Configures the log file. 
        # NOTE: The Log capability is to be used with the NONEBUS Handle. Other handle than this will 
        # cause the function fail.
        #
        self.m_objPCANBasic.SetValue(PCAN_NONEBUS, PCAN_LOG_CONFIGURE, iBuffer)


    ## Configures the PCAN-Trace file for a PCAN-Basic Channel
    ##
    def ConfigureTraceFile(self):
        # Configure the maximum size of a trace file to 5 megabytes
        #
        iBuffer = 5
        stsResult = self.m_objPCANBasic.SetValue(self.m_PcanHandle, PCAN_TRACE_SIZE, iBuffer)
        if stsResult != PCAN_ERROR_OK:
            self.IncludeTextMessage(self.GetFormatedError(stsResult[0]))

        # Configure the way how trace files are created: 
        # * Standard name is used
        # * Existing file is ovewritten, 
        # * Only one file is created.
        # * Recording stopts when the file size reaches 5 megabytes.
        #
        iBuffer = TRACE_FILE_SINGLE | TRACE_FILE_OVERWRITE
        stsResult = self.m_objPCANBasic.SetValue(self.m_PcanHandle, PCAN_TRACE_CONFIGURE, iBuffer)        
        if stsResult != PCAN_ERROR_OK:
            self.IncludeTextMessage(self.GetFormatedError(stsResult[0]))
            

    ## Help Function used to get an error as text
    ##
    def GetFormatedError(self, error):
        # Gets the text using the GetErrorText API function
        # If the function success, the translated error is returned. If it fails,
        # a text describing the current error is returned.
        #
        stsReturn = self.m_objPCANBasic.GetErrorText(error, 0)
        if stsReturn[0] != PCAN_ERROR_OK:
            return "An error occurred. Error-code's text ({0:X}h) couldn't be retrieved".format(error)
        else:
            return stsReturn[1]





    ## Gets the current status of the PCAN-Basic message filter
    ##
    def GetFilterStatus(self):
        # Tries to get the sttaus of the filter for the current connected hardware
        #
        stsResult = self.m_objPCANBasic.GetValue(self.m_PcanHandle, PCAN_MESSAGE_FILTER)

        # If it fails, a error message is shown
        #
        if stsResult[0] != PCAN_ERROR_OK:
            print("Error!", self.GetFormatedError(stsResult[0]))
            return False,
        else:
            return True, stsResult[1]


    

    ## Creates and returns an input line for a received message with the messages-receive            
    ## Listview format
    ##
    def FormatCANMessage(self, msg, time):
        msgStringEntry = ""
        newMsg = msg.getCANMessage()
        bIsRTR = (newMsg.MSGTYPE & PCAN_MESSAGE_RTR.value) == PCAN_MESSAGE_RTR.value
      
        if (newMsg.MSGTYPE & PCAN_MESSAGE_EXTENDED.value) == PCAN_MESSAGE_EXTENDED.value:
            if bIsRTR:
                strTemp = "EXT/RTR "
            else:
                strTemp = "EXTENDED"
            msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_TYPE] - len(strTemp)))
            strTemp = "{0:08X}".format(newMsg.ID)
            msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_ID] - len(strTemp)))
        else:
            if bIsRTR:
                strTemp = "STD/RTR "
            else:
                strTemp = "STANDARD"
            msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_TYPE] - len(strTemp)))
            strTemp = "{0:03X}".format(newMsg.ID)
            msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_ID] - len(strTemp)))

        strTemp = str(newMsg.LEN)
        msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_LENGTH] - len(strTemp)))

        if bIsRTR:
            strTemp = "Remote Request"
        else:
            strTemp = ""
            for i in range(newMsg.LEN):
                if strTemp != "":
                    strTemp = strTemp + " "
                strTemp = strTemp + "{0:02X}".format(newMsg.DATA[i])
            msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_DATA] - len(strTemp)))

        strTemp = str(msg.getCount())
        msgStringEntry = msgStringEntry + (strTemp + " "*(self.m_ListColSpace[COL_COUNT] - len(strTemp)))
        msgStringEntry = msgStringEntry + (time + " "*(self.m_ListColSpace[COL_TIME] - len(time)))

        return msgStringEntry    

################################################################################################################################################
### Message-proccessing functions
################################################################################################################################################

    ## Modifies a message entry in the Message-ListView
    ##
    def ModifyMsgEntry(self, msgStsCurrentMessage, theMsg, itsTimeStamp):
        # Update and format the new time information
        #
        lastTimeStamp = msgStsCurrentMessage.getTimestamp()
        fTime = itsTimeStamp.millis + (itsTimeStamp.micros / 1000.0)       
        
        fTime = fTime - (lastTimeStamp.millis + (lastTimeStamp.micros / 1000.0))
            
        # Update the values associated with the message
        #
        msgStsCurrentMessage.Actualize(theMsg, itsTimeStamp)
        msgStringEntry = self.FormatCANMessage(msgStsCurrentMessage,str(fTime))
        
        print  (msgStringEntry)
        # Refresh the line-entry in the listview
        #
        #self.lstMessages.delete(msgStsCurrentMessage.getPosition())
        #self.lstMessages.insert(msgStsCurrentMessage.getPosition(),text=msgStringEntry)


    ## Inserts a new entry for a new message in the Message-ListView
    ##
    def InsertMsgEntry(self, theMsg, itsTimeStamp):
        # Format the new time information
        #
        if self.m_showPeriodCHB.get() == 0:
            strTime = "{0},{1}".format(itsTimeStamp.millis,itsTimeStamp.micros)
        else:
            strTime = ""

        # The status values associated with the new message are created
        #
        lastMsg = MessageStatus(theMsg,itsTimeStamp,len(self.m_LastMsgsList))
        self.m_LastMsgsList.append(lastMsg)

        # We add this status in the last message list
        msgStringEntry = self.FormatCANMessage(lastMsg,strTime)
        #self.lstMessages.insert(END,text=msgStringEntry)
        print (msgStringEntry)


    ## Processes a received message, in order to show it in the Message-ListView
    ##
    def ProcessMessage(self, *args):
        bFound = False
        
        # Split the arguments. [0] TPCANMsg, [1] TPCANTimestamp
        #
        theMsg = args[0][0]
        itsTimeStamp = args[0][1]    

        # We search if a message (Same ID and Type) is 
        # already received or if this is a new message
        #
        for msgStsCurrentMessage in self.m_LastMsgsList:
            if msgStsCurrentMessage.getCANMessage().ID == theMsg.ID:
                if msgStsCurrentMessage.getCANMessage().MSGTYPE == theMsg.MSGTYPE:
                    bFound = True
                    break        

        if bFound:
            # Messages of this kind are already received; we do an update
            #
            self.ModifyMsgEntry(msgStsCurrentMessage, theMsg, itsTimeStamp)
        else:
            # Messages of this kind are not received; we create a new entry
            #
            self.InsertMsgEntry(theMsg, itsTimeStamp)




################################################################################################################################################
### Event Handlers
################################################################################################################################################        

    ## Form-Closing Function / Finish function
    ##
    def finish_OnClosing(self):
        # Releases the used PCAN-Basic channel
        #
        self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)
        """Quit our mainloop."""
        self.exit = 0




    ## Button btnHwRefresh handler
    ##
    def btnHwRefresh_Click(self):

        # Clears the Channel comboBox and fill it again with
        # the PCAN-Basic handles for no-Plug&Play hardware and
        # the detected Plug&Play hardware
        #
        items = []
        # self.cbbChannel.subwidget('listbox').delete(0, Tix.END)
        for name, value in self.m_CHANNELS.iteritems():
            # Includes all no-Plug&Play Handles
            #
            if (value.value <= PCAN_DNGBUS1.value):
                items.append(name)
            else:
                # Checks for a Plug&Play Handle and, according with the return value, includes it
                # into the list of available hardware channels.
                #
                result = self.m_objPCANBasic.GetValue(value, PCAN_CHANNEL_CONDITION)
                if (result[0] == PCAN_ERROR_OK) and (result[1] & PCAN_CHANNEL_AVAILABLE):
                    result = self.m_objPCANBasic.GetValue(value, PCAN_CHANNEL_FEATURES)
                    items.append(name)

        items.sort()
        print (items)
        # self.cbbChannel
        # for name in items:
        #     self.cbbChannel.insert(Tix.END, name)
        # self.cbbChannel['selection'] = self.cbbChannel.pick(Tix.END)












    ## Button btnInit handler
    ##
    # def btnInit_Click(self):
    #     # gets the connection values
    #     #
    #     baudrate = self.m_BAUDRATES[self.cbbBaudrates['selection']]
    #     hwtype = self.m_HWTYPES[self.cbbHwType['selection']]
    #     ioport = int(self.cbbIO['selection'],16)
    #     interrupt = int(self.cbbInterrupt['selection'])
    #
    #     # Connects a selected PCAN-Basic channel
    #     #
    #     result =  self.m_objPCANBasic.Initialize(self.m_PcanHandle,baudrate,hwtype,ioport,interrupt)
    #
    #     if result != PCAN_ERROR_OK:
    #         tkMessageBox.showinfo("Error!", self.GetFormatedError(result[0]))
    #     else:
    #         # Prepares the PCAN-Basic's PCAN-Trace file
    #         #
    #         self.ConfigureTraceFile()
    #
    #     # Sets the connection status of the form
    #     #
    #     self.SetConnectionStatus(result == PCAN_ERROR_OK)


    ## Button btnRelease handler
    ##
    def btnRelease_Click(self):
        # Releases a current connected PCAN-Basic channel
        #
        self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)
##        tmrRead.enabled = false;
##        if thread ...:
##            thread.abort()
##            thread.Join()
##            thread =0
        # Sets the connection status of the main-form
        #
        self.SetConnectionStatus(False)


    ## Button btnFilterApply handler
    ##
    def btnFilterApply_Click(self):
        if self.m_FilterExtCHB.get():
            filterMode = PCAN_MODE_EXTENDED
        else:
            filterMode = PCAN_MODE_STANDARD

        # Gets the current status of the message filter
        #
        filterRet = self.GetFilterStatus()

        if not filterRet[0]:
            return 

        # Configures the message filter for a custom range of messages
        #
        if self.m_FilteringRDB.get() == 2:
            # Sets the custom filter
            #
            result = self.m_objPCANBasic.FilterMessages(self.m_PcanHandle,
                                                        int(self.m_IdFromNUD.get()),
                                                        int(self.m_IdToNUD.get()),
                                                        filterMode)
            # If success, an information message is written, if it is not, an error message is shown
            #
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The filter was customized. IDs from {0:X} to {1:X} will be received".format(int(self.m_IdFromNUD.get()),int(self.m_IdToNUD.get())))
            else:
                print("Error!", self.GetFormatedError(result))

            return

        # The filter will be full opened or complete closed
        #
        if self.m_FilteringRDB.get() == 0:
            filterMode = PCAN_FILTER_CLOSE
            textEnd = "closed"
        else:
            filterMode = PCAN_FILTER_OPEN
            textEnd = "opened"

        # The filter is configured
        #
        result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,
                                              PCAN_MESSAGE_FILTER,
                                              filterMode)
        
        # If success, an information message is written, if it is not, an error message is shown
        #
        if result == PCAN_ERROR_OK:
            self.IncludeTextMessage("The filter was successfully "+ textEnd)
        else:
            print.showinfo("Error!", self.GetFormatedError(result))


    ## Button btnFilterQuery handler
    ##
    def btnFilterQuery_Click(self):
        # Queries the current status of the message filter
        #
        filterRet = self.GetFilterStatus()

        if filterRet[0]:
            if filterRet[1] == PCAN_FILTER_CLOSE:
                self.IncludeTextMessage("The Status of the filter is: closed.")
            elif filterRet[1] == PCAN_FILTER_OPEN:
                self.IncludeTextMessage("The Status of the filter is: full opened.")
            elif filterRet[1] == PCAN_FILTER_CUSTOM:
                self.IncludeTextMessage("The Status of the filter is: customized.")
            else:
                self.IncludeTextMessage("The Status ofself.tmrRead the filter is: Invalid.")
                




    ## Button btnGetVersions handler
    ##
    def btnGetVersions_Click(self):
        # We get the vesion of the PCAN-Basic API
        #
        result = self.m_objPCANBasic.GetValue(PCAN_NONEBUS, PCAN_API_VERSION)
        if result[0] ==PCAN_ERROR_OK:
            self.IncludeTextMessage("API Version: " + result[1])
            # We get the driver version of the channel being used
            #
            result = self.m_objPCANBasic.GetValue(self.m_PcanHandle, PCAN_CHANNEL_VERSION)
            if result[0] == PCAN_ERROR_OK:
                # Because this information contains line control characters (several lines)
                # we split this also in several entries in the Information List-Box
                #
                lines = string.split(result[1],'\n')
                self.IncludeTextMessage("Channel/Driver Version: ")
                for line in lines:
                    self.IncludeTextMessage("     * " + line)

        # If an error ccurred, a message is shown
        #
        if result[0] != PCAN_ERROR_OK:
            print.showinfo("Error!", self.GetFormatedError(result[0]))



    ## Button btnWrite handler
    ##
    def btnWrite_Click(self,id,List):
        
        iCount =len(List)
        
        # We create a TPCANMsg message structure
        #
        CANMsg = TPCANMsg()

        # We configurate the Message.  The ID,
        # Length of the Data, Message Type and the data
        #
        CANMsg.ID = int(id,16)
        CANMsg.LEN =iCount
        CANMsg.MSGTYPE = PCAN_MESSAGE_STANDARD

        # If a remote frame will be sent, the data bytes are not important.
        #
   
    
            # We get so much data as the Len of the message
            #
        for i in range(iCount):
            CANMsg.DATA[i] = int(List[i],16)

        # The message is sent to the configured hardware
        #
        result = self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)

        # The message was successfully sent
        #
        if result == PCAN_ERROR_OK:
            print ("Message was successfully sent\n")
            return True
        else:
            # An error occurred.  We show the error.
            #
            print ("Message error!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            return False


    ## Button btnReset handler
    ##
    def btnReset_Click(self):
        # Resets the receive and transmit queues of a PCAN Channel.
        #
        result = self.m_objPCANBasic.Reset(self.m_PcanHandle)

        # If it fails, a error message is shown
        #
        if result != PCAN_ERROR_OK:
            print("Error!", self.GetFormatedTex(result))
        else:
            self.IncludeTextMessage("Receive and transmit queues successfully reset")


    ## Button btnStatus handler
    ##            
    def btnStatus_Click(self):
        # Gets the current BUS status of a PCAN Channel.
        #
        result = self.m_objPCANBasic.GetStatus(self.m_PcanHandle)

        # Switch On Error Name
        #
        if result == PCAN_ERROR_INITIALIZE:
            errorName = "PCAN_ERROR_INITIALIZE"
        elif result == PCAN_ERROR_BUSLIGHT:
            errorName = "PCAN_ERROR_BUSLIGHT"
        elif result == PCAN_ERROR_BUSHEAVY:
            errorName = "PCAN_ERROR_BUSHEAVY"
        elif result == PCAN_ERROR_BUSOFF:
            errorName = "PCAN_ERROR_BUSOFF"
        elif result == PCAN_ERROR_OK:
            errorName = "PCAN_ERROR_OK"
        else:
            errorName = "See Documentation"

        # Display Message
        #
        self.IncludeTextMessage("Status: {0} ({1:X}h)".format(errorName, result))







    ## Checkbox chbFilterExt handler
    ##             
    def chbFilterExt_CheckedChanged(self):
        # Determines the maximum value for a ID
        # according with the Filter-Type
        #
        if self.m_FilterExtCHB.get():
            self.nudIdTo['to'] = 0x1FFFFFFF
            self.nudIdFrom['to'] = 0x1FFFFFFF
        else:
            self.nudIdTo['to'] = 0x7FF
            self.nudIdFrom['to'] = 0x7FF

        # We check that the maximum value for a selected filter 
        # mode is used
        #
        if int(self.m_IdToNUD.get()) > self.nudIdTo['to']:
            pass
            #self.m_IdToNUD.set(iMaxValue)
        if int(self.m_IdFromNUD.get()) > self.nudIdFrom['to']:
            pass
            #self.m_IdFromNUD.set(iMaxValue)



## Button btnParameterSet handler
    ##
    def btnParameterSet_Click(self):
        currentVal = self.cbbParameter['selection']
        iVal = self.m_PARAMETERS[currentVal]

        if self.m_ConfigurationRDB.get() == 1:
            iBuffer = PCAN_PARAMETER_ON
            lastStr = "activated"
            lastStr2 = "ON"
        else:
            iBuffer = PCAN_PARAMETER_OFF
            lastStr = "deactivated"
            lastStr2 = "OFF"

        # The Device-Number of an USB channel will be set
        #
        if iVal == PCAN_DEVICE_NUMBER:
            iBuffer = int(self.m_DeviceIdNUD.get())
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_DEVICE_NUMBER,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The desired Device-Number was successfully configured")

        # The 5 Volt Power feature of a PC-card or USB will be set
        #        
        elif iVal == PCAN_5VOLTS_POWER:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_5VOLTS_POWER,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The USB/PC-Card 5 power was successfully " + lastStr)
            
        # The feature for automatic reset on BUS-OFF will be set
        #        
        elif iVal == PCAN_BUSOFF_AUTORESET:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_BUSOFF_AUTORESET,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The automatic-reset on BUS-OFF was successfully " + lastStr)
            
        # The CAN option "Listen Only" will be set
        #        
        elif iVal == PCAN_LISTEN_ONLY:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_LISTEN_ONLY,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The CAN option ""Listen Only"" was successfully " + lastStr)

        # The feature for logging debug-information will be set
        #
        elif iVal == PCAN_LOG_STATUS:
            result = self.m_objPCANBasic.SetValue(PCAN_NONEBUS,PCAN_LOG_STATUS,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The feature for logging debug information was successfully " + lastStr)

        # The channel option "Receive Status" will be set
        #        
        elif iVal == PCAN_RECEIVE_STATUS:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_RECEIVE_STATUS,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The channel option ""Receive Status"" was set to  " + lastStr2)

        # The feature for tracing will be set
        #        
        elif iVal == PCAN_TRACE_STATUS:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_TRACE_STATUS,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The feature for tracing data was successfully " + lastStr)

        # The feature for tracing will be set
        #        
        elif iVal == PCAN_CHANNEL_IDENTIFYING:
            result = self.m_objPCANBasic.SetValue(self.m_PcanHandle,PCAN_CHANNEL_IDENTIFYING,iBuffer)
            if result == PCAN_ERROR_OK:
                self.IncludeTextMessage("The procedure for channel identification was successfully " + lastStr)
                
        # The current parameter is invalid
        #
        else:
            stsResult = PCAN_ERROR_UNKNOWN
            print("Error!", "Wrong parameter code.")

        # If the function fail, an error message is shown
        #
        if result != PCAN_ERROR_OK:
            print("Error!", self.GetFormatedError(result))



       
    ## Entry txtID OnLeave handler
    ##                   
    def txtID_Leave(self,*args):
        # Calculates the text length and Maximum ID value according
        # with the Message Typ
        #
        if self.m_ExtendedCHB.get():
            iTextLength = 8
            uiMaxValue = 0x1FFFFFFF
        else:
            iTextLength = 3
            uiMaxValue = 0x7FF
        
        try:
            iValue = int(self.m_IDTXT.get(),16)       
        except ValueError:
            iValue = 0
        finally:
            # The Textbox for the ID is represented with 3 characters for 
            # Standard and 8 characters for extended messages.
            # We check that the ID is not bigger than current maximum value
            #
            if iValue > uiMaxValue:
                iValue = uiMaxValue            
            self.m_IDTXT.set("{0:0{1}X}".format(iValue,iTextLength))
            return True
        

    ## Entry txtData0 OnLeave handler
    ##   
    def txtData0_Leave(self,*args):        
        edits = [self.m_Data0TXT, self.m_Data1TXT, self.m_Data2TXT, self.m_Data3TXT, self.m_Data4TXT, self.m_Data5TXT, self.m_Data6TXT, self.m_Data7TXT]
        for i in range(8):
            # The format of all Textboxes Data fields are checked.
            #
            self.txtData0_LeaveHelper(edits[i])

    ## Helper function for the above funciton
    #
    def txtData0_LeaveHelper(self, editVar):
        try:
            iValue = int(editVar.get(),16)       
        except ValueError:
            iValue = 0
        finally:
            # All the Textbox Data fields are represented with 2 characters.
            # The maximum value allowed is 255 (0xFF)
            #
            if iValue > 255:
                iValue = 255
            editVar.set("{0:0{1}X}".format(iValue,2))
            
    def signal_handler(self,signal, frame):
        print('You pressed Ctrl+C!')
        self.finish_OnClosing()
        sys.exit(0)
        


                
                             
    def tmrRead_Tick(self):
        print ("AJA")
###*****************************************************************

# class WriteHeartbeat(threading.Thread):
#
#     def __init__(self,func,arg):
#         threading.Thread.__init__()
#         self.func=func
#         self.args=arg
#
#     def run(self):
#         apply(self.func,self.args)
        

       
if __name__ == '__main__':
    # Creates the Tkinter-extension Root
    #
    #root = Tix.Tk()
    # Uses the root to launch the PCAN-Basic Example application
    '''
    BAUDRATES must be correct
    As21 is PCAN_BAUD_250K
    '''
    SR=PcanHandler(PCAN_BAUD_250K)
    #PS=SerialThread.ReadDeviceThread()
    
    
    try:
    
        WHeart1=threading.Thread(target=SR.writeHeartbeat1)
        WHeart2=threading.Thread(target=SR.writeReverseSwitch)
    #     WHeart3=threading.Thread(target=SR.writeHeartbeat3)
    #     WHeart4=threading.Thread(target=SR.writeHeartbeat4)
    #     WHeart5=threading.Thread(target=SR.writeHeartbeat5)
    #     WHeart6=threading.Thread(target=SR.writeHeartbeat6)
    #     WHeart7=threading.Thread(target=SR.writeHeartbeat7)
    #     WHeart8=threading.Thread(target=SR.writeHeartbeat8)
    #     WHeart9=threading.Thread(target=SR.writeHeartbeat9)
    #     WHeart10=threading.Thread(target=SR.writeHeartbeat10)
    #     WHeart11=threading.Thread(target=SR.writeHeartbeat11)
    #     WHeart12=threading.Thread(target=SR.writeHeartbeat12)
    #     WHeart13=threading.Thread(target=SR.writeHeartbeat13)
    #     WHeart14=threading.Thread(target=SR.writeHeartbeat14)
    #     WHeart15=threading.Thread(target=SR.writeHeartbeat15)
    #     WHeart16=threading.Thread(target=SR.writeHeartbeat16)
    #     WHeart17=threading.Thread(target=SR.writeHeartbeat17)
    #     WHeart18=threading.Thread(target=SR.writeHeartbeat18)
        
        
        RHeart=threading.Thread(target=SR.readHeartbeat)
        
        WHeart1.setDaemon(False)
        WHeart2.setDaemon(False)
    #     WHeart3.setDaemon(False)
    #     WHeart4.setDaemon(False)
    #     WHeart5.setDaemon(False)
    #     WHeart6.setDaemon(False)
    #     WHeart7.setDaemon(False)
    #     WHeart8.setDaemon(False)
    #     WHeart9.setDaemon(False)
    #     WHeart10.setDaemon(False)
    #     WHeart11.setDaemon(False)
    #     WHeart12.setDaemon(False)
    #     WHeart13.setDaemon(False)
    #     WHeart14.setDaemon(False)
    #     WHeart15.setDaemon(False)
    #     WHeart16.setDaemon(False)
    #     WHeart17.setDaemon(False)
    #     WHeart18.setDaemon(False)
        
        RHeart.setDaemon(False)
        
        WHeart1.start()
        WHeart2.start()
        while True:
            if SR.statusSwitch:
                time.sleep(5)
                SR.statusSwitch=False
            else:
                time.sleep(5)
                SR.statusSwitch=True
                
                
        
    #     WHeart3.start()
    #     WHeart4.start()
    #     WHeart5.start()
    #     WHeart6.start()
    #     WHeart7.start()
    #     WHeart8.start()
    #     WHeart9.start()
    #     WHeart10.start()
    #     WHeart11.start()
    #     WHeart12.start()
    #     WHeart13.start()
    #     WHeart14.start()
    #     WHeart15.start()
    #     WHeart16.start()
    #     WHeart17.start()
    #     WHeart18.start()
     
        RHeart.start()
    except KeyboardInterrupt:
        SR.heartOn=False
        SR.finish_OnClosing()
    finally:
        SR.finish_OnClosing()
        
        
    
