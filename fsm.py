from transitions.extensions import GraphMachine
from utils import *
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_dine(self, event):
        # text = event.message.text
        # print("which meal you want to choose")
        # send_text_message(event.reply_token,
        #                   'which meal you want to eat')
        # return text.lower() == "go to dine_input_time"
        title = '請問想要吃早餐 午餐 還是晚餐'
        text = '讓healthy bear來幫你選擇最適合你的食物'
        btn = [
            MessageTemplateAction(
                label='早餐',
                text='breakfast'
            ),
            MessageTemplateAction(
                label='午餐',
                text='lunch'
            ),
            MessageTemplateAction(
                label='晚餐',
                text='dinner'
            ),
        ]
        url = 'https://i.imgur.com/NT0a6ID.png'
        send_button_message(event.reply_token, title, text, btn, url)

    def input_breakfast(self, event):
        send_breakfast(event.reply_token)
        self.go_back()

    def input_lunch(self, event):
        print("lunch")
        send_text_message(event.reply_token,
                          'lunch')
        self.go_back()

    def input_dinner(self, event):
        print("dinner")
        send_text_message(event.reply_token,
                          'dinner')
        self.go_back()
