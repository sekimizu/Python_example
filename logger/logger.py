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
