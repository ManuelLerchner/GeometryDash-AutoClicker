from src.helper import printGreen, printYellow, printRed, BOLD

from pynput.mouse import Button, Controller as MouseController
import pyautogui
import json
import time


class EventPlayer:

    def __init__(self):
        self.mouse = MouseController()
        self.eventList = []

    def getEvents(self, fileName):
        with open(f"savedRecordings/{fileName}.txt", 'r') as file:
            self.eventList = json.load(file)


    def playFile(self):

        startTime = time.time()
        currentIndex = 0
        while currentIndex < len(self.eventList):
            if(time.time()-startTime >= float(self.eventList[currentIndex]["time"])):

                # Execute Event with Index "currentIndex"
                #print(currentIndex, self.eventList[currentIndex])
                self.executeEvent(self.eventList[currentIndex])
                currentIndex += 1

    def executeEvent(self, event):

        if(event["group"] == "KEY"):
            if (event["type"] == "PRESS"):
                # self.keyboard.press(event["button"])
                pyautogui.keyDown(event["button"])

            if (event["type"] == "RELEASE"):
                # self.keyboard.release(event["button"])
                pyautogui.keyUp(event["button"])

        if(event["group"] == "MOUSE"):
            if (event["type"] == "PRESS"):
                if(event["button"]=="Button.left"):
                    pyautogui.mouseDown()
                if(event["button"]=="Button.right"):
                    pyautogui.mouseDown(button="right")

            if (event["type"] == "RELEASE"):
                if(event["button"]=="Button.left"):
                    pyautogui.mouseUp()
                if(event["button"]=="Button.right"):                
                    pyautogui.mouseUp(button="right")

    def printEventList(self):
        for event in self.eventList:
            print(event)

    def startPlaying(self, filename, TIME_DELAY):
        self.getEvents(filename)
        printYellow(f"\nStart playing in {TIME_DELAY} seconds ...")
        printRed("Stop playing with ESC-Key", pre=BOLD)
        time.sleep(TIME_DELAY)
        printYellow("Start playing now ...\n")

        self.playFile()
