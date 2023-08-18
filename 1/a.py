def zero_divide(callback):
    def inner(a, b):
        if b == 0:
            print('На ноль нельзя делить')
            return
        else:
            return callback(a, b)
        
    return inner


@zero_divide
def divide(a, b):
    print(a / b)
    
divide = zero_divide(divide)

divide(15, 3)