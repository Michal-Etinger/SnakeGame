import turtle

class Snake(turtle.Turtle):
    def __init__(self, w, h, scoreboard):
        super().__init__(shape="square")
        self.penup()
        self.w = w
        self.h = h
        self.scoreboard = scoreboard
        self.snake_starting_position = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        self.starting_snake_dir = "up"
        self.current_location = self.snake_starting_position
        self.snake_dir = self.starting_snake_dir
        self.offsets = {
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }

    def chop_tail(self):
        self.current_location.pop(0)

    def move(self):  # Accept the food instance as an argument
        snake = self.current_location
        new_head = snake[-1].copy()
        new_head[0] = snake[-1][0] + self.offsets[self.snake_dir][0]
        new_head[1] = snake[-1][1] + self.offsets[self.snake_dir][1]

        eat_itself = new_head in snake[:-1]

        if not eat_itself:
            snake.append(new_head)

            if snake[-1][0] > self.w / 2:
                snake[-1][0] -= self.w
            elif snake[-1][0] < - self.w / 2:
                snake[-1][0] += self.w
            elif snake[-1][1] > self.h / 2:
                snake[-1][1] -= self.h
            elif snake[-1][1] < -self.h / 2:
                snake[-1][1] += self.h

        return eat_itself

    def get_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance

    def go_up(self):
        if self.snake_dir != "down":
            self.snake_dir = "up"

    def go_right(self):
        if self.snake_dir != "left":
            self.snake_dir = "right"

    def go_down(self):
        if self.snake_dir != "up":
            self.snake_dir = "down"

    def go_left(self):
        if self.snake_dir != "right":
            self.snake_dir = "left"

    def reset(self):
        self.snake_starting_position = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        self.starting_snake_dir = "up"
        self.current_location = self.snake_starting_position
        self.snake_dir = self.starting_snake_dir
        self.offsets = {
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }
