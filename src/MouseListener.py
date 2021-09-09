import threading
from pynput.mouse import Listener
import time

from src.helper import makeDict


class MouseListener:

    def __init__(self, history):
        self.Listener = Listener(on_click=self.on_click)
        self.tStartRecording = None
        self.history = history

    def on_click(self, x, y, button, pressed):
        #print("PRESSED" if pressed else "RELEASED", str(button))

        timeNS = time.time_ns()-self.tStartRecording
        threading.Thread(target=self.handleClick,
                         args=(button, pressed, timeNS)).start()

    def stop(self):
        self.Listener.stop()

    def handleClick(self, button, pressed, time):
        self.handleEvent(time,
                         "PRESS" if pressed else "RELEASE", str(button))

    def handleEvent(self, time, event, key):
        self.history.append(makeDict(time,
                                     "MOUSE", event, key))
