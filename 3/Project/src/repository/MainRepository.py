from src.domain.User import User
from src.dto.UserDto import UserDto 


class MainRepository:
    def __init__(self) -> None:
        self.userDto = UserDto()
        self.user = None
    
    def create_new_user(self, user) -> User:
        """
        Сохранить пользователя в базе данных        
        """
        self.user = self.userDto.fromUserToEntity(user)
        print("Success. New user:", self.user)
        return user