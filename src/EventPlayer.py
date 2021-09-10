import threading
from src.helper import printGreen, printYellow, printRed, BOLD

from pynput.mouse import Button, Controller as MouseController
import pyautogui
import json
import time


class EventPlayer:

    def __init__(self):
        self.mouse = MouseController()
        self.eventList = []
        self.correctionDelta = 200000

    def getEvents(self, fileName):
        with open(f"savedRecordings/{fileName}.txt", 'r') as file:
            self.eventList = json.load(file)

    def playFile(self):

        startTime = time.time_ns()

        currentIndex = 0
        while currentIndex < len(self.eventList):
            if(time.time_ns()-startTime+self.correctionDelta >= int(self.eventList[currentIndex]["time"])):

                threading.Thread(target=self.executeEvent,
                                 args=(
                                     self.eventList[currentIndex],)
                                 ).start()

                delta = (time.time_ns()-startTime -
                         int(self.eventList[currentIndex]["time"]))

                self.correctionDelta = self.lerp(
                    self.correctionDelta, delta, 0.8)

                currentIndex += 1

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

    def lerp(self, a, b, t):
        return a*(1-t)+b*t

    def printEventList(self):
        for event in self.eventList:
            print(event)

    def startPlaying(self, filename, TIME_DELAY):
        self.getEvents(filename)
        printYellow(f"\nStart playing in {TIME_DELAY} seconds ...")
        time.sleep(TIME_DELAY)
        printYellow("Start playing now ...\n")

        self.playFile()

        printGreen(f"Replaying '{filename}' has finished.", pre=BOLD)
