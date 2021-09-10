from pynput.mouse import Listener
import time
import threading

from src.helper import makeDict


class MouseListener:

    def __init__(self, history):
        self.Listener = Listener(on_click=self.on_click)
        self.tStartRecording = None
        self.history = history

    def on_click(self, x, y, button, pressed):
        #print("PRESSED" if pressed else "RELEASED", str(button))

        threading.Thread(target=self.handleClick,
                         args=(pressed, button)).start()

    def stop(self):
        self.Listener.stop()

    def handleClick(self, pressed, button):
        self.handleEvent(
            "PRESS" if pressed else "RELEASE", str(button))

    def handleEvent(self, event, key):
        delta = time.perf_counter_ns()-self.tStartRecording
        self.tStartRecording = time.perf_counter_ns()
        self.history.append(
            makeDict(delta, "MOUSE", event, key))
