from colorama import Fore, Back, Style


def printYellow(str, *args, **kwargs):
    print(Fore.YELLOW+str+Style.RESET_ALL, *args, *kwargs)


def printGreen(str, *args, **kwargs):
    print(Fore.GREEN+str+Style.RESET_ALL, *args, *kwargs)
