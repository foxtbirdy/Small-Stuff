import  pyautogui
import time
try:
    while True:
        x,y = pyautogui.position()
        positionData = "X: "+ str(x) + " Y: " + str(y) + "\n"
        print(positionData, end="")
except KeyboardInterrupt:
    print("\nProgram Terminated.")
