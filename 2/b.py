from __future__ import annotations


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, vector: Vector):
        print('__add__ function')
        if type(vector) != Vector:
            raise ValueError('Вектор можно складывать только с векторами!')
        
        self.x += vector.x
        self.y += vector.y
        return self

    def __sub__(self, vector: Vector): NotImplemented

    def __mul__(self, number: int): 
        print('__mul__ function')
        if type(number) != int:
            raise ValueError('Вектор можно умножать только с числами!')
        
        self.x *= number
        self.y *= number
        return self      
        
    def __truediv__(self, number: int): NotImplemented

    def __gt__(self, vector: Vector):
        print('__gt__ function')
        if type(vector) != Vector:
            raise ValueError('Вектор можно складывать только с векторами!')
        
        return self.mod() > vector.mod()

    def __lt__(self, vector: Vector): NotImplemented

    def __eq__(self, vector: Vector):
        return self.x == vector.x and self.y == vector.y

    def __str__(self) -> str:
        return f"Координата: ({self.x} | {self.y})"
    
    def mod(self) -> int:
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(1, 1)
v2 = Vector(1, 2)

# print(v1 + v2)
# print(v1 * 4)
# print(v1 > v2)
print(v1 == v2)