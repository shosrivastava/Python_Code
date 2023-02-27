# Method 1:

""" print("This code is for sending an automated message.\n")

import time
import pyautogui

pyautogui.FAILSAFE = True

def sendMessage():
    time.sleep(10)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

sendMessage() """

#Method 2:

import time
import pyautogui

pyautogui.FAILSAFE = True
time.sleep(2)

while True:
    pyautogui.typewrite("Hey there..")
    time.sleep(3)
    pyautogui.press("Enter")
