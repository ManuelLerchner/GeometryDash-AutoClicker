from pynput.mouse import Listener
import time


class MouseListener:

    def __init__(self, history):
        self.Listener = Listener(on_click=self.on_click)
        self.tStartRecording = None
        self.history = history

    def on_click(self, x, y, button, pressed):

        self.history.append(
            (time.time()-self.tStartRecording, "PRESS" if pressed else "RELEASE", str(button)))
        print(x, y, button, pressed)

    def stop(self):
        self.Listener.stop()
