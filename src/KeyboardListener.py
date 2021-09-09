from pynput.keyboard import Listener
from pynput import keyboard
import time


class KeyboardListener:

    def __init__(self, MouseListener, history):
        self.MouseListener = MouseListener
        self.tStartRecording = None
        self.history = history

        self.Listener = Listener(
            on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        print("PRESS:", key)

        if key == keyboard.Key.esc:
            self.history.append(
                (time.time()-self.tStartRecording, "KEY", "PRESS", str(key)))
        else:
            self.history.append(
                (time.time()-self.tStartRecording, "KEY", "PRESS", key))

    def on_release(self, key):
        print("RELEASE:", key)

        if key == keyboard.Key.esc:
            self.history.append(
                (time.time()-self.tStartRecording, "KEY", "PRESS", str(key)))
        else:
            self.history.append(
                (time.time()-self.tStartRecording, "KEY", "RELEASE", key))

        if key == keyboard.Key.esc:
            self.MouseListener.stop()
            return False
