import time
from ethtools import *
from parameter import *
import itertools

# simple API
def get_ethtool_log(netcard):
    Ethtool.ethtool_log(netcard)

def update_ethtool_log():
    pass

def local_netcard():
    return Parameter.get_netcard_name(1)

def lp_netcard():
    return Parameter.get_netcard_name(0)

def force_parameter(speed: list, duplex: list):

    def division(i):
        configs = i.split("/")
        if configs[0] =="1000" and configs[1] == "half":
            return "1000/half"
        return configs

    config =[m +"/"+ n for m in speed for n in duplex]
    con = map(division, config)
    return list(con)

def autoneg_parameter(advertised):
    config = []
    combination = {}
    for i in range(1,len(advertised)+1):
        iter = itertools.combinations(advertised,i)
        for n in list(iter):
            m = max(n)
            s = sum(n)
            config.append(s)
            combination[s] = m
    return config, combination

def get_speed():
    Para = Parameter()
    speed = Para.Get_ethtool().speed()
    return speed

def get_link():
    Para = Parameter()
    link = Para.Get_ethtool().link()
    return link

def get_duplex():
    Para = Parameter()
    duplex = Para.Get_ethtool().duplex()
    return duplex



def compare_result(speed, duplex,autoneg, config):

    result = Ethtool.show_verfication(speed, duplex, autoneg, config)
    return result


def get_status_list():
    Para = Parameter()
    get_list =Para.Get_ethtool().status_list()
    return get_list


def test():
    print("\033[0;31;40m Hello test case\033[0m")
    d = {0x01:"10/half", 0x02:"10/full", 0x04:"100/half", 0x08:"100/full", 0x20:"1000/full"}
    print(d.get(0x10))
    print(d[0x01])
    for key in d:
        print(key,":", d.get(key))


# simple test case
def force_mode_test():
    speed = ["1000", "100", "10"]
    duplex = ["full", "half"]
    second = 1
    config_list = force_parameter(speed, duplex)

    for times in range(1):
        for s in config_list:
            if s == "1000/half":
                continue
            Ethtool.setup_force_mode(local_netcard(), s[0], s[1])
            get_ethtool_log(local_netcard())
            Ethtool.setup_force_mode(lp_netcard(), s[0], s[1])
            time.sleep(second)
            if get_link() == "yes":
                print("s",s[0],s[1],"get_status",get_status_list() ,"link", get_link())
                compare_result(s[0], s[1], "off", get_status_list())
            else:
                print(f"\033[0;31;40m {s[0]}/{s[1]} link up timeout: {second}s\033[0m")

def autoneg_mode_test():
    advertised = [0x01,0x02,0x04,0x08,0x20]
    config_list = autoneg_parameter(advertised)
    second = 1

    for times in range(1):
        for s in config_list:
            if s == "1000/half":
                continue
            Ethtool.setup_autoneg_mode()

def main():
    test()
    advertised = [0x01,0x02,0x04,0x08,0x20]
    s = autoneg_parameter(advertised)
    print(s)
#    force_mode_test()

if __name__ == "__main__":
    main()
