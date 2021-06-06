import time
import functools
from ethtools import *
from parameter import *
from ifconfig import *
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
        if configs[0] =="1000" and configs[1] == "Half":
            return "1000/Half"
        return configs

    config =[m +"/"+ n for m in speed for n in duplex]
    con = map(division, config)
    return list(con)

def autoneg_parameter(advertised):
    sum_to_list = {}
    combination = {}
    list2 =[]
    for i in range(1,len(advertised)+1):
        iter = itertools.combinations(advertised,i)
        for n in list(iter):
            m = max(n)
            s = sum(n)
            list2.append(n)
            combination[s] = m
            for b in list2:
                sum_to_list[s] = b
    return combination, sum_to_list

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

def force_compare_result(speed, duplex,autoneg, config):
    result = Ethtool.show_verfication(speed, duplex, autoneg, config)
    return result

def autoneg_compare_result(keys, config, adver_map):
    if config[0].get(keys) in adver_map:
        value = adver_map.get(config[0].get(keys))
        ad_speed = value.split("/")[0]
        ad_duplex = value.split("/")[1]
        print(f"autoneg result should be : {ad_speed}/{ad_duplex}")
    if ad_speed == get_speed() and ad_duplex ==get_duplex:
        print("\033[0;32;40m test success\033[0m")
    else:
        print("\033[0;31;40m test fail\033[0m")

    if keys in config[1]:
        for n in config[1].get(keys):
            if n in adver_map:
                values = adver_map.get(n)
                print(f"lp advertising: {values}")
        print("=================")

def power(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("start call %s():" % func.__name__)

        speed = ["1000", "100", "10"]
        duplex = ["Full", "Half"]
        second = 1
        config_list = force_parameter(speed, duplex)

        for times in range(1):
            for s in config_list:
                if s == "1000/Half":
                    continue

                res = func(*args, **kw)

                Ethtool.setup_force_mode(local_netcard(), s[0], s[1])
                Ethtool.setup_force_mode(lp_netcard(), s[0], s[1])
                time.sleep(second)
                get_ethtool_log(local_netcard())
                if get_link() == "yes":
                    print("s",s[0],s[1],"get_status",get_status_list() ,"link", get_link())
                    force_compare_result(s[0], s[1], "off", get_status_list())
                else:
                    print(f"\033[0;33;40m {s[0]}/{s[1]} link up timeout: {second}s\033[0m")

                    print("end call %s():" % func.__name__)
        return res
    return wrapper


def ifconfig_down():
   pass

def get_status_list():
    Para = Parameter()
    get_list =Para.Get_ethtool().status_list()
    return get_list


def test():
    print("\033[0;31;40m Hello test case\033[0m")
    d = {0x01:"10/Half", 0x02:"10/Full", 0x04:"100/Half", 0x08:"100/Full", 0x20:"1000/Full"}
    print(d.get(0x10))
    print(d[0x01])
    for key1 in d:
        print(key1,":", d.get(key1))

    advertised = [0x01,0x02,0x04,0x08,0x20]
    s = autoneg_parameter(advertised)
    print(s)

# simple test case
def force_mode_test():
    speed = ["1000", "100", "10"]
    duplex = ["Full", "Half"]
    second = 1
    config_list = force_parameter(speed, duplex)

    for times in range(1):
        for s in config_list:
            if s == "1000/Half":
                continue
            Ethtool.setup_force_mode(local_netcard(), s[0], s[1])
            Ethtool.setup_force_mode(lp_netcard(), s[0], s[1])
            time.sleep(second)
            get_ethtool_log(local_netcard())
            if get_link() == "yes":
                print("s",s[0],s[1],"get_status",get_status_list() ,"link", get_link())
                force_compare_result(s[0], s[1], "off", get_status_list())
            else:
                print(f"\033[0;33;40m {s[0]}/{s[1]} link up timeout: {second}s\033[0m")

def autoneg_mode_test():
    second = 1
    advertised = [0x01,0x02,0x04,0x08,0x20]
    config_list = autoneg_parameter(advertised)
    advertised_map = {0x01:"10/Half", 0x02:"10/Full", 0x04:"100/Half", 0x08:"100/Full", 0x20:"1000/Full"}

    for times in range(1):
        for key0 in config_list[0]:
            Ethtool.setup_autoneg_mode(local_netcard(), sum(advertised))
            Ethtool.setup_autoneg_mode(lp_netcard(), key0)
            time.sleep(second)
            get_ethtool_log(local_netcard())
            if get_link() == "no":
                autoneg_compare_result(key0, config_list, advertised_map)
            else:
                print("\033[0;33;40m Link Timeout\033[0m")

@power
def power_test():
    print("xxxx")


def test55():
    print("hello world")

def main():
    power_test()
#    test()
#    force_mode_test()
    autoneg_mode_test()
#    test55()

if __name__ == "__main__":
    main()
