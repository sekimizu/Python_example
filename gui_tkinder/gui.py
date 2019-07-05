import tkinter as tk

# ==================================================================================================
"""Caller"""
"""
# UI
    argu = {'mText' : 'Check Light Bar', 'mImgSrc' : 'led.png', 'mBtnOk' : 'PASS', 'mBtnCancel' : 'FAIL', 'mTitle' : 'Light Bar'}
    mUI = gui.UI(argu)
    mUI.onRender()

    if mUI.mOk == True:
        return 1
    else:
        return 0
"""
# ==================================================================================================
class UI:
    """
    self.mText = Str/None
    self.mImgSrc = Str/None
    self.mBtnOk = Str/None
    self.mBtnCancel = Str/None
    self.mTitle = Str/None
    """
    def __init__(self, argu):
        self.dict = argu
        self.mOk , self.mCancle = False, False
        self.root = tk.Tk()
        if 'mTitle' in self.dict and self.dict['mTitle'] != None:
            self.root.title(self.dict['mTitle'])
        else:
            self.root.title('NaN')
    
    def onRender(self):
        index = 0
        # Check if need to display text
        if 'mText' in self.dict and self.dict['mText'] != None:
            label_text = tk.Label(self.root, text = self.dict['mText']);
            label_text.grid(row = index, column = 0, columnspan = 2, sticky = tk.W + tk.E)
            index += 1
        
        # Check if need to display image
        if 'mImgSrc' in self.dict and self.dict['mImgSrc'] != None:
            img_png = tk.PhotoImage(file = self.dict['mImgSrc'])
            label_img = tk.Label(self.root, image = img_png)
            label_img.grid(row = index, column = 0, columnspan = 2, sticky = tk.W + tk.E)
            index += 1
        
        # Check if need to display OK button
        if 'mBtnOk' in self.dict and self.dict['mBtnOk'] != None:
            btn_ok = tk.Button(self.root, text = self.dict['mBtnOk'], command = self.clickOk)
            btn_ok.grid(row = index, column = 0, sticky = tk.W + tk.E + tk.S, padx = 5, pady = 5)
        
        # Check if need to display CANCEL button
        if 'mBtnCancel' in self.dict and self.dict['mBtnCancel'] != None:
            mBtnCancel = tk.Button(self.root, text = self.dict['mBtnCancel'], command = self.clickCancel)
            mBtnCancel.grid(row = index, column = 1, sticky = tk.W + tk.E + tk.S, padx = 5, pady = 5)
            
        self.root.mainloop()
        
    def onStop(self):
        if self.root != None:
            self.root.destroy()
    
    def clickOk(self):
        self.mOk = True
        self.onStop()
    
    def clickCancel(self):
        self.mCancel = True
        self.onStop()
        
# ==================================================================================================   

if __name__ == '__main__':
    argu = {'hasText' : False, 'mText' : 'Hello Welcome!', 'hasImg' : True, 'mImgSrc' : 'gundam.png', 'mBtnOk' : 'OK', 'mBtnCancel' : 'CANCEL', 'mTitle' : 'Hi'}
    mUI = UI(argu)
    mUI.onRender()
    
    print(" OK value : {0}".format(mUI.mOk))
    print(" CANCEL value : {0}".format(mUI.mCancel))
    print("FINISH...")
