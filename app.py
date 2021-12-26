import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from message import *
from image import *
from Function import *

from fsm import TocMachine
from utils import send_text_message

# for getenv
load_dotenv()


machine = TocMachine(
    states=["user", "dine_input_time",
            "dine_breakfast", "dine_lunch", "dine_dinner"],
    transitions=[
        # dine
        {"trigger": "advance", "source": "user",
            "dest": "dine_input_time", "conditions": "is_going_to_dine"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_breakfast", "conditions": "input_breakfast"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_lunch", "conditions": "input_lunch"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_dinner", "conditions": "input_dinner"},
        # go back
        {"trigger": "go_back", "source": ["dine_breakfast", "dine_lunch",
                                          "dine_dinner"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)


# machine = TocMachine(
#     states=["user", "dine_input_time", "dine_breakfast", "dine_lunch", "dine_dinner",
#             "BMI_input_height", "BMI_input_weight", "BMI_input_gender", "BMI_final",
#             "water_input", "water_input_weight", "water_input_bottle_storage", "water_final",
#             "sport_input_type", "sport_input_time", "sport_final"],
#     transitions=[
#         # dine
#         {"trigger": "advance", "source": "user",
#             "dest": "dine_input_time", "conditions": "is_going_to_dine"},
#         {"trigger": "advance", "source": "dine_input_time",
#             "dest": "dine_breakfast", "conditions": "input breakfast"},
#         {"trigger": "advance", "source": "dine_input_time",
#             "dest": "dine_lunch", "conditions": "input_lunch"},
#         {"trigger": "advance", "source": "dine_input_time",
#             "dest": "dine_dinner", "conditions": "input_dinner"},
#         # BMI
#         {"trigger": "advance", "source": "user",
#             "dest": "BMI_input_height", "conditions": "BMI"},
#         {"trigger": "advance", "source": "BMI_input_height",
#             "dest": "BMI_input_weight", "conditions": "BMI_input_height"},
#         {"trigger": "advance", "source": "BMI_input_weight",
#             "dest": "BMI_input_gender", "conditions": "BMI_input_weight"},
#         {"trigger": "advance", "source": "BMI_input_gender",
#             "dest": "BMI_final", "conditions": "BMI_input_gender"},
#         # water
#         {"trigger": "advance", "source": "user",
#             "dest": "water_input_weight", "conditions": "drink water"},
#         {"trigger": "advance", "source": "water_input_weight",
#             "dest": "water_input_bottle_storage", "conditions": "drink water_input weight"},
#         {"trigger": "advance", "source": "water_input_bottle_storage",
#             "dest": "water_final", "conditions": "drink water_input bottlr storage"},
#         # exercise
#         {"trigger": "advance", "source": "user",
#             "dest": "sport_input_type", "conditions": "exercise"},
#         {"trigger": "advance", "source": "sport_input_type",
#             "dest": "sport_input_time", "conditions": "input exercise type"},
#         {"trigger": "advance", "source": "sport_input_time",
#             "dest": "sport_final", "conditions": "input exercise time"},
#         # go back
#         {"trigger": "go_back", "source": ["dine_breakfast", "dine_lunch",
#                                           "dine_dinner", "BMI_final", "water_final", "sport_final"], "dest": "user"},
#     ],
#     initial="user",
#     auto_transitions=False,
#     show_conditions=True,
# )


# machine = TocMachine(
#     states=["user", "state1", "state2"],
#     transitions=[
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state1",
#             "conditions": "is_going_to_state1",
#         },
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state2",
#             "conditions": "is_going_to_state2",
#         },
#         {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
#     ],
#     initial="user",
#     auto_transitions=False,
#     show_conditions=True,
# )
app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)
parser = WebhookParser(channel_secret)

mode = 0


@app.route('/callback', methods=['POST'])
def webhook_handler():
    global mode
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f'Request body: {body}')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f'\nFSM STATE: {machine.state}')
        print(f'REQUEST BODY: \n{body}')

        # response = machine.advance(event)

        # if response == False:
        if machine.state == 'user' and event.message.text.lower() == 'dine':
            machine.state = 'dine_input_time'
            # send_text_message(event.reply_token,
            #                   'dine%s' % {machine.state})
            # machine.is_going_to_dine(event)
            # print(event)
            machine.is_going_to_dine(event)
            print(f'\nFSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and event.message.text.lower() == 'breakfast':
            machine.state = 'dine_breakfast'
            machine.input_breakfast(event)
            print(f'\nbreakfast FSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and event.message.text.lower() == 'lunch':
            machine.state = 'dine_lunch'
            machine.input_lunch(event)
            print(f'\nlunch FSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and event.message.text.lower() == 'dinner':
            machine.state = 'dine_dinner'
            machine.input_dinner(event)
            print(f'\ndinner FSM STATE: {machine.state}')
        else:
            machine.state = 'user'
            send_text_message(event.reply_token, 'default')
            print(f'\nFSM STATE: {machine.state}')

    return 'OK'


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
