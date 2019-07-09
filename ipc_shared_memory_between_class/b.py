class b:
    def __init__(self):
        print("Init b...")
    
    def operation(self, cmd, logger):
        print("Write cmd", cmd, "to", logger)
        logger.append(cmd)

