"""
[LogFile]
Disable = 0
LogName = log.txt
TimeStamp = 1
FileStamp = 1
FuncStamp = 1
LineStamp = 1

# Get config parser
config_parser = items.getConfigParser()

# Set logger output directory
logDirectory = config_parser.getValue('LogFile', 'Directory')
m_log.setDirectory(logDirectory)

# Set logger output file
logFilename = config_parser.getValue('LogFile', 'LogName')
m_log.setLogFilename(logFilename)

# Set logger flag
options = ['Disable', 'TimeStamp', 'FileStamp', 'FuncStamp', 'LineStamp']
config_settings = config_parser.getValues('LogFile', options)
m_log.setLogger(config_settings)

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
    def __init__(self, default_dir = ".", default_file = "log"):
        self.record = []
        self.directory, self.log_filename = default_dir, default_file
        self.disable, self.timeStamp, self.fileStamp, self.funcStamp, self.lineStamp, = 1, 0, 0, 0, 0
        
    def setDirectory(self, directory_name):
        self.directory = directory_name
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

    def setLogFilename(self, logfile_name):
        self.log_filename = logfile_name

    def getLogger(self):
        return self.record
    
    def setLogger(self, opts):
        try:
            self.disable, self.timeStamp, self.fileStamp, self.funcStamp, self.lineStamp = int(opts[0]), int(opts[1]), int(opts[2]), int(opts[3]), int(opts[4])
            userName, osName, platformSystem, platformRelease = getpass.getuser(), os.name, platform.system(), platform.release()

            #print("Disable", str(_disable), "Time", str(_timeStamp), "File", str(_fileStamp), "Func", str(_funcStamp), "Line", str(_lineStamp))
            msg = "User : " + userName + " , Platform : " + osName + " " + platformSystem + " " + platformRelease
            print(msg)
        except:
            raise 'Error'
        
    def writeBuffer(self, msg):
        output = []
        # do not write log is disabled
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
        # add debug msg
        output.append(msg)
        # write whole data into record
        self.record.append(output)

    def printLog(self):
        for line in self.record:
            print(line)

    def cleanLog(self):
        while len(self.record) != 0:
            self.record.pop()   
    
    def reportGen(self):
        with open(self.directory + "/" + self.log_filename, 'a') as f:
            for line in self.record:
                f.write("%s\n" % str(line))

    def getTime(self):
        return str(datetime.datetime.now())