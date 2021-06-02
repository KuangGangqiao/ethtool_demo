from ethtools import *
from parameter import *

def force_mode_test():
    Ethtool.setup_force_mode(1000, "full")

def main():
    force_mode_test()

if __name__ == "__main__":
    main()
