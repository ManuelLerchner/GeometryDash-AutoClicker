from pynput.mouse import Listener
import time


class MouseListener:

    def __init__(self, history):
        self.Listener = Listener(on_click=self.on_click)
        self.tStartRecording = None
        self.history = history

    def on_click(self, x, y, button, pressed):

        self.history.append(
            (time.time()-self.tStartRecording, "MOUSE", "PRESS" if pressed else "RELEASE", str(button)))
        print(button, "PRESSED" if pressed else "RELEASED")

    def stop(self):
        self.Listener.stop()
