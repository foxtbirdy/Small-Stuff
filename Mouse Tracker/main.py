import  pyautogui
import time

def greetings():
    print("Please press Crtl + C to quit..")
    time.sleep(3)
    print("Mouse Tracker beginning in 5 seconds...")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
 
greetings()

try:
    while True:
        x,y = pyautogui.position()
        positionData = "X: "+ str(x) + " Y: " + str(y) + "\n"
        print(positionData, end="")
except KeyboardInterrupt:
    print("\nProgram Terminated.")
