import turtle      #יבוא של סיפריית חיצונית טורטל
import random      #יבוא של סיפרייה חיצונית רנדום


class Food(turtle.Turtle):     #(הורשה ממחלקת טורטל) מחלקה בשם אוכל - הגדרת האוכל שיופיע על גבי המסך 
    def __init__(self, size, w, h):      #מתודת אתחול של המחלקה
        super().__init__()            #(אב קדמון=טורטל) אתחול אב קדמון 
        self.w = w             #הגדרת משתנה רוחב המסך
        self.h = h             #הגדרת משתנה גובה המסך
        self.food_size = size  #הגדרת משתנה של גדול האוכל
        self.color("yellow")   #(ירושה ממחלקת טורטל) מתודת הגדרת צבע האוכל
        self.shape("circle")   #(ירושה ממחלקת טורטל) מתודת הגדרת צורת האוכל 
        self.shapesize(size / 20)    #(ירושה ממחלקת טורטל) מתודת הגדרת גודל האוכל 
        self.penup()           #(ירושה ממחלקת טורטל) מתודת הגדרת ציור על המסך 

    def reset(self):           #מתודה לעדכון מיקום האוכל על גבי המסך
        new_position = self.get_random_food_position()     #הגרלת מיקום חדש על ידי מתודת רנדום שהגדרנו בהמשך
        self.goto(new_position)             #הגדרת מתודת לשינוי המיקום החדש של האוכל על גבי המסך
        self.position = new_position        #הגדרת משתנה של המיקום בתוך הזיכרון

    def get_random_food_position(self):     #מתודת שמגרילה מיקום חדש בכל פעם על המסך
        x = random.randint(int(- self.w / 2 + self.food_size), int(self.w / 2 - self.food_size))   #(מיקום אופקי) הגרלת איקס רנדומלי על המסך
        y = random.randint(int(- self.h / 2 + self.food_size), int(self.h / 2 - self.food_size))   #(מיקום אנכי) הגרלת ואי רנדומלי על המסך 
        return (x, y)         #החזרת האיקס והוואי שהגרלנו
