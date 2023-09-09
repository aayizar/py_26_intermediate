from src.domain.User import User


class UserDto:
    def UserToEntity(self, user: User) -> dict:
        return {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'email': user.email,
            'password': user.password
        }
    
    def EntityToUser(self, entity: dict) -> User:
        return User(
            entity['name'],
            entity['surname'],
            entity['phone'],
            entity['email'],
            entity['password'],
            entity['id'],
        )