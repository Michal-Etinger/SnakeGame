import turtle #יבוא של סיפריה חיצונית טורטל


class Snake(turtle.Turtle):    #(הורשה ממחלקת טורטל) מחלקה בשם נחש - הגדרת הנחש שיופיע על גבי המסך 
    def __init__(self, w, h):     #מתודת אתחול של המחלקה
        super().__init__()      #"הוראה:"אב קדמון תבצע את האיתחול
        self.penup()     #(הורשה ממחלקת טורטך) מתודת הגדרת ציור על המסך 
        self.w = w       #הגדרת משתנה רוחב המסך
        self.h = h       #הגדרת משתנה גובה המסך
        self.shape("square")   #(הורשה ממחלקת טורטל) מתודת הגדרת הצורה של הנחש 
        self.snake_starting_position = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]] #(הראש,רגל ראשונה, רגל שנייה וכן הלאה) משתנה הגדרת הנחש עצמו 
        self.starting_snake_dir = "up"  # "הגדרת משתנה להתחלת התזוזה: "תתחיל לעלות למעלה
        self.current_location = self.snake_starting_position  #הגדרת משתנה המיקום לגוף הנחש
        self.snake_dir = self.starting_snake_dir    #הגדרת כיוון הנחש
        self.offsets = {      #הגדרת שינוי מיקום הנחש לפי הכיוונים
            "up": (0, 20),
            "down": (0, -20),
            "left": (-20, 0),
            "right": (20, 0)
        }

    def chop_tail(self):   #מחלקה למחיקת הזנב בזמן תזוזה רגילה
        self.current_location.pop(0)    #"פקודה: "תוציא את הזנב של הנחש שנמצא במיקום אפס

    def move(self):       #מתודת התזוזה של הנחש
        snake = self.current_location    #משתנה הכנסה לתוך הנחש את מיקומי הנחש בכל רגע
        new_head = snake[-1].copy()      #העתקה לתוך ראש הנחש החדש את מיקום ראש הנחש הישן
        new_head[0] = snake[-1][0] + self.offsets[self.snake_dir][0]   #הגדרת איקס חדש לחודש החדש
        new_head[1] = snake[-1][1] + self.offsets[self.snake_dir][1]   #הגדרת ואי חדש לראש החדש

        eat_itself = new_head in snake[:-1]    #בדיקת האם הראש החדש נמצא על המיקום של גוף הנחש

        if not eat_itself:           #אם לא אכל את עצמו
            snake.append(new_head)       

            if snake[-1][0] > self.w / 2:     #במקרה והראש החדש עבר את גבולות המסך
                snake[-1][0] -= self.w         
            elif snake[-1][0] < - self.w / 2:
                snake[-1][0] += self.w
            elif snake[-1][1] > self.h / 2:
                snake[-1][1] -= self.h
            elif snake[-1][1] < -self.h / 2:
                snake[-1][1] += self.h

        return eat_itself   #החזרה האם הוא אכל את עצמו או לא

    def go_up(self):     #לשנות את כיוון הנחש ללמעלה
        if self.snake_dir != "down":
            self.snake_dir = "up"

    def go_right(self):    #לשנות את כיוון הנחש לימין
        if self.snake_dir != "left":
            self.snake_dir = "right"

    def go_down(self):     #לשנות את כיוון הנחש ללמטה
        if self.snake_dir != "up":
            self.snake_dir = "down"

    def go_left(self):    #לשנות את כיוון הנחש שמאלה
        if self.snake_dir != "right":
            self.snake_dir = "left"

    def reset(self):      #אתחול הנחש לאחר פסילה במשחק
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
        