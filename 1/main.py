from State import State
from User import User

from c import print_current_user


u1 = User(1, 'Nurzhan', 'Tangatarov', '+74324154143', 'nurzhan@gmail.com')
u2 = User(1, 'Aleksandr', 'Tangatarov', '+74324154143', 'nurzhan@gmail.com')

State.change_user(u1)
print_current_user()

State.change_user(u2)
print_current_user()