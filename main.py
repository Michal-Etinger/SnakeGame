import turtle                       #סיפרייה חיצונית 
from game import Game               #סיפרייה פנימית
from scoreboard import Scoreboard   #פנימי
from food import Food               #פנימי
from snake import Snake             #פנימי
from display import Display         #פנימי
from send_message import Message    #פנימי


w = 800           #משתנה רוחב
h = 600           #משתנה גובה
food_size = 20    #משתנה גודל האוכל
delay = 100       #(miliseconds) משתנה קצב הרענון 


class Main:       #מחלקת מניין
    scoreboard = Scoreboard()              #בניית אובייקט לוח תוצאות
    display = Display((w, h), "Snake Game", "./png.bg.png", 0)    #בניית אובייקט תצוגה
    send_message = Message("Message",  "+972527256247")         #בניית אובייקט הודעת ווטצאפ
    snake = Snake(w, h)                    #בניית אובייקט הנחש
    food = Food(food_size, w, h)           #בניית אובייקט האוכל
    game = Game(snake, food,  scoreboard, delay, display, send_message)     #בניית אובייקט המשחק עצמו
    game.reset()                           #אתחול המשחק
    turtle.mainloop()                      #מריץ את המשחק


    