import collections


class SnakeGame:

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.dir = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.counter = 0
        self.snake_path = collections.deque([[0, 0]])

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        curr = self.snake_path[-1]
        x = curr[0] + self.dir[direction][0]
        y = curr[1] + self.dir[direction][1]
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            # hits a border the snakes dies
            return -1

        if [x, y] in self.snake_path and [x, y] != self.snake_path[0]:
            # snake bites its body
            return -1

        if self.food and x == self.food[0][0] and y == self.food[0][1]:
            self.food.popleft()
            self.counter += 1
        else:
            self.snake_path.popleft()

        self.snake_path.append([x, y])
        return self.counter


if __name__ == '__main__':
    # width = 3
    # height = 2
    # food = [[1, 2], [0, 1]]
    # obj = SnakeGame(width, height, food)
    # param_1 = obj.move("R")
    # print("param_1: {}".format(param_1))
    # param_2 = obj.move("D")
    # print("param_2: {}".format(param_2))
    # param_3 = obj.move("R")
    # print("param_3: {}".format(param_3))
    # param_4 = obj.move("U")
    # print("param_4: {}".format(param_4))
    # param_5 = obj.move("L")
    # print("param_5: {}".format(param_5))
    # param_6 = obj.move("U")
    # print("param_6: {}".format(param_6))

    # ["SnakeGame", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move", "move",
    #  "move", "move", "move"]

    direc = [["D"], ["D"], ["R"], ["U"], ["U"], ["L"], ["D"], ["R"],
             ["R"], ["U"], ["L"], ["L"], ["D"], ["R"], ["U"]]
    width = 3
    height = 3
    food = [[2, 0], [0, 0], [0, 2], [0, 1], [2, 2], [0, 1]]
    obj = SnakeGame(width, height, food)
    for dir in direc:
        print(obj.move(dir[0]))
