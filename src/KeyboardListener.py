from pynput.keyboard import Listener
from pynput import keyboard


class KeyboardListener:

    def __init__(self, MouseListener):
        self.MouseListener = MouseListener

        self.Listener = Listener(
            on_press=self.on_press, on_release=self.on_release)

    def on_press(self, key):
        print("press", key)

    def on_release(self, key):
        print("release", key)

        if key == keyboard.Key.esc:
            self.MouseListener.stop()
            return False
