from User import User

class State:
    def __init__(self) -> None:
        self.user:User = None
    
    @classmethod
    def change_user(self, user: User):
        self.user = user