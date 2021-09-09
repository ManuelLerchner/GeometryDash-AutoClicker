from pynput.mouse import Listener


class MouseListener:

    def __init__(self):
        self.Listener = Listener(on_click=self.on_click)


    def on_click(self, x, y, button, pressed):
        print(x, y, button, pressed)

    def stop(self):
        self.Listener.stop()
