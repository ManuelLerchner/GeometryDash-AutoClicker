import time
from colorama import Fore, Style

from src.helper import printGreen, printYellow, printRed, BOLD
from src.KeyboardListener import KeyboardListener
from src.MouseListener import MouseListener


TIME_DELAY = 2


def saveDataToFile(fileName):
    printYellow("Saving Data ...")
    
    with open('fileName.txt', 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")

    return


if __name__ == '__main__':
    ML = MouseListener()
    KL = KeyboardListener(ML)

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

    # Wait until finished Recording
    ML.Listener.join()
    KL.Listener.join()

    printYellow("\nFinish Recording")

    # save Data
    saveDataToFile()

    printGreen(f"'{filename}' has been saved", pre=BOLD)
