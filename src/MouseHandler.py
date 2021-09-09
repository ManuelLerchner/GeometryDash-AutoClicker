from pynput.mouse import Button, Controller

class MouseHandler:

    def __init__(self, fileName):
        mouse = Controller()
    
    

    def mouseEvent(self, x,y,button,eventType):
        self.mouse.position(x,y)

        if not eventType:
            self.mouse.release(button)
        
        if eventType:
            self.mouse.press(button)