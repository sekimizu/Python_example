class a:
    def __init__(self):
        print("Init a...")
        self.logger = []
    
    def getLogger(self):
        return self.logger

    def print_log(self):
        print("In a, print_log, logger size", len(self.logger))
        for line in self.logger:
            print("a > msg =", line)
        while len(self.logger) != 0:
            self.logger.pop()   
    
