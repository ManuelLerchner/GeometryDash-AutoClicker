from pynput.keyboard import Listener
from pynput import keyboard
import time
import threading

from src.helper import makeDict


class KeyboardListener:

    def __init__(self, MouseListener, history):
        self.MouseListener = MouseListener
        self.tStartRecording = None
        self.history = history

        self.Listener = Listener(
            on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        #print("PRESS:", key)
        timeNS = time.time_ns()-self.tStartRecording
        threading.Thread(target=self.handlePress, args=(key, timeNS)).start()

    def on_release(self, key):
        #print("RELEASE:", key)

        timeNS = time.time_ns()-self.tStartRecording
        threading.Thread(target=self.handleRelease, args=(key, timeNS)).start()

        if key == keyboard.Key.esc:
            self.MouseListener.stop()
            return False

    def handlePress(self, key, time):
        if key in [keyboard.Key.esc, keyboard.Key.space, keyboard.Key.enter]:
            self.handleEvent(time, "PRESS", str(key).split(".")[1])
        else:
            self.handleEvent(time, "PRESS", str(key).replace("'", ""))

    def handleRelease(self, key, time):
        if key in [keyboard.Key.esc, keyboard.Key.space, keyboard.Key.enter]:
            self.handleEvent(time, "RELEASE",  str(key).split(".")[1])
        else:
            self.handleEvent(time, "RELEASE",  str(key).replace("'", ""))

    def handleEvent(self, time, event, key):
        self.history.append(makeDict(time,
                                     "KEY", event, key))
