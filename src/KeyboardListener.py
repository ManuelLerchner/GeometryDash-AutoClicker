import threading
from pynput.keyboard import Listener
from pynput import keyboard
import time

from src.helper import makeDict


class KeyboardListener:

    def __init__(self, MouseListener, history):
        self.MouseListener = MouseListener

        self.history = history

        self.Listener = Listener(
            on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        #print("PRESS:", key)
        threading.Thread(target=self.handlePress, args=(key,)).start()

    def on_release(self, key):
        #print("RELEASE:", key)

        threading.Thread(target=self.handleRelease, args=(key,)).start()

        if key == keyboard.Key.esc:
            self.MouseListener.stop()
            return False

    def handleRelease(self, key):
        if key in [keyboard.Key.esc, keyboard.Key.space, keyboard.Key.enter]:
            self.handleEvent("RELEASE", str(key).split(".")[1])
        else:
            self.handleEvent("RELEASE", str(key).replace("'", ""))

    def handlePress(self, key):
        if key in [keyboard.Key.esc, keyboard.Key.space, keyboard.Key.enter]:
            self.handleEvent("PRESS", str(key).split(".")[1])
        else:
            self.handleEvent("PRESS", str(key).replace("'", ""))

    def handleEvent(self, event, key):
        delta = time.perf_counter_ns()-self.MouseListener.tStartRecording
        self.MouseListener.tStartRecording = time.perf_counter_ns()

        self.history.append(
            makeDict(delta, "KEY", event, key))
