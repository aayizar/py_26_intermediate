from src.domain.User import User

class UserDto:
    def fromUserToEntity(self, user:User):
        return {
            "id": user.id,
            "name": user.name,
            "surname": user.surname,
            "phone": user.phone,
            "email": user.email
        }
    
    def fromEntityToUser(self, entity):
        return User(
            entity["id"],
            entity["name"],
            entity["surname"],
            entity["phone"],
            entity["email"],            
        )