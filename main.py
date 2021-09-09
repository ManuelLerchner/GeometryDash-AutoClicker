import time
from colorama import Fore, Style
import os.path

from src.helper import printGreen, printYellow, printRed, BOLD
from src.KeyboardListener import KeyboardListener
from src.MouseListener import MouseListener


TIME_DELAY = 2


def saveDataToFile(fileName, data):
    printYellow("Saving Data ...")

    filenameCount = 1
    newFileName = "savedRecordings/"+fileName+".txt"

    while True:
        if not os.path.isfile(newFileName):
            break
        newFileName = "savedRecordings/"+fileName+"_"+str(filenameCount)+".txt"
        filenameCount += 1

    with open(newFileName, 'w') as file:
        for item in data:
            file.write(f"{item}\n")


if __name__ == '__main__':
    history = []
    ML = MouseListener(history)
    KL = KeyboardListener(ML, history)

    print("-"*32)
    printYellow("Started Recorder")

    # Input filename
    filename = str(input(Fore.GREEN+"Enter Record-Name: "+Style.RESET_ALL))

    # Wait Time
    printYellow(f"\nStart listening in {TIME_DELAY} seconds ...")
    printRed("Stop Recording with ESC-Key", pre=BOLD)
    time.sleep(TIME_DELAY)
    printYellow("Start listening now ...\n")

    # Start Listener Threads
    ML.Listener.start()
    KL.Listener.start()

    KL.tStartRecording = time.time()
    ML.tStartRecording = time.time()

    # Wait until finished Recording
    ML.Listener.join()
    KL.Listener.join()

    printYellow("\nFinish Recording")

    # save Data
    saveDataToFile(filename, history)

    printGreen(f"'{filename}' has been saved", pre=BOLD)
