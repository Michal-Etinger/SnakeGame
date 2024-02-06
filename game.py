import turtle    #יבוא של סיפרייה חיצונית טורטל


class Game():      #(הכלה) מחלקת המשחק עצמו המכילה את כל יתר המחלקות 
    def __init__(self, snake , food , scoreboard, delay, display, send_message):  #אתחול של המשחק
        self.display = display  
        self.delay = delay    
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.send_message = send_message
    

    def reset(self):      #אתחול המשחק
        self.screen_listen()    #אתחול והגדרת הקשבה למקשים
        self.food.reset()       #אתחול המיקום של האוכל
        self.move_snake()       #התזוזה של הנחש
        
    def screen_listen(self):    #אתחול והגדרה של הקשבה למקשים
        self.display.screen.listen()    #מעכשיו תקשיב למקשים
        self.display.screen.onkey(self.snake.go_up, "Up")    #בעת לחיצת על כפתור אפ הפעל את גואפ של האובייקט של הנחש
        self.display.screen.onkey(self.snake.go_right, "Right")
        self.display.screen.onkey(self.snake.go_down, "Down")
        self.display.screen.onkey(self.snake.go_left, "Left")

    def move_snake(self):       #תזוזת הנחש
        eat_itself = self.snake.move()     #בנה את הראש החדש
        if eat_itself:      #במידה ואכלנו את עצמו
            self.snake.reset()         #נאתחל את הנחש
            self.send_message.edit_message(f"Congrats your score is {self.scoreboard.score}")   #מעדכנים את ההודעה בווטצאפ
            self.send_message.send()     #שולחים את ההודעה
            self.scoreboard.score = 0    #מאפסים את ההניקוד
            self.after_move_snake()      # קוראים למתודה בהמשך להמשך הפעולות
        else:                    #במקרה והוא לא אכל את עצמו
            if not self.food_collision():   #האם הוא לא אכל אוכל
                self.snake.chop_tail()      #תמחק את הזנב
            self.after_move_snake()         #קוראים למתודה בהמשך להמשך הפעולות
            
    def after_move_snake(self):      #מתודת עדכון המסך לאחר תזוזת הנחש
        self.snake.clearstamps()        #מתודה שירשנו מטורטל שאחראית למחיקת שארית הנחש מהמסך אחרי שהוא זז
        for segment in self.snake.current_location:   #עבור כל גוף של הנחש תצייר על המסך במיקום איקס וואי
            self.snake.goto(segment[0], segment[1])   #הקורדינטות של כל סגמנט
            self.snake.stamp()      #תקבע את מה שציירנו לאחר תזוזת הנחש
        self.display.screen.update()          #ביצענו שינויים, תעדכן את השינויים על גבי המסך
        turtle.ontimer(self.move_snake, self.delay)    #לקרוא למתודה בעוד זמן מסויים
        self.scoreboard.update_score()      #לבצע עדכון ללוח התוצאות

    def get_distance(self, pos1, pos2):     #מתודה כללית לצורך אומדן מרחק
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5   #פיתגורס
        return distance

    def food_collision(self):        #בדיקת המרחק בין הראש לאוכל - האם הראש נכנס קרוב לאוכל
        if self.get_distance(self.snake.current_location[-1], self.food.position) < 20:     #אם המרחק בין הראש לאוכל קטן מ-20
            self.food.reset()        #אתחול מיקום האוכל
            self.scoreboard.increase_score()      #הגדלת לוח התוצאות עקב אכילת האוכל
            return True
        return False


