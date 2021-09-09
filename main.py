from colorama import Fore, Style
from src.helper import printGreen, printYellow

from src.KeyboardListener import KeyboardListener
from src.MouseListener import MouseListener


def saveDataToFile():
    printYellow("Saving Data...")
    return


if __name__ == '__main__':
    ML = MouseListener()
    KL = KeyboardListener(ML)

    print("-"*32)
    printYellow("Started Recorder")

    # Input filename
    filename = str(input(Fore.GREEN+"Enter Record-Name: "+Style.RESET_ALL))

    printYellow("Start listening now ...\n")

    # Start Listener Threads
    ML.Listener.start()
    KL.Listener.start()

    # Wait untill finished Recording
    ML.Listener.join()
    KL.Listener.join()

    printYellow("\nFinish Recording")

    # save Data
    saveDataToFile()

    printGreen(f"'{filename}' has been saved")
