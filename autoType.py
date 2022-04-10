import pyautogui
import time
import sys
 
time.sleep(3)

filename = sys.argv[1]
 
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
    