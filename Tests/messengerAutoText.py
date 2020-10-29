import pyautogui
from time import sleep

x = 15  #ilośc wiadomości

while True:
    pyautogui.typewrite("KRYSTIAN SPOKOJNIE TO WIĘCEJ TESTOW")
    sleep(.100)
    pyautogui.typewrite("\n")
    sleep(0.5)
    x -= 1

    if x == 0:
        break
