from colorama import Fore, Back, Style

BOLD = '\033[1m'


def printYellow(str, pre="", *args, **kwargs):
    print(Fore.YELLOW+pre+str+Style.RESET_ALL, *args, *kwargs)


def printGreen(str, pre="", *args, **kwargs):
    print(Fore.GREEN+pre+str+Style.RESET_ALL, *args, *kwargs)


def printRed(str, pre="", *args, **kwargs):
    print(Fore.RED+pre+str+Style.RESET_ALL, *args, *kwargs)
