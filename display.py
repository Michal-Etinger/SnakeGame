import turtle          #יבוא סיפרייה חיצונית בשם טורטל


class Display:         #מחלקה בשם תצוגה - האחראית על המסך של המשחק
    def __init__(self, setup, title, bgimage, tracer):     #מתודת אתחול של המחלקה - מקבלת 4 משתנים
        self.screen = turtle.Screen()              #יוצר מסך עם משתנה בשם טרטל.סקרין
        self.screen.setup(*setup)                  #הגדרת גודל המסל עם משתנה בשם סטאפ
        self.screen.title(title)                   #הגדרת הכותרת של המסך עם משתנה בשם טייטל
        self.screen.bgpic(bgimage)                 #הגדרת תמונת הרקע של המסך עם משתנה בשם בגאימג
        self.screen.tracer(tracer)                 #הגדרת קצב הרענון של המסך עם משתנה בשם טרייסר