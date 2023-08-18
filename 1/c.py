from State import State
from User import User

def print_current_user():
    u: User = State.user
    print(f'Class User:\n  self.id: {u.id}\n  self.name: {u.name}\n  self.surname: {u.surname}')