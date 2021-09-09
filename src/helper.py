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


def makeDict(time, type, event, button):
    return {"time": str(time), "group": type, "type": event, "button": button}


def saveDataToFile(fileName, history):
    printYellow("Saving Data ...")

    filenameCount = 1
    newFileName = "savedRecordings/"+fileName+".txt"

    while True:
        if not os.path.isfile(newFileName):
            break
        newFileName = "savedRecordings/"+fileName+"_"+str(filenameCount)+".txt"
        filenameCount += 1

    with open(newFileName, 'w') as file:
        json.dump(history, file)
