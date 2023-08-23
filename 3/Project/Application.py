import keyboard
import time

from src.service.MainService import MainService


service = MainService()
while True:
    if keyboard.is_pressed('w'):
        service.create_new_user()
    if keyboard.is_pressed('o'):
        break
    
    print(".")
    time.sleep(0.2)