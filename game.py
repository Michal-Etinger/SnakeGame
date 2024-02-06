from snake import Snake
from food import Food
from send_message import Message
import turtle

class Display:
    def __init__(self, setup, title, bgimage, tracer):
        self.screen = turtle.Screen()
        self.screen.setup(*setup)
        self.screen.title(title)
        self.screen.bgpic(bgimage)
        self.screen.tracer(tracer)

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 36, "normal"))

class Game(Display):
    def __init__(self, snake , food, display , scoreboard, delay):
        self.delay = delay
        self.snake = snake
        self.food = food
        self.display = display
        self.scoreboard = scoreboard

        self.message = "Message"
        self.number = "+972527256247"
        self.send_message = Message(self.message, self.number)

    
        
        
    def after_move_snake(self):
        self.snake.clearstamps()
        for segment in self.snake.current_location:
            self.snake.goto(segment[0], segment[1])
            self.snake.stamp()
        self.display.screen.update()
        turtle.ontimer(self.move_snake, self.delay)
        self.scoreboard.update_score()  # Update the score after each move

    def screen_listen(self):
        self.display.screen.listen()
        self.display.screen.onkey(self.snake.go_up, "Up")
        self.display.screen.onkey(self.snake.go_right, "Right")
        self.display.screen.onkey(self.snake.go_down, "Down")
        self.display.screen.onkey(self.snake.go_left, "Left")

    def reset(self):
        self.screen_listen()
        self.food.reset()
        self.move_snake()

    def move_snake(self):
        eat_itself = self.snake.move()  
        if eat_itself:
            self.snake.reset()
            self.send_message.edit_message(f"Congrats your score is {self.scoreboard.score}")
            self.send_message.send()
            self.scoreboard.score = 0
            self.after_move_snake()
        else:
            if not self.food_collision():
                self.snake.chop_tail()
            self.after_move_snake()

    def get_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance

    def food_collision(self):
        if self.get_distance(self.snake.current_location[-1], self.food.position) < 20:
            self.food.reset()
            self.scoreboard.increase_score()  # Increase score when snake eats food
            return True
        return False
