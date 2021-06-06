import os

class Ifconfig():
    def __init__():
        pass

    @classmethod
    def setup_power(netcard_name: str, flag: str):
        cls.netcard_name = netcard_name
        cls.flag = flag
        os.system(f"sudo ifconfig {cls.netcard_name} {cls.flag}")
