import os
from ethtoolbase import *

class Ethtool(EthtoolBase):

    def __init__(self):
        pass
    @classmethod
    def setup_an_mode(cls, speed, dulpex, advertising, autoneg ="on"):
        """
        an_mode
        """
        return "hello ethtool an_mode"
    @classmethod
    def setup_force_mode(cls, netcard_name: str, speed: str, duplex: str, autoneg = "off"):
        """
        force_mode
        """
        cls.speed = speed
        cls.duplex = duplex
        cls.autoneg = autoneg
        cls.netcard_name = netcard_name
        os.system(f"sudo ethtool -s {cls.netcard_name} speed {cls.speed} duplex {cls.duplex} autoneg {cls.autoneg}")

    @classmethod
    def show_verfication(cls, speed: str, duplex: str, autoneg: str, config: list):
        cls.speed = speed
        cls.duplex = duplex
        cls.autoneg = autoneg
        cls.config = config
        setting_err = 0
        if cls.speed not in cls.config:
            setting_err =setting_err + 1
            print("\033[1;31;40m speed is no correct\033[0m")
        if cls.duplex not in cls.config:
            setting_err =setting_err + 1
            print("\033[1;31;40m duplex is no correct\033[0m")
        if cls.autoneg not in cls.config:
            setting_err =setting_err + 1
            print("\033[1;31;40m autoeg is no correct\033[0m")
        if setting_err > 0:
            print(f"\033[1;31;40m Setup {cls.speed}M {cls.duplex} is fail\033[0m")
            return setting_err
        else:
            print(f"\033[1;32;40m Test {cls.speed}M {cls.duplex} is success\033[0m")
            return 0
    @classmethod
    def ethtool_log(cls, netcard_name: str):
        cls.netcard_name = netcard_name
        os.system(f"sudo ethtool {cls.netcard_name} > log.txt")
