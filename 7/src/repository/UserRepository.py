import json

from src.domain.User import User
from src.dto.UserDto import UserDto


class UserRepository:
    def __init__(self) -> None:
        self.dto = UserDto()
    
    
    def __get_data(self) -> None:
        try:
            path = 'src/db/users.json'
            data = None
            
            with open(path, 'r', encoding='utf8') as f:
                content = f.read()
                if content == '':
                    data = []
                else:
                    data: list = json.loads(content)

            return data
        except Exception as e:
            print(e)

    def __write_data(self, data):
        try:
            path = 'src/db/users.json'
            
            with open(path, 'w', encoding='utf8') as f_write:
                f_write.write(json.dumps(data, indent=2))
        except Exception as e:
            print(e)
    
    def __append_data(self, user):
        try:
            path = 'src/db/users.json'
            data = None
            
            with open(path, 'r', encoding='utf8') as f:
                content = f.read()
                if content == '':
                    data = []
                else:
                    data: list = json.loads(content)
            
            data.append(user)
            
            with open(path, 'w', encoding='utf8') as f_write:
                f_write.write(json.dumps(data, indent=2))
        except Exception as e:
            print(e)
    
    def __change_user_data(self, id: int, user: User):
        users = self.__get_data()
        for index, el in enumerate(users):
            if self.dto.EntityToUser(el).id == id:
                users[index] = self.dto.UserToEntity(user)

        self.__write_data(users)

    def create_new_user(self, user: User):
        content = self.dto.UserToEntity(user)
        self.__append_data(content)
    
    def change_password(self, id: int, new_password: str):
        count = 0
        for char in new_password:
            if char in '*_-+=&^%$#@!~':
                count += 1
        if count == 0:
            print('Слабый пароль. Добавь символ')
            return
        user = self.get_user(id)
        user.password = new_password
        self.__change_user_data(id, user)
    
    def get_user(self, id: int):
        users = self.__get_data()
        for el in users:
            if self.dto.EntityToUser(el).id == id:
                return self.dto.EntityToUser(el)

    def delete_user(self, id: int):
        users: list = self.__get_data()
        for el in users:
            if self.dto.EntityToUser(el).id == id:
                users.remove(el)
        self.__write_data(users)