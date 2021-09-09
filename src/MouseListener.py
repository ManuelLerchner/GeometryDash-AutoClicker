from pynput.mouse import Listener
import time

from src.helper import makeDict


class MouseListener:

    def __init__(self, history):
        self.Listener = Listener(on_click=self.on_click)
        self.tStartRecording = None
        self.history = history

    def on_click(self, x, y, button, pressed):
        print("PRESSED" if pressed else "RELEASED", str(button))

        self.handleEvent(
            "PRESS" if pressed else "RELEASE", str(button))

    def stop(self):
        self.Listener.stop()

    def handleEvent(self, event, key):
        self.history.append(makeDict(time.time()-self.tStartRecording,
                                     "MOUSE", event, key))
