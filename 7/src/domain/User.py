import random


class User:
    def __init__(self, name: str, surname: str, phone: str, email: str, password: str, id=random.randint(100000, 999999)) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password = password
