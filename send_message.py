import pywhatkit as kit       #יבוא סיפרייה חיצונית בשם פייואטקיט


class Message:        #מחלקה בשם הודעה
    def __init__(self, message, number): #מק מתודת אתחול של המחלקה 
        self.message = message           #יצירת משתנה בשם "ההודעה" של המחלקה (יצירת המצב)
        self.number = number             #יצירת משתנה בשם "מספר הטלפון" של המחלקה (יצירת המצב)

    def edit_message(self, message):  #מתודה של שינוי ההודעה שתשלח בהתאם לניקוד המשתנה
        self.message = message        #שינוי תוכן ההודעה - עדכון המשתנה שיצרנו
        
    def send(self):        #מתודה של שליחת ההודעה דרך הסיפרייה שייבאנו
        kit.sendwhatmsg_instantly(self.number, self.message, wait_time=10)  #הפעולה עצמה של שליחת ההודעה
        

