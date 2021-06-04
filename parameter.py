from parameterbase import *

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
            return "100"

        def duplex(self):
            return "full"

        def autoneg(self):
            return "off"

        def link(self):
            return "up"

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
            return "enp0s25"

        else:
            return "enx0050b6c37e71"

    def get_support_mode(self):
        return "hello get_support"
