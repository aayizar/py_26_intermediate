from src.domain.User import User
from src.dto.UserDto import UserDto 

from src.repository.MainRepository import MainRepository


class MainService:
    def __init__(self) -> None:
        self.repository = MainRepository()
    
    def create_new_user(self) -> User:
        id = int(input())
        name = input()
        surname = input()
        phone = input()
        email = input()

        user = User(id, name, surname, phone, email)
        return self.repository.create_new_user(user)