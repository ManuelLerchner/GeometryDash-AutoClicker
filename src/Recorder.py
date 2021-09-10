import time
from colorama import Fore, Style
import os.path
import json

from src.helper import printGreen, printYellow, printRed, progressBar, saveDataToFile, BOLD
from src.KeyboardListener import KeyboardListener
from src.MouseListener import MouseListener


class Recorder:

    def __init__(self, overrite):
        self.history = []

        self.ML = MouseListener(self.history)
        self.KL = KeyboardListener(self.ML, self.history)
        self.overwrite = overrite

    def startRecording(self, TIME_DELAY, filename):

        print("-"*32)
        printYellow("Started Recorder")

        # Input filename
        if not filename:
            filename = str(
                input(Fore.GREEN+"Enter Record-Name: "+Style.RESET_ALL))

        # Wait Time
        printYellow(f"\nStart listening in {TIME_DELAY} seconds ...")
        printRed("Stop Recording with ESC-Key", pre=BOLD)
        # time.sleep(TIME_DELAY)
        progressBar(TIME_DELAY)
        printYellow("Start listening now ...\n")

        tstart = time.perf_counter_ns()

        # Start Listener Threads
        self.ML.Listener.start()
        self.KL.Listener.start()

        self.ML.tStartRecording = tstart

        # Wait until finished Recording
        self.ML.Listener.join()
        self.KL.Listener.join()

        printYellow("\nFinish Recording")
        print(time.perf_counter_ns()-tstart)

        # save Data
        saveDataToFile(filename, self.history, self.overwrite)

        printGreen(f"'{filename}' has been saved", pre=BOLD)
