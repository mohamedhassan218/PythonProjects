import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import sys

# Get the length and width of the screan.
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# Ensure that the user has sent the number of minutes in the argument list.
if len(sys.argv) < 2:
    print("Sorry, you must specify the number of minutes of the record!")
    sys.exit()
    
screan = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", f, 30.0, screan)
now_time = time.time()
duration = int(sys.argv[1]) * 60
end_time = now_time + duration


while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break

output.release()
print("Recording Finished")