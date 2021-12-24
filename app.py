import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
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
    states=["init", "dine_input_time", "dine_breakfast", "dine_lunch", "dine_dinner",
            "BMI_input_height", "BMI_input_weight", "BMI_input_gender", "BMI_final",
            "water_input", "water_input_weight", "water_input_bottle_storage", "water_final",
            "sport_input_type", "sport_input_time", "sport_final"],
    transitions=[
        # dine
        {"trigger": "advance", "source": "init",
            "dest": "dine_input_time", "conditions": "is_going_to_dine"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_breakfast", "conditions": "input breakfast"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_lunch", "conditions": "input_lunch"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_dinner", "conditions": "input_dinner"},
        # BMI
        {"trigger": "advance", "source": "init",
            "dest": "BMI_input_height", "conditions": "measure BMI"},
        {"trigger": "advance", "source": "BMI_input_height",
            "dest": "BMI_input_weight", "conditions": "measure BMI_input_height"},
        {"trigger": "advance", "source": "BMI_input_weight",
            "dest": "BMI_input_gender", "conditions": "measure BMI_input_weight"},
        {"trigger": "advance", "source": "BMI_input_gender",
            "dest": "BMI_final", "conditions": "measure BMI_input_gender"},
        # water
        {"trigger": "advance", "source": "init",
            "dest": "water_input_weight", "conditions": "drink water"},
        {"trigger": "advance", "source": "water_input_weight",
            "dest": "water_input_bottle_storage", "conditions": "drink water_input weight"},
        {"trigger": "advance", "source": "water_input_bottle_storage",
            "dest": "water_final", "conditions": "drink water_input bottlr storage"},
        # exercise
        {"trigger": "advance", "source": "init",
            "dest": "sport_input_type", "conditions": "exercise"},
        {"trigger": "advance", "source": "sport_input_type",
            "dest": "sport_input_time", "conditions": "input exercise type"},
        {"trigger": "advance", "source": "sport_input_time",
            "dest": "sport_final", "conditions": "input exercise time"},
        # go back
        {"trigger": "go_back", "source": ["dine_breakfast", "dine_lunch",
                                          "dine_dinner", "BMI_final", "water_final", "sport_final"], "dest": "init"},
    ],
    initial="init",
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


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '吃什麼' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '健康' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '抽' in msg:
        message = random_image()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif msg.lower() == 'mocha':
        message = TextSendMessage(text='milk')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
