class ParameterBase():
    def __init__(self):
        pass

    def get_current_status(self):
        """
        speed | duplex | link up and down
        """
        raise NotImplemented

    def get_support_mode(self):
        """
        get_support_mode
        """
        raise NotImplemented
