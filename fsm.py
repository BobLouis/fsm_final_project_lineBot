from transitions.extensions import GraphMachine
from utils import *
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction


class TocMachine(GraphMachine):
    weight = 0.0
    height = 0.0
    bottle_storage = 0
    sport_type = ''
    sport_time = 0

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_dine(self, event):
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
        send_lunch(event.reply_token)
        self.go_back()

    def input_dinner(self, event):
        send_dinner(event.reply_token)
        self.go_back()

    def BMI(self, event):
        send_text_message(event.reply_token,
                          'please input your weight in kilogram')

    def BMI_input_height(self, event, val):
        self.weight = val
        send_text_message(event.reply_token, 'please input your height in cm')

    def BMI_input_weight(self, event, val):
        self.height = val
        title = '你的BMI 指數'
        text = 'BMI = ' + \
            str(round(self.weight / ((self.height/100) ** 2), 2))
        btn = [
            MessageTemplateAction(
                label='BMI',
                text='BMI'
            )
        ]
        url = 'https://i.imgur.com/GlJn5SY.jpeg'
        send_button_message(event.reply_token, title, text, btn, url)
        self.go_back()

    def drink_water(self, event):
        send_text_message(event.reply_token,
                          'please input your weight in kilogram')

    def water_input_weight(self, event, val):
        self.weight = val
        send_text_message(event.reply_token,
                          'please input your bottle storage in ml')

    def water_input_bottle_storage(self, event, val):
        self.bottle_storage = val
        title = '你一天該喝多少水'
        text = '該喝' + str(self.weight*30)+'cc 的水\n也就是' + \
            str(round(self.weight*30/self.bottle_storage, 1))+'瓶的水'
        btn = [
            MessageTemplateAction(
                label='BMI',
                text='BMI'
            )
        ]
        url = 'https://i.imgur.com/XXdtszA.gif'
        send_button_message(event.reply_token, title, text, btn, url)
        self.go_back()

    def exercise_in(self, event):
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

    def input_exercise_type(self, event):
        self.sport_type = event.message.text
        title = '選擇運動類時間'
        text = ''
        btn = [
            MessageTemplateAction(
                label='10',
                text='10'
            ),
            MessageTemplateAction(
                label='20',
                text='20'
            ),
            MessageTemplateAction(
                label='30',
                text='30'
            )
        ]
        url = 'https://i.imgur.com/0kUpCmW.jpeg'
        send_button_message(event.reply_token, title, text, btn, url)

    def input_exercise_time(self, event):
        self.sport_time = int(event.message.text)
        Aerobic＿10(event.reply_token)
        self.go_back()
