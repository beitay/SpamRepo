from pynput.keyboard import Key, Controller
import time

times_to_spam = input("Enter number of times to spam> ")

time.sleep(5)
i = 0
while i < int(times_to_spam):
    keyboard = Controller()
    # any letter
    keyboard.press('A')
    keyboard.release('A')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    i += 1
