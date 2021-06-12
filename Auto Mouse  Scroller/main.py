import pyautogui
import time
import keyboard
import os
# Safety first
pyautogui.FAILSAFE = True
# greet
user_notify = 'This is only a concept DEMO\nAt want speed you want to read?\n1. Fast\n2. Normal\n3. Slow\n4. Very Slow'
# alert
alert_text = "The program is about to start. Relocate your mouse on the position for the scrolling to work. This program will be excueted in 3 seconds after the [OK] is pressed.\nTo stop this program, click shift on your keyboard. You can also use the Crtl+C on terminal to manually stop the scrolling."
# abort
abort_text = "The program was aborted. Thanks for testing."
# Ask user the speed of the program
user_input = int(pyautogui.prompt(text=user_notify, title='Program Setup' , default='Choose Index'))


try:
	if user_input:
		pyautogui.alert(text=alert_text, title="Program Alert")
		time.sleep(3)

		while True:
			if keyboard.is_pressed('shift'):
				pyautogui.alert(text=abort_text, title="Program Aborted")
				break
			elif user_input == 4:
				pyautogui.scroll(-5)
			elif user_input == 3:
				pyautogui.scroll(-10)
			elif user_input == 2:
				pyautogui.scroll(-15)
			elif user_input == 1:
				pyautogui.scroll(-20)
			else:
				pyautogui.alert(text='Invalid Input', title="Program Aborted")		



except KeyboardInterrupt: # Exception handling
	pyautogui.alert(text=abort_text, title="Program Aborted by hotkey")

