from parameterbase import *
import re

class Parameter(ParameterBase):
    def __init__(self):
        pass

    class Get_ethtool():
        """
        speed | duplex | link | AN
        """
        def __init__(self):
            pass

        def speed(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    speed = re.findall(r"Speed:\s*(\d+)", line);
                    if len(speed):
                        return speed[0]

        def duplex(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    duplex = re.findall(r"Duplex:\s*(\w+)", line);
                    if len(duplex):
                        if duplex[0] not in ["Full", "Half"]:
                            raise "ethtool log duplex is illegal"
                        return duplex[0]

        def autoneg(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    autoneg = re.findall(r"Auto-negotiation:\s*(\w+)", line);
                    if len(autoneg):
                        if autoneg[0] not in ["on", "off"]:
                            raise "ethtool log autoneg is illegal"
                        return autoneg[0]

        def link(self):
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    link = re.findall(r"Link detected:\s*(\w+)", line);
                    if len(link):
                        if link[0] not in ["yes", "no"]:
                            raise "ethtool log link is illegal"
                        return link[0]

        def status_list(self):
            lists =[]
            if self.speed() =="1000" and self.duplex() == "Half":
                raise "Don't support 1000M/Half"
            lists.append(self.speed())
            lists.append(self.duplex())
            lists.append(self.autoneg())
            return lists

        def support_link():
            flag =""
            l =[]
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    support = re.findall(r"(?<=Supported link modes:)\s*(.+)", line);
                    if len(support):
                        flag = "support"
                    if flag == "support" and re.match(r"\s*(\d+)", line) != None:
                        support = (re.findall("\s*(.+)", line))
                    l = l + support
                    if re.search(r"Supported pause frame use:", line) != None:
                        return l

        def support_an():
            with open('log.txt','r', encoding='UTF-8') as f:
                for line in f.readlines():
                    support = re.findall(r"Supports auto-negotiation:\s*(\w+)", line);
                    for i in support:
                        return i


        def advertised_link():
            flag = ""
            l = []
            with open('log.txt','r', encoding='UTF-8'):
                for line in f.readlines():
                    ad = re.findall(r"(?<=Advertised link modes:)\s*(.+)", line);
                    if len(ad):
                        flag = "advertised"
                    if  flag == "advertised" and re.match(r"\s*(\d+)", line) != None:
                        ad = (re.findall("\s*(.+)", line))
                    l = l + ad
                    if re.search(r"Advertised pause frame use:", line) != None:
                        return l

        def advertised_an():
            with open('log.txt','r', encoding='UTF-8'):
                for line in f.readlines():
                    support = re.findall(r"Advertised auto-negotiation:\s*(\w+)", line);
                    for i in support:
                        return i

        def lp_advertised_link():
            flag = ""
            l = []
            f=open('log.txt','r', encoding='UTF-8')
            for line in f.readlines():
                lp_ad = re.findall(r"(?<=Link partner advertised link modes:)\s*(.+)", line);
                if len(lp_ad):
                    flag = "lp_advertised"
                if flag == "lp_advertised" and re.match(r"\s*(\d+)", line) != None:
                    lp_ad = (re.findall("\s*(.+)", line))
                l = l + lp_ad
                if re.search(r"Link partner advertised pause frame use:", line) != None:
                    return l

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
            return "enp2s0"

