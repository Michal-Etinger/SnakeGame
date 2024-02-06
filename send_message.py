import pywhatkit as kit
from datetime import datetime
import openai

class Message:
    def __init__(self, message, number):
        self.message = message
        self.number = number

    def edit_message(self, message):
        self.message = message
        
    def send(self):
        kit.sendwhatmsg_instantly(self.number, self.message, wait_time=10)
        
        
class ChatGPTBot:
    def __init__(self, api_key, engine="text-davinci-003"):
        openai.api_key = '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'
        self.engine = engine

    def generate_response(self, user_message, max_tokens=150):
        response = openai.Completion.create(
            engine=self.engine,
            prompt=user_message,
            max_tokens=max_tokens,
        )
        return response.choices[0].text.strip()
    

