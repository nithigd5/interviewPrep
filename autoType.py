import pyautogui
import time
import sys
import os
 

filename = sys.argv[1]
if not os.path.exists(filename):
    print("File Not Exists")
    exit(0)
print("Reading File and typing file...")
timeLeft = 3
for i in range(timeLeft, 0, -1):
    print(f"Time Left: {i}")
    time.sleep(1)
for line in open(filename, "r"):
    line = line.strip()
    l = list(line)
    
    for i in line:
        # if(i=="}"):
        #     pyautogui.press("down")
        #     pyautogui.press("enter")
        # else:
         pyautogui.write(i)
         
        # time.sleep(0.0001)
    pyautogui.press("enter")
print("File typed successfully")