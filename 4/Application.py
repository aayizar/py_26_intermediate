import keyboard
import time

from src.service.SnakeService import SnakeService

height = 20
width = 40
service = SnakeService(height, width)

def login():
    ...

def game():
    while True:
        if keyboard.is_pressed('m'):
            break
        if keyboard.is_pressed('w'):
            service.change_direction('w')
        if keyboard.is_pressed('a'):
            service.change_direction('a')
        if keyboard.is_pressed('s'):
            service.change_direction('s')
        if keyboard.is_pressed('d'):
            service.change_direction('d')
        
        if service.snake_move():
            break
        
        service.check_snake_on_food()
        
        if service.is_snake_on_wall():
            break
            
        
        service.draw()
        time.sleep(0.5)
        


    print("Ваш счет составил:", service.get_score())

login()
game()