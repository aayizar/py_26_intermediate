from src.repository.UserRepository import UserRepository
from src.domain.User import User

import json


repository = UserRepository()

# user1 = User(
#     'Nurzhan',
#     'Tangatarov',
#     '+77074862447',
#     'tangatarovnurzan@gmail.com',
#     'qwerty12'
# )

# repository.create_new_user(user1)

user_id = 365840
# user = repository.get_user(user_id)
# print(user.surname)

# user.surname = 'Mairam'
# repository.change_user_data(user_id, user)

repository.delete_user(user_id)
