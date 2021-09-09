from pynput.mouse import Button, Controller
from pynput import keyboard
import time


class EventPlayer:

    def __init__(self):
        self.mouse = Controller()
        self.eventList = []

    def getEvents(self, fileName):
        with open(f"savedRecordings/{fileName}.txt", 'r') as data:
            for line in data:
                event = line.strip()[1:-1].replace(' ',
                                                   '').replace("'", '').split(",")
                self.eventList.append(event)

    def playFile(self):
        startTime = time.time()
        print(startTime)
        currentIndex = 0
        while currentIndex < len(self.eventList):
            if(time.time()-startTime >= float(self.eventList[currentIndex][0])):

                # Execute Event with Index "currentIndex"
                print(currentIndex, self.eventList[currentIndex])
                self.executeEvent()
                currentIndex += 1

    def executeEvent(self, time, eventGroup, eventType, id):

        if(eventGroup == "KEY"):
            pass

        if(eventGroup == "MOUSE"):
            if eventType == "PRESS":
                self.mouse.press(button)

            if eventType == "RELEASE":
                self.mouse.release(button)

    def printEventList(self):
        for event in self.eventList:
            print(event)


EP = EventPlayer()

EP.getEvents("Test123")
EP.printEventList()
