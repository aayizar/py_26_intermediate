class MyList:
    def __init__(self, arr) -> None:
        self.arr:list = arr
        
    def __add__(self, number):
        print('__add__ function')
        if type(number) != int:
            raise ValueError('Класс работает только с числами!')
        self.arr.append(number)
        return self
    
    def __mul__(self, number):
        print('__mul__ function')
        if type(number) != int:
            raise ValueError('Класс работает только с числами!')
        for i in range(len(self.arr)):
            self.arr[i] *= number
        return self
        
    def __str__(self) -> str:
        return str(self.arr)
    

l1 = MyList([2, 5, 6, 7])

print(l1 + 5)
print(l1 * 4)