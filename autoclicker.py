from pynput import keyboard
from pynput import mouse


def on_press(key):
    print(key)



def on_release(key):
    if key == keyboard.Key.esc:
        return False


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()  
    
wait_for_user_input()
