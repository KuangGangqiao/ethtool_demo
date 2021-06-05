class EthtoolBase():

    def __init__(self):
        pass

    def setup_autoneg_mode(self, speed, dulpex, advertising, autoneg ="on"):
        """
        autoneg_mode
        """
        raise NotImplemented

    def setup_force_mode(self, speed, duplex, advertising, autoneg = "off"):
        """
        force_mode
        """
        raise NotImplemented



