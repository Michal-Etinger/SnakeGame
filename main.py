import turtle
from game import Game
from game import Display
from game import Scoreboard
from snake import Snake
from food import Food
from send_message import ChatGPTBot

w = 800
h = 600
food_size = 20
dilay = 100

class Main:
    #thedesplay=desplay
    scoreboard = Scoreboard()
    snake = Snake(w, h, scoreboard)
    food = Food(food_size, w, h, scoreboard)
    display = Display((w, h), "Snake Game", "./png.bg.png", 0)
    game = Game(snake, food, display, scoreboard, dilay)
    game.reset()
    turtle.mainloop()
    
    
    
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenAI API key
    api_key = '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'

    chatgpt_bot = ChatGPTBot(api_key)

    # Your user messages
    user_messages = [
        "Tell me a joke.",
        "What's the weather like today?",
        "Who won the last World Series?",
    ]

    # Generate and print responses
    for user_message in user_messages:
        response = chatgpt_bot.generate_response(user_message)
        print(f"User: {user_message}")
        print(f"ChatGPT: {response}")
        print("-" * 30)