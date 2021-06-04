import time
from ethtools import *
from parameter import *

# simple API
def select_local_netcard():
    return Parameter.get_netcard_name(1)

def select_lp_netcard():
    return Parameter.get_netcard_name(0)

def input_parameter(speed: list, duplex: list):

    def division(i):
        configs = i.split("/")
        if configs[0] =="1000" and configs[1] == "half":
            return "1000_half"
        return configs

    config =[m +"/"+ n for m in speed for n in duplex]
    con = map(division, config)
    return list(con)

def get_speed():
    parameters = Parameter()
    speed = parameters.get_current_status().speed()
    return speed

def get_link():
    parameters = Parameter()
    link = parameters.get_current_status().link()
    return link

def get_duplex():
    parameters = Parameter()
    duplex = parameters.get_current_status().duplex()
    return duplex



def compare_result(speed, duplex,autoneg, config):

    result = Ethtool.show_verfication(speed, duplex, autoneg, config)
    return result


def get_status_list():
    parameters = Parameter()
    get_list =parameters.get_current_status().status_list()
    return get_list


def test():
    print("\033[0;31;40m Hello test case\033[0m")



# simple test case
def force_mode_test():
    speed = ["1000","100","10"]
    duplex = ["full","half"]

    local = select_local_netcard()
    lp = select_lp_netcard()
    config_list = input_parameter(speed, duplex)
    current_speed = get_speed()
    current_link = get_link()
    current_status = get_status_list()

    time_err_flag = 0

    for times in range(1):
        for setting in config_list:
            if setting == "1000_half":
                continue
            Ethtool.setup_force_mode(local, setting[0], setting[1])
            Ethtool.setup_force_mode(lp, setting[0], setting[1])
            time.sleep(1)
            if current_link == "yes":
                compare_result(setting[0], setting[1], "off", current_status)
            else:
                time_err_flag = time_err_flag +1
                print("link up timeout",time_err_flag)


def main():
    test()
    force_mode_test()

if __name__ == "__main__":
    main()
