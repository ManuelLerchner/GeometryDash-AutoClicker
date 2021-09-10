from colorama import Fore, Back, Style
import os
import json

BOLD = '\033[1m'


def printYellow(str, pre="", *args, **kwargs):
    print(Fore.YELLOW+pre+str+Style.RESET_ALL, *args, *kwargs)


def printGreen(str, pre="", *args, **kwargs):
    print(Fore.GREEN+pre+str+Style.RESET_ALL, *args, *kwargs)


def printRed(str, pre="", *args, **kwargs):
    print(Fore.RED+pre+str+Style.RESET_ALL, *args, *kwargs)


def makeDict(time, group, type, button):
    return {"time": str(time), "group": group, "type": type, "button": button}


def saveDataToFile(fileName, history, overwrite):
    printYellow("Saving Data ...")

    if not os.path.exists("savedRecordings"):
        os.makedirs("savedRecordings")

    filenameCount = 1
    newFileName = "savedRecordings/"+fileName+".txt"

    while True and not overwrite:
        if not os.path.isfile(newFileName):
            break
        newFileName = "savedRecordings/"+fileName+"_"+str(filenameCount)+".txt"
        filenameCount += 1

    with open(newFileName, 'w') as file:
        json.dump(history, file)
