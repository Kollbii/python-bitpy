import pyautogui
from time import sleep

x = 10  #ilośc wiadomości

while True:
    pyautogui.typewrite("TO TYLKO WIADOMOSC")
    sleep(.500)
    pyautogui.typewrite("\n")
    sleep(2)
    x -= 1

    if x == 0:
        break
