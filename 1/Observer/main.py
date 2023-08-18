from time import sleep
import keyboard

  
class Observer():
  listeners = []
  
  @classmethod
  def add_listener(self, callback):
    self.listeners.append(callback)
  
  @classmethod
  def update(self, user):
    for listener in self.listeners:
      listener(user)

def update(callback):
  def inner():
    user = callback()
    Observer.update(user)
  return inner



class User:
  def __init__(self, id, name) -> None:
    self.id = id
    self.name = name
        
        
class Draw():
  def __init__(self) -> None:
    Observer.add_listener(self.print_user)
  
  def print_user(self, user: User):
    print(user.id, user.name)
 


  

@update
def change_user():
  global current_user
  id = int(input())
  name = input()
  current_user = User(id, name)
  return current_user


d1 = Draw()
d2 = Draw()

current_user = None

work = True
while work:
  if keyboard.is_pressed('w'):
    change_user()
  if keyboard.is_pressed('a'):
    print('a')
  if keyboard.is_pressed('s'):
    print('s')
  if keyboard.is_pressed('d'):
    print('d')
  if keyboard.is_pressed('q'):
    work = False

  sleep(0.5)