"""
[LogFile]
Disable = 0
LogName = log.txt
TimeStamp = 1
FileStamp = 1
FuncStamp = 1
LineStamp = 1

# Set logger level
m_log.setLogger(Disable, TimeStamp, FileStamp, FuncStamp, LineStamp)

# Write message into buffer
m_log.writeBuffer(OUTPUT_MSG)

# Dump debug message
m_log.printLog()
"""
import os
import platform
import datetime
import inspect
import getpass

class logger():
    def __init__(self):
        self.record = []
        self.disable, self.timeStamp, self.fileStamp, self.funcStamp, self.lineStamp, = 1, 0, 0, 0, 0
        
    def getLogger(self):
        return self.record
    
    def setLogger(self, _disable, _timeStamp, _fileStamp, _funcStamp, _lineStamp):
        try:
            self.disable, self.timeStamp, self.fileStamp, self.funcStamp, self.lineStamp = _disable, _timeStamp, _fileStamp, _funcStamp, _lineStamp
            userName, osName, platformSystem, platformRelease = getpass.getuser(), os.name, platform.system(), platform.release()

            #print("Disable", str(_disable), "Time", str(_timeStamp), "File", str(_fileStamp), "Func", str(_funcStamp), "Line", str(_lineStamp))
            msg = "User : " + userName + " , Platform : " + osName + " " + platformSystem + " " + platformRelease
            print(msg)
        except:
            raise 'Error'
        
    def writeBuffer(self, msg):
        output = []
        if self.disable is 1:
            return

        # add time stamp
        if self.timeStamp is 1:
            output.append(self.getTime())
        # add filename stamp
        if self.fileStamp is 1:
            file_msg = str(inspect.stack()[1].filename).split('\\').pop()
            # add line number after filename
            if self.lineStamp is 1:
                file_msg = file_msg + ":" + str(inspect.stack()[1].lineno)
            output.append(file_msg)
        # add function name stamp
        if self.funcStamp is 1:
            output.append(inspect.stack()[1].function)

        output.append(msg)
        self.record.append(output)

    def printLog(self):
        #print("logger >>> Current buffer size", len(self.record))
        for line in self.record:
            print(line)

    def cleanLog(self):
        while len(self.record) != 0:
            self.record.pop()   
    
    def reportGen(self):
        print("logger >>> Write log into file...")

        
    def getTime(self):
        return str(datetime.datetime.now())

"""

class log:
    def __init__(self):
        self.debug = True
        self.tc = name()
			
    def createDir(self):
        if not os.path.exists('DebugLog'):
            os.makedirs('DebugLog')
		
    def writeInfoToLog(self, mode, infoStr):    #arg1-> 0: no space, 1: 4 space, arg2-> string
        self.createDir()
        fPath = os.path.abspath('.')
        fLogName = self.getIniData('LogFile', 'LogName')
        fStrComb = fPath + '\\DebugLog\\' + fLogName
        f = open(fStrComb, 'a+')
        if mode == 1:
            f.write('    ' + infoStr + '\n')
        else:
            f.write(infoStr + '\n')
        f.close()
		
        if self.debug == True:
            print(infoStr)

    def getIniData(self, mainStr, subStr):
        #parser = configparser.ConfigParser()
        parser = MyConfigParser()
        parser.read('settings/config.ini')
        return parser.get(mainStr, subStr)
		
    def setIniData(self, mainStr, subStr, sData):
        #parser = configparser.ConfigParser()
        parser = MyConfigParser()
        parser.read('settings/config.ini')
        parser[mainStr][subStr] = sData 
        with open('config.ini', 'w') as configfile:
            parser.write(configfile)
		
    def writeReport(self, infoStr):
        self.createDir()
        fPath = os.path.abspath('.')
        fLogName = self.getIniData('Report', 'PartNumber')
        fStrComb = fPath + '\\DebugLog\\' + fLogName[9:] + '.txt'
        f = open(fStrComb, 'a+')
        f.write(infoStr + '\n')
        f.close()
		
    def getTcSum(self):
        parser = configparser.ConfigParser()
        parser.read('settings/config.ini')
        sum = 0
        while True:
            try:
                subStr = 'TC' + str(sum)
                res = parser.get('Report', subStr)
                sum += 1
            except:
                return sum
				
    def casesLog(self,mode, tcIndex, result):
        caseName = self.tc.getTcName(tcIndex)
        if mode == 0:
            self.writeInfoToLog(0,caseName)
        else:
            if result == 1:
                self.writeInfoToLog(1,caseName + 'cSuccessful')
            else:
                self.writeInfoToLog(1,caseName + 'cFail')
				
    def setTcResult(self,tcIndex,res):
        sCase = 'TC' + str(tcIndex)
        try:
            self.setIniData("Report", sCase, str(res))
        except:
            print("error ...!")
			
    def getTcResult(self,tcIndex):
        sCase = 'TC' + str(tcIndex)
        res = self.getIniData("Report", sCase)
        return res

# ==================================================================================================
class name:
    def __init__(self):
        pass

    def getTcName(self,tcIndex):
        index = str(tcIndex)
        if index == '0':
            res = 'acPowerON(0)'
        elif index == '1':
            res = 'acPowerON(1)'
        elif index == '2':
            res = 'reportTask()'
        elif index == '3':
            res = 'execCmd_COM()'
        elif index == '4':
            res = 'openCOM()'
        elif index == '5':
            res = 'BMCLogin()'
        elif index == '6':
            res = 'flashBMCMacTask()'
        elif index == '7':
            res = 'flashMAC3()'
        elif index == '8':
            res = 'systemPowerON()'
        elif index == '9':
            res = 'BMCToSysPort()'
        elif index == '10':
            res = 'systemLogin()'
        elif index == '11':
            res = 'chkDeviceStatus()'
        elif index == '12':
            res = 'chkDeviceStatus()'
        elif index == '13':
            res = 'sysPowerOFF_intoBMC()'
        elif index == '14':
            res = 'confirmSysPowerOFF()'
        elif index == '15':
            res = 'BMCRestart()'
        else:
            res = 'Reserved ...'
			
        return res

"""