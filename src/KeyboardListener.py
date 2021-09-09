from pynput.keyboard import Listener
from pynput import keyboard
import time

from src.helper import makeDict


class KeyboardListener:

    def __init__(self, MouseListener, history):
        self.MouseListener = MouseListener
        self.tStartRecording = None
        self.history = history

        self.Listener = Listener(
            on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        print("PRESS:", key)

        if key in [keyboard.Key.esc, keyboard.Key.space]:
            self.handleEvent("PRESS", str(key))
        else:
            self.handleEvent("PRESS", key)

    def on_release(self, key):
        print("RELEASE:", key)

        if key in [keyboard.Key.esc, keyboard.Key.space]:
            self.handleEvent("RELEASE", str(key))
        else:
            self.handleEvent("RELEASE", key)

        if key == keyboard.Key.esc:
            self.MouseListener.stop()
            return False

    def handleEvent(self, event, key):
        self.history.append(makeDict(time.time()-self.tStartRecording,
                                     "KEY", event, key))
