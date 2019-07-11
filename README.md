-------------------------------------------------------------------
Installation:
-------------------------------------------------------------------

1. Install [Python 3.7](https://www.python.org/downloads/release/python-370/) 
<br>
2. Install Robot framework from [Github](https://github.com/robotframework/robotframework) instructions.
<br>
3. Install Text Editor [Visual Studio Code](https://code.visualstudio.com/)
    ![image](https://imgur.com/download/GlMikqh/)
<br>
4. Setup PATH Variable
    ![image](https://imgur.com/download/4qhDSMP/)
<br>
5. Add "C:\Users\<YOUR_USERNAME>\AppData\Local\Programs\Python\Python37"
<br>
6. Check environment.
    ```
    python -V
    pip -V
    ```
    ![image](https://imgur.com/download/h27JtRq/)
<br>

-------------------------------------------------------------------
How to launch:
-------------------------------------------------------------------
1. From Visual Studio Code
```
Select "File" > "Open Folder" on top menu.
```
![image](https://imgur.com/download/1r4VVX9/)
<br>
```
Select target directory and click ok.
```
![image](https://imgur.com/download/ok9BVTR/)
<br>
```
After load-up, select "Terminal" > "New Terminal" on top menu.
```
![image](https://imgur.com/download/iSAiTKp/)
<br>
```
Terminal will pop-up in buttom frame.
```
![image](https://imgur.com/download/PxS4J1C/)
<br>

2. From terminal

For develop (DEBUG single case):
```
Change current directory to target folder.
```
![image](https://imgur.com/download/LXMgqXC/)
<br>

Do a single run.
```
python main.py <index>
```
![image](https://imgur.com/download/WGuxF68/)
<br>

Show the result.
![image](https://imgur.com/download/yo8HgGA/)

For Test Process(Run all scripts):
```
robot main.robot
```

-------------------------------------------------------------------
Folders definition:
-------------------------------------------------------------------

#### 'settings' -- Store all config or script files

#### 'modules' -- Store all Python plug-in features to 'main.py' and 'cases.py'

#### 'resources' -- Icon or images for Test Case might use.

-------------------------------------------------------------------
Files definition:
-------------------------------------------------------------------

#### 'main.robot' -- Use to lunch the Robot for Testing
    CMD : 'robot main.robot'
    
    Description:
        Define Test sequence by list all Test_Case in this file.
        Each block define the Test_Case entry name, e.q. "cOpenSysCOM", 
        it should map to the file 'cases.robot' for item "OpenSysCOM".
        The detail of what does each Test Case should do, should be defined in 'cases.robot'
        
        e.q.
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │*** Settings ***                                                             │
        │Resource    cases.robot  <-- Included cases.robot                            │
        │                                                                             │
        │*** Test Cases ***                                                           │
        │cOpenSysCOM              <-- Define Test Case name                           │
        │    OpenSysCOM           <-- KeyWord defined in cases.robot                  │
        │...                                                                          │
        │...                                                                          │
        │... (More Test Cases)                                                        │
        └─────────────────────────────────────────────────────────────────────────────┘


<br>
#### 'cases.robot' -- Define all test case keyword, should be load by 'main.robot'
    CMD : Should not be executed
    
    Description:
        If you want to change or modify test case behavior, please modify here.
        Like log to console, how to make Robot though this Test Cast is "PASS" or "FAIL"



<br>
#### 'main.py' -- Python code entry point for 'main.robot'
    CMD : 'python main.py <index_of_Test_Case>
    (could be execute in python for debug propose)
    
    Description:
        Decide to run which method accroding to the argument passed in.
        This <index_of_Test_Case> should be set in 'cases.robot'
        Here's a function mapping table named 'func_list'.
        Modify this table to add/delete mapping function if need.

        e.q.
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │func_list = {                                                                │
        │    '1' : items.OpenSysCOM,                                                  │
        │    '2' : items.WaitBootComplete,                                            │
        │    '3' : items.ChkBootFromBIOS1, #shell cmd                                 │
        │    '4' : items.ChkBootFromBIOS2, #shell cmd                                 │
        │    '5' : items.InitBT, #shell cmd                                           │
        │    '6' : items.DeinitBT, #shell cmd                                         │
        │    '7' : items.ChkSimCardExist, #shell cmd                                  │
        │    '8' : items.Chk3GRF, #shell cmd, argument                                │
        │    '9' : items.LightBar,                                                    │
        │    '10' : items.ExternalGps, #shell cmd                                     │
        │    '11' : items.ChkeMMC #shell cmd                                          │
        │}                                                                            │
        └─────────────────────────────────────────────────────────────────────────────┘
        
        and then using following command to call the function.
        # ret = func_list[index]()



<br>
#### 'cases.py' -- Python code for all Test Cases.
    CMD : Should not be executed
    
    Description:
        Detail Python code for each part of Test Cases.
        Should be called from 'main.py', do not call this directlly.
        Here's main process for the testing, implement code here to add/delete feature.
        
        Each function should return (0 : FAIL / 1 : PASS) to 'main.py'



<br>
#### 'settings' > 'config.ini' -- Record configuration for testing process.
    CMD : Should not be executed
    (Refered from 'modules' > 'comPort.py' and 'configParser.py')
    
    Description:
        Should be written in following format:
        ┌────────────────────────────────┐
        │ [Category]                     │  <-- CATEGORY_NAME
        ├────────────────────────────────┤
        │ OPTION1 = VALUE1               │  <-- OPTION_NAME
        │ OPTION2 = VALUE2               │
        │ ...                            │
        └────────────────────────────────┘
        <or>
        ┌────────────────────────────────┐
        │ [Category]                     │
        ├────────────────────────────────┤
        │ OPTION1 : VALUE1               │
        │ OPTION2 : VALUE2               │
        │ ...                            │
        └────────────────────────────────┘
        
        Use following command to retrive value.
        
        # <VARIABLE> = config_parser.getValue(<CATEGORY_NAME>, <OPTION_NAME>)
        
        e.q.
        # abc = config_parser.getValue('Category', 'OPTION2')
        abc should be 'VALUE2'
        


<br>
#### 'modules' > 'comPort.py' -- Serial communicate with DUT via UART(COM).
    CMD : Should not be executed
    (Refered from 'cases.py')
    
    Description:
        Read 'config.ini' to set com port name and baudrate.
        Communicate with DUT via RS232 Com port.
        Should not been modified if possible, because it only provide basic functions 
        to 'cases.py'.

        ┌────────────────────────────────┐
        │ [COMPortSetting]               │
        ├────────────────────────────────┤
        │ COM_System = COM3              │
        │ COM_BaudRate = 115200          │
        │ COM_TimeOut = 3                │
        └────────────────────────────────┘



<br>
#### 'modules' > 'configParser.py' -- Read configuration from 'config.ini'.
    CMD : Should not be executed
    (Refered from 'cases.py')
    
    Description:
        Read 'config.ini' to load all arguments to run test process.
        All the data will be stored in 'config_dict' variables in dictionary format.
        Use method 'getValue(<CATEGORY_NAME>, <OPTION_NAME>)' to retrive value. (Case senstive)
        
        e.q. 
        In 'config.ini'.
        ┌────────────────────────────────┐
        │ [COMPortSetting]               │  <-- CATEGORY_NAME
        ├────────────────────────────────┤
        │ COM_System = COM3              │  <-- OPTION_NAME
        │ COM_BaudRate = 115200          │
        │ COM_TimeOut = 3                │
        └────────────────────────────────┘
        
        ```
        In 'cases.py' or any place need to get configuration.
        ```
        com_system = config_parser.getValue('COMPortSetting', 'COM_System') // COM3 (STRING)
        com_baudrate = config_parser.getValue('COMPortSetting', 'COM_BaudRate') // 115200 (INT)
        com_timeout = config_parser.getValue('COMPortSetting', 'COM_TimeOut') // 3 (INT)
        ```


<br>
#### 'modules' > 'gui.py' -- Launch GUI dialog for testing process.
    CMD : Should not be executed
    (Refered from 'cases.py')
    
    Description:
        A simple GUI dialog to show information to user.
        The dialog element is shown below:
        (Icon should be in 'png' format!!!)

        ┌────────────────────────────┬───┐
        │ <Dialog Title>             │ X │
        ├────────────────────────────┴───┤
        │ <Dialog Display Text>          │
        ├────────────────────────────────┤
        │ <Dialog Display Icon>          │ 
        ├───────────────┬────────────────┤
        │ <OK button>   │<Cancel button> │
        └───────────────┴────────────────┘

        e.q.
        In 'cases.py' or any place need to get configuration.

        * UI
        # argu = {'mText' : 'Check Light Bar', 'mImgSrc' : 'DFC_LIGHTBAR.png', 'mBtnOk' : 'PASS', 'mBtnCancel' : 'FAIL', 'mTitle' : 'Light Bar'}
        # mUI = gui.UI(argu)
        # mUI.onRender()
        
        # if mUI.mOk == True:
        #     return 1
        # else:
        #     return 0

        This may construct a new dialog and popup in front of all windows contained below message.

        ┌────────────────────────────┬───┐
        │ Light Bar                  │ X │
        ├────────────────────────────┴───┤
        │ Check Light Bar                │
        ├────────────────────────────────┤
        │ Icon 'DFC_LIGHTBAR.png'        │ 
        ├───────────────┬────────────────┤
        │ PASS          │ FAIL           │
        └───────────────┴────────────────┘

        if user click 'x' or 'FAIL' to terminate window, it will return '0'.
        Otherwise, once click 'PASS', it will return '1'.



<br>
#### 'modules' > 'logger.py' -- Store log into file or pass it to somewhere.
    CMD : Should not be executed
    (Refered from 'cases.py' and 'main.py')
    
    Description:
        In charge of written information to a log file.
        All the output log will be buffered in 'record' variable in list format.

        Once the test process execution complete, call 'report_gen' method,
        it should dump all message in 'record' to specific file.

        * The logger's attribute could be set in 'config.ini', the content as shown in below.

        ┌────────────────────────────────┐
        │ [LogFile]                      │
        ├────────────────────────────────┤
        │ Disable = 0                    │
        │ Directory = RobotLog           │
        │ LogName = log.txt              │
        │ TimeStamp = 1                  │
        │ FileStamp = 1                  │
        │ FuncStamp = 1                  │
        │ LineStamp = 1                  │
        └────────────────────────────────┘

        * Flag definition:
        
        Disable : Do not output log message to file. (0/1)
        Directory : Which directory should log file been saved. (STRING)
        LogName : Log filename (STRING)
        TimeStamp : Display the timestamp for each log message. (0/1)
        FileStamp : Show the filename which print out this log message. (0/1)
        FuncStamp : Show the function'name which print out this log message. (0/1)
        LineStamp : Show the column number in file which print out this log message. (0/1)



<br>
#### 'modules' > 'timerTasker.py' -- In charge of multi-threading for test process
    CMD : Should not be executed
    (Refered from 'cases.py')
    
    Description:
        Each Test Case has its timeout to execute some command, or maybe some 
        timeout for waiting DUT response.

        Use this 'timerTasker.py' to count a period, and trigger timeout if necessary.

        e.q.
        ┌───────────────────────────────────────────────────────────────────────────────────────────┐
        │ tSec = self.config_parser.getValue('TimeOut', 'WaitBoot')                                 │
        │ self.timer_tasker.setTimeOut(int(tSec))                                                   │                                               
        │ self.timer_tasker.start() // The timer start to count down according to WaitBoot's value. │
        │                                                                                           │
        │  while True:                                                                              │
        │      <Do something here...>                                                               │
        │      if self.timer_tasker.getTimeUp() is True: // Time's up                               │
        │          print("Timeout!!! leave")                                                        │
        │          self.timer_tasker.stop()                                                         │
        │          return 0 // report failed to someone                                             │ 
        │                                                                                           │
        └───────────────────────────────────────────────────────────────────────────────────────────┘


<br>
![image](http://gitlab.adlinktech.com/sourcecode_for_projects/SM_Gen_2.1_Robot_Framework/raw/99b0efe0d61a60d3af771249426f235c6d597190/resources/arch.png)
