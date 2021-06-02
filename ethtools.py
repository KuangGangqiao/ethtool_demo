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
    def setup_force_mode(cls, speed, duplex, autoneg = "off"):
        """
        force_mode
        """
        os.system("sudo ethtool -s enp2s0 speed 10 duplex full autoneg off")
        print("hello ethtool force_mode")



