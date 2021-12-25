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
    states=["user", "dine_input_time", "dine_breakfast", "dine_lunch", "dine_dinner",
            "BMI_input_height", "BMI_input_weight", "BMI_input_gender", "BMI_final",
            "water_input", "water_input_weight", "water_input_bottle_storage", "water_final",
            "sport_input_type", "sport_input_time", "sport_final"],
    transitions=[
        # dine
        {"trigger": "advance", "source": "user",
            "dest": "dine_input_time", "conditions": "is_going_to_dine"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_breakfast", "conditions": "input breakfast"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_lunch", "conditions": "input_lunch"},
        {"trigger": "advance", "source": "dine_input_time",
            "dest": "dine_dinner", "conditions": "input_dinner"},
        # BMI
        {"trigger": "advance", "source": "user",
            "dest": "BMI_input_height", "conditions": "measure BMI"},
        {"trigger": "advance", "source": "BMI_input_height",
            "dest": "BMI_input_weight", "conditions": "measure BMI_input_height"},
        {"trigger": "advance", "source": "BMI_input_weight",
            "dest": "BMI_input_gender", "conditions": "measure BMI_input_weight"},
        {"trigger": "advance", "source": "BMI_input_gender",
            "dest": "BMI_final", "conditions": "measure BMI_input_gender"},
        # water
        {"trigger": "advance", "source": "user",
            "dest": "water_input_weight", "conditions": "drink water"},
        {"trigger": "advance", "source": "water_input_weight",
            "dest": "water_input_bottle_storage", "conditions": "drink water_input weight"},
        {"trigger": "advance", "source": "water_input_bottle_storage",
            "dest": "water_final", "conditions": "drink water_input bottlr storage"},
        # exercise
        {"trigger": "advance", "source": "user",
            "dest": "sport_input_type", "conditions": "exercise"},
        {"trigger": "advance", "source": "sport_input_type",
            "dest": "sport_input_time", "conditions": "input exercise type"},
        {"trigger": "advance", "source": "sport_input_time",
            "dest": "sport_final", "conditions": "input exercise time"},
        # go back
        {"trigger": "go_back", "source": ["dine_breakfast", "dine_lunch",
                                          "dine_dinner", "BMI_final", "water_final", "sport_final"], "dest": "user"},
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

        response = machine.advance(event)

        if response == False:
            if event.message.text.lower() == 'fsm':
                machine.state = 'state10'
                send_text_message(event.reply_token,
                                  'fsm123%s' % {machine.state})
                print(event)

                print(f'\nFSM STATE: {machine.state}')
            elif machine.state != 'user' and event.message.text.lower() == 'restart':
                send_text_message(
                    event.reply_token, '輸入『fitness』即可開始使用健身小幫手。\n隨時輸入『chat』可以跟機器人聊天。\n隨時輸入『restart』可以從頭開始。\n隨時輸入『fsm』可以得到當下的狀態圖。' + mode)
                machine.go_back()
            elif machine.state == 'user':
                send_text_message(
                    event.reply_token, '輸入『fitness』即可開始使用健身小幫手。\n隨時輸入『chat』可以跟機器人聊天。\n隨時輸入『restart』可以從頭開始。\n隨時輸入『fsm』可以得到當下的狀態圖。%d' % mode)
            elif machine.state == 'input_age' or machine.state == 'input_height' or machine.state == 'input_weight':
                send_text_message(event.reply_token, '請輸入一個整數')
            elif machine.state == 'input_gender':
                send_text_message(event.reply_token, '請輸入『男生』或『女生』')
            elif machine.state == 'input_days':
                send_text_message(event.reply_token, '請輸入一個『0~7的整數』')
            elif machine.state == 'choose':
                send_text_message(event.reply_token, '請輸入『增肌』或『減脂』')
            elif machine.state == 'muscle':
                send_text_message(
                    event.reply_token, '輸入『熱量』可以查看您一天所需的熱量。\n輸入『影片』可以觀看健身影片。\n輸入『back』可重新選擇目標。')
            elif machine.state == 'thin':
                send_text_message(
                    event.reply_token, '輸入『低醣飲食』可以查看何謂低醣飲食。\n輸入『生酮飲食』可以查看何謂生酮飲食。\n輸入『back』可重新選擇目標。')
            elif machine.state == 'show_cal':
                if event.message.text.lower() == 'bmr':
                    text = '即基礎代謝率，全名為 Basal Metabolic Rate。基礎代謝意思是身體為了要維持運作，在休息時消耗掉的熱量。基礎代謝率佔了總熱量消耗的一大部分。會影響到基礎代謝率高低的有很多，像是總體重、肌肉量、賀爾蒙、年齡等。'
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() == 'tdee':
                    text = '即每日總消耗熱量，全名為 Total Daily Energy Expenditure。指的是人體在一天內消耗的熱量，除了基礎代謝率所需的能量以外，還包括運動和其他活動消耗的熱量，像是走路、上下樓梯、活動肌肉等等。通常運動量愈大，TDEE也會愈高。'
                    send_text_message(event.reply_token, text)
                elif event.message.text.lower() != 'back':
                    send_text_message(
                        event.reply_token, '輸入『食物』可以查看一天的熱量應如何攝取。\n輸入『BMR』或『TDEE』會有文字說明。\n輸入『back』返回選單。')
            elif machine.state == 'show_video' and event.message.text.lower() != 'back':
                send_text_message(
                    event.reply_token, '輸入『胸』，『背』，『腿』，『肩』，『二頭』，『三頭』可搜尋相關影片。\n輸入『back』返回選單。')
            elif (machine.state == 'show_img' or machine.state == 'get_video') and (event.message.text.lower() != 'back'):
                send_text_message(event.reply_token, '輸入『back』返回選單。')
            elif machine.state == 'show_food' and event.message.text.lower() != 'back':
                send_text_message(
                    event.reply_token, '輸入『圖片』可查看熱量圖。\n輸入『查詢』可查詢食物的營養素。\n輸入『back』返回選單。')
            elif (machine.state == 'thin_type1' or machine.state == 'thin_type2') and (event.message.text.lower() != 'back'):
                send_text_message(event.reply_token,
                                  '輸入『熱量』可以查看您一天所需的熱量。\n輸入『back』返回選單。')

    return 'OK'


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
