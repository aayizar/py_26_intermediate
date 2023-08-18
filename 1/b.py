class User:
    def __init__(self, id, name, surname, phone, email) -> None:
        ...

def none_value_check(callback):
    def inner(id, name, surname, phone, email):
        if id == None:
            print('Айди не дана')
            return
        else:
            return callback(id, name, surname, phone, email)
        
    return inner



user_list = []

@none_value_check
def create_user(id, name, surname, phone, email):
    user_list.append( User(id, name, surname, phone, email) )