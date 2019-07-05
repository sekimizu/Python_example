import configparser as cp
import re

class myConfigParser:
    def __init__(self, filename = "./settings/config.ini"):
        self.config = cp.ConfigParser()
        # remove space and tab if exist
        self.config.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
        self.config.read(filename)
        self.config_dict = {}

    # read all options from each secions
    def parserConfig(self):
        section_len = len(self.config.sections())
        if section_len == 0:
            print("No valid section found in config file")
            return

        for section in self.config.sections():
            self.config_dict[section] = {}
            options = self.config.options(section)
            for option in options:
                value = self.config.get(section, option, vars=None)
                self.config_dict[section][option] = value
                #print("Set dict[{0}][{1}] = {2}".format(section, option, value))

    # dump all config content
    def printConfigAll(self):
        print(self.config_dict)

    # dump all config sections
    def printDicts(self):
        for item in self.config_dict:
            print("-->", item)

    # dump all config options in specific section
    def printOptions(self, section_name):
        if section_name in self.config_dict:
            for option in self.config_dict[section_name]:
                value = self.config_dict[section_name][option]
                print("Read [{0}][{1}] = {2}".format(section_name, option, value))

if __name__ == '__main__':
    mCP = myConfigParser()
    mCP.parserConfig()
    
    # print for debug
    #mCP.printConfigAll()
    #mCP.printDicts()
    #mCP.printOptions("COMPortSetting")