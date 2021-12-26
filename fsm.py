from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_dine(self, event):
        text = event.message.text
        print("which meal you want to choose")
        send_text_message(event.reply_token,
                          'which meal you want to eat')
        return text.lower() == "go to dine_input_time"

    def input_breakfast(self, event):
        text = event.message.text
        print("breakfast")
        send_text_message(event.reply_token,
                          'breakfast')
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
