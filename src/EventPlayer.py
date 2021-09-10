from src.helper import printGreen, printYellow, printRed, BOLD, progressBar

from pynput.mouse import Button, Controller as MouseController
import pyautogui
import json
import time
import threading


class EventPlayer:

    def __init__(self):
        self.mouse = MouseController()
        self.eventList = []
        self.correctionTime = 100000

    def getEvents(self, fileName):
        with open(f"savedRecordings/{fileName}.txt", 'r') as file:
            self.eventList = json.load(file)

    def playFile(self):
        timeCorrection = 0

        for i in range(len(self.eventList)):
            deltaShould = int(self.eventList[i]["time"])

            tStart = time.perf_counter_ns()

            time.sleep((deltaShould-timeCorrection)/10**9)

            threading.Thread(target=self.executeEvent,
                             args=(self.eventList[i],)).start()

            tEnd = time.perf_counter_ns()
            deltaActual = tEnd-tStart

            timeCorrection = deltaActual-deltaShould

    def executeEvent(self, event):
        if(event["group"] == "KEY"):
            if (event["type"] == "PRESS"):
                # self.keyboard.press(event["button"])
                pyautogui.keyDown(event["button"])

            elif (event["type"] == "RELEASE"):
                # self.keyboard.release(event["button"])
                pyautogui.keyUp(event["button"])

        elif(event["group"] == "MOUSE"):
            if (event["type"] == "PRESS"):
                if(event["button"] == "Button.left"):
                    pyautogui.mouseDown()
                elif(event["button"] == "Button.right"):
                    pyautogui.mouseDown(button="right")

            elif (event["type"] == "RELEASE"):
                if (event["button"] == "Button.left"):
                    pyautogui.mouseUp()
                elif(event["button"] == "Button.right"):
                    pyautogui.mouseUp(button="right")

    def startPlaying(self, filename, TIME_DELAY):
        self.getEvents(filename)
        printYellow(f"\nStart playing in {TIME_DELAY} seconds ...")
        progressBar(TIME_DELAY)
        printYellow("Start playing now ...\n")

        tstart = time.perf_counter_ns()

        self.playFile()

        print(time.perf_counter_ns()-tstart)

        printGreen(f"Replaying '{filename}' has finished.", pre=BOLD)
