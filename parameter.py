from parameterbase import *
import re

class Parameter(ParameterBase):
    def __init__(self):
        pass

    class get_current_status():
        """
        speed | duplex | link | AN
        """
        def __init__(self):
            pass

        def speed(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                print("====speed====")
                for line in f.readlines():
                    speed = re.findall(r"Speed:\s*(\d+)", line);
                    if len(speed):
                        return speed[0]

        def duplex(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                print("====duplex====")
                for line in f.readlines():
                    duplex = re.findall(r"Duplex:\s*(\w+)", line);
                    if len(duplex):
                        if duplex[0] not in ["Full", "Half"]:
                            raise "ethtool log duplex is illegal"
                        duplexs = duplex[0].lower()
                        return duplexs

        def autoneg(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                print("====duplex====")
                for line in f.readlines():
                    autoneg = re.findall(r"Auto-negotiation:\s*(\w+)", line);
                    if len(autoneg):
                        if autoneg[0] not in ["on", "off"]:
                            raise "ethtool log autoneg is illegal"
                        return autoneg[0]

        def link(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                print("====duplex====")
                for line in f.readlines():
                    link = re.findall(r"Link detected:\s*(\w+)", line);
                    if len(link):
                        if link[0] not in ["yes", "no"]:
                            raise "ethtool log link is illegal"
                        return link[0]

        def status_list(self):
            lists =[]
            if self.speed() =="1000" and self.duplex() == "half":
                raise "Don't support 1000M|half"
            lists.append(self.speed())
            lists.append(self.duplex())
            lists.append(self.autoneg())
            return lists



    @classmethod
    def get_netcard_name(self, flag: int):
        """
        I thought of a simple algorithm to
        automatically get the name of the
        network card
        """
        self.flag = flag
        if self.flag:
            return "enp2s0"

        else:
            return "enp4s6"

    def get_support_mode(self):
        return "hello get_support"
