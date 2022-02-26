# Author: Web Developer Kanai
# URI: https://devsecit.com
import pyautogui as gui
from time import sleep
import time
import sys

ur = input("Enter facebook profile url ")
cnt = int(input("How many posts will reacted ? "))
emotion = int(input("What will be emotion ? \n1. Like \n2.Love\n3.Care\n4.Haha\n5.Wow\n6.Sad\n7.Angry\n"))

print('Switch fast to your browser where your facebook account is logged in')


def countdown(t):
    while t > 0:
        sys.stdout.write('\rTimeout : {}s'.format(t))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)


countdown(10)
gui.press('f6')
gui.write(ur)
sleep(1)
gui.press('enter')
sleep(10)


def __MakeLike():
    gui.press('j')
    gui.press('l')
    for x in range(1, emotion):
        gui.press('right')
    gui.press('enter')
    sleep(2)


for v in range(0,cnt):
    __MakeLike()
