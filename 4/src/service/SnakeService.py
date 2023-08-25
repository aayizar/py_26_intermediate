from random import randint

from src.repository.MainRepository import MainRepository
from src.domain.Snake import Snake
from src.domain.Point import Point
from src.domain.Food import Food
from src.domain.Wall import Wall


class SnakeService:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        
        self.repository = MainRepository()
        self.snake = Snake()
        self.foods: list[Food] = [
            Food(*self.get_random_in_map()), 
            Food(*self.get_random_in_map())
        ]
        self.walls: list[Wall] = [
            Wall(*self.get_random_in_map()),
            Wall(*self.get_random_in_map())
        ]
        
        self.snake_append(*self.get_random_in_map())
        self.snake_append(-1, -1)
        self.snake_append(-1, -1)
    
    def snake_move(self):
        for ind in range(len(self.snake.body)-1, 0, -1):
            self.snake.body[ind].x = self.snake.body[ind - 1].x
            self.snake.body[ind].y = self.snake.body[ind - 1].y
        
        head = self.snake.body[0]
        head.x += self.snake.dx
        head.y += self.snake.dy
        
        if head.x == self.width:
            head.x = 0
        if head.x == -1:
            head.x = self.width - 1
        if head.y == self.height:
            head.y = 0
        if head.y == -1:
            head.y = self.height - 1
        
        # if snake:
        #     return True
        return False
    
    def snake_append(self, x, y):
        self.snake.body.append(Point(x, y))
    
    def check_snake_on_food(self):
        for food in self.foods:
            if food.is_equal(self.snake.body[0]):
                food.x = randint(0, self.width)
                food.y = randint(0, self.height)
                self.repository.increase_score(1)
                self.snake_append(-1, -1)
                
    def is_snake_on_wall(self):
        for wall in self.walls:
            return wall.is_equal(self.snake.body[0])
    
    def change_direction(self, dir):
        if dir == 'a':
            if self.snake.dx == 1:
                return
            self.snake.dx = -1
            self.snake.dy = 0
        if dir == 'd':
            if self.snake.dx == -1:
                return
            self.snake.dx = 1
            self.snake.dy = 0
        if dir == 'w':
            if self.snake.dy == 1:
                return
            self.snake.dx = 0
            self.snake.dy = -1
        if dir == 's':
            if self.snake.dx == -1:
                return
            self.snake.dx = 0
            self.snake.dy = 1
        
    def get_score(self):
        return self.repository.get_score()
    
    def get_random_in_map(self):
        return (randint(0, self.width-1), randint(0, self.height-1))
    
    def draw(self):
        field = ''
        
        for y in range(self.height):
            for x in range(self.width):
                el = '⬛'
                
                for point in self.snake.body:
                    if not point.is_equal(Point(x, y)):
                        continue
                    
                    if  point != self.snake.body[0]:
                        el = '🟧'
                    else:
                        el = '🟥'
                
                for food in self.foods:
                    if el == '⬛' and food.is_equal(Point(x, y)):
                        el = '🍏'
                
                
                for wall in self.walls:
                    if el == '⬛' and wall.is_equal(Point(x, y)):
                        el = '🟦'
                        
                
                field += el
            field += '\n'
            
        print('\n\n\n\n\n' + field)
                