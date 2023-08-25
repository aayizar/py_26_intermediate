from src.domain.User import User
from src.dto.UserDto import UserDto 


class MainRepository:
    def __init__(self) -> None:
        self.userDto = UserDto()
        self.user = None
        self.score = 0
        self.maps = [
            [
                [0, 1],
                [0, 0]
            ]
        ]
    
    def increase_score(self, value):
        self.score += value
    
    def get_score(self):
        return self.score
    
    # def create_new_user(self, user) -> User:
    #     """
    #     Сохранить пользователя в базе данных        
    #     """
    #     self.user = self.userDto.fromUserToEntity(user)
    #     print("Success. New user:", self.user)
    #     return user