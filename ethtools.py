import os
from ethtoolbase import *

class Ethtool(EthtoolBase):

    def __init__(self):
        pass
    @classmethod
    def setup_autoneg_mode(cls, netcard_name: str, advertising: dict, autoneg ="on"):
        """
        autoneg_mode
        """
        cls.netcard_name = netcard_name
        cls.advertising = advertising
        cls.autoneg = autoneg

        os.system(f"sudo ethtool -s {cla.netcard_name} autoneg {cls.autoneg}")
        os.system(f"sudo ethtool -s {cls.netcard_name} advertise {cls.advertising}")

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
    def ethtool_log(cls, netcard_name: str):
        cls.netcard_name = netcard_name
        os.system(f"sudo ethtool {cls.netcard_name} > log.txt")

    @classmethod
    def show_verfication(cls, speed: str, duplex: str, autoneg: str, config: list):
        cls.speed = speed
        cls.duplex = duplex
        cls.autoneg = autoneg
        cls.config = config
        cls.err = 0
        if cls.speed not in cls.config:
            cls.err =cls.err + 1
            print("\033[1;31;40m speed is no correct\033[0m")
        if cls.duplex not in cls.config:
            cls.err =cls.err + 1
            print("\033[1;31;40m duplex is no correct\033[0m")
        if cls.autoneg not in cls.config:
            cls.err =cls.err + 1
            print("\033[1;31;40m autoneg is no correct\033[0m")
        if cls.err > 0:
            print(f"\033[1;31;40m Setup {cls.speed}M {cls.duplex} is fail\033[0m")
            return cls.err
        else:
            print(f"\033[1;32;40m Test {cls.speed}M {cls.duplex} is success\033[0m")
            return 0

