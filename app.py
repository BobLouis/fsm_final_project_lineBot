import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


from fsm import TocMachine
from utils import send_text_message

# for getenv
load_dotenv()

# record user state
user_state = {}
#

machine = TocMachine(
    states=["user", "dine_input_time",
            "dine_breakfast", "dine_lunch", "dine_dinner",
            "BMI_input_height", "BMI_input_weight", "BMI_final",
            "sport_input_type", "sport_input_time", "sport_final",
            "water_input_weight", "water_input_bottle_storage", "water_final",
            "news", "news_social", "news_health"
            ],
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

        # BMI
        {"trigger": "advance", "source": "user",
            "dest": "BMI_input_height", "conditions": "BMI"},
        {"trigger": "advance", "source": "BMI_input_height",
            "dest": "BMI_input_weight", "conditions": "BMI_input_height"},
        {"trigger": "advance", "source": "BMI_input_weight",
            "dest": "BMI_final", "conditions": "BMI_input_weight"},
        # water
        {"trigger": "advance", "source": "user",
            "dest": "water_input_weight", "conditions": "drink_water"},
        {"trigger": "advance", "source": "water_input_weight",
            "dest": "water_input_bottle_storage", "conditions": "water_input_weight"},
        {"trigger": "advance", "source": "water_input_bottle_storage",
            "dest": "water_final", "conditions": "water_input_bottle_storage"},

        # exercise
        {"trigger": "advance", "source": "user",
            "dest": "sport_input_type", "conditions": "exercise_in"},
        {"trigger": "advance", "source": "sport_input_type",
            "dest": "sport_input_time", "conditions": "input_exercise_type"},
        {"trigger": "advance", "source": "sport_input_time",
            "dest": "sport_final", "conditions": "input exercise time"},

        # news
        {
            "trigger": "advance", "source": "user",
            "dest": "news", "conditions": "select_news",
        },
        {
            "trigger": "advance", "source": "news",
            "dest": "news_social", "conditions": "select_social_news",
        },
        {
            "trigger": "advance", "source": "news",
            "dest": "news_health", "conditions": "select_health_news",
        },


        {"trigger": "go_back", "source": ["dine_breakfast", "dine_lunch",
                                          "dine_dinner", 'BMI_final', 'water_final', 'sport_final', "news_social", "news_health"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)


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


@app.route('/callback', methods=['POST'])
def webhook_handler():
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
        uid = event.source.user_id
        print("uid", uid)
        if uid in user_state:
            machine.state = user_state[uid]
        else:
            user_state[uid] = 'user'
        msg = event.message.text.lower()
        if machine.state == 'user' and event.message.text.lower() == 'dine':
            machine.state = 'dine_input_time'
            machine.is_going_to_dine(event)
            print(f'\nFSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and 'breakfast' in msg:
            machine.state = 'dine_breakfast'
            machine.input_breakfast(event)
            print(f'\nbreakfast FSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and 'lunch' in msg:
            machine.state = 'dine_lunch'
            machine.input_lunch(event)
            print(f'\nlunch FSM STATE: {machine.state}')
        elif machine.state == 'dine_input_time' and 'dinner' in msg:
            machine.state = 'dine_dinner'
            machine.input_dinner(event)
            print(f'\ndinner FSM STATE: {machine.state}')
        elif machine.state == 'user' and 'bmi' in msg:
            machine.state = 'BMI_input_height'
            machine.BMI(event)
            print(f'\nBMIFSM STATE: {machine.state}')
        elif machine.state == 'BMI_input_height':
            try:
                # Convert it into float
                val = float(msg)
                machine.state = 'BMI_input_weight'
                machine.BMI_input_height(event, val)
            except ValueError:
                send_text_message(event.reply_token,
                                  'please input your height in integer')
        elif machine.state == 'BMI_input_weight':
            try:
                # Convert it into float
                val = float(msg)
                machine.state = 'BMI_final'
                machine.BMI_input_weight(event, val)
            except ValueError:
                send_text_message(event.reply_token,
                                  'please input your weight in integer')
        elif machine.state == 'user' and 'water' in msg:
            machine.state = 'water_input_weight'
            machine.drink_water(event)
        elif machine.state == 'water_input_weight':
            try:
                # Convert it into int
                val = int(msg)
                machine.state = 'water_input_bottle_storage'
                machine.water_input_weight(event, val)
            except ValueError:
                send_text_message(event.reply_token,
                                  'please input your weight in integer')
        elif machine.state == 'water_input_bottle_storage':
            try:
                # Convert it into int
                val = int(msg)
                machine.state = 'water_final'
                machine.water_input_bottle_storage(event, val)
            except ValueError:
                send_text_message(event.reply_token,
                                  'please input your bottle storage in integer')

        elif machine.state == 'user' and 'sport' in msg:
            machine.state = 'sport_input_type'
            machine.exercise_in(event)
        elif machine.state == 'sport_input_type':
            machine.state = 'sport_input_time'
            machine.input_exercise_type(event, msg)
        elif machine.state == 'sport_input_time':
            machine.state = 'sport_final'
            machine.input_exercise_time(event)
        elif machine.state == 'user' and 'news' in msg:
            machine.state = 'news'
            machine.select_news(event)
            print(f'\nBMIFSM STATE: {machine.state}')
        elif machine.state == 'news':
            if(msg == 'health'):
                machine.state = 'news_health'
                machine.select_health_news(event)
            elif(msg == 'social'):
                machine.state = 'news_social'
                machine.select_social_news(event)

        else:
            machine.state = 'user'
            # send_text_message(event.reply_token, 'default')
            machine.default_msg(event)
            print(f'\nFSM STATE: {machine.state}')
        user_state[uid] = machine.state
    return 'OK'


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
