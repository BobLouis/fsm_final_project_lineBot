import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_carousel_message(reply_token, col):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=ImageCarouselTemplate(columns=col)
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template=ButtonsTemplate(
            title=title,
            text=text,
            thumbnail_image_url=url,
            actions=btn
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_breakfast(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='https://www.youtube.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='連結2',
                            uri='https://www.youtube.com/'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def send_lunch(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='https://www.youtube.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='連結2',
                            uri='https://www.youtube.com/'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def send_dinner(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageTemplateAction(
                            label='message1',
                            text='message text1'
                        ),
                        URITemplateAction(
                            label='uri1',
                            uri='https://www.youtube.com/'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageTemplateAction(
                            label='message2',
                            text='message text2'
                        ),
                        URITemplateAction(
                            label='連結2',
                            uri='https://www.youtube.com/'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def aerobic10(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='10分钟超燃脂HIIT有氧运动',
                    text='不伤膝盖）比跑步郑多燕更有效减肥瘦身还有线条【周六野Zoey】',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=xuVrLqLyXHE&ab_channel=%E5%91%A8%E5%85%AD%E9%87%8EZoey'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='有氧運動 無跳躍不傷膝蓋10分鐘有氧運動',
                    text='在家跟著節奏爆汗吧！',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=UsvsX_Y5Qdc&t=19s&ab_channel=%E4%BA%9E%E9%87%8C%E6%B2%99Alisa'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def aerobic20(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='20分鐘低難度有氧運動',
                    text='腰腿| 燃脂| 無工具高體脂大基數入門適合【周六野Zoey】',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=LZAQQOH5n8g&t=490s&ab_channel=%E5%91%A8%E5%85%AD%E9%87%8EZoey'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='20分钟暴汗燃脂有氧运动',
                    text='全程站立无跳跃｜膝盖友好｜大基数友好【周六野Zoey】',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=sf4V6lrRs4I&ab_channel=%E5%91%A8%E5%85%AD%E9%87%8EZoey'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def retrain10(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='進階居家撕裂者腹肌10分鐘運動',
                    text='每天跟May做一輪，腹肌現形🔥At-home 10min intense abs workout. Do this everyday!',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=4pOjPjN7AqI&ab_channel=MayFit'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='中階】居家健身',
                    text='10分鐘腹肌訓練 - 無器械 打造六塊肌/ 10 mins abs workout at home no equipment',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=TSN738gKhyA&ab_channel=%E6%B8%B8%E6%9B%B8%E5%BA%AD'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def retrain20(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='20分鐘居家高强度全身肌肉徒手訓練【高級版】',
                    text='無需器材也能在家做的運動｜有效針對全身肌肉的訓練｜男生和女生都適合的健身訓練【健身運動】',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=JOu1dGBalBs&ab_channel=Eugene%26Jayn'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='FF居家上工訓練菜單',
                    text='20分鐘高燃脂 HIIT 訓練(無跳躍)',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=v03azf3VJLw&ab_channel=%E5%81%A5%E8%BA%AB%E5%B7%A5%E5%BB%A0'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def hi_aerobic10(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='中階 10分鐘高強度居家運動',
                    text='燃燒脂肪 有氧+無氧/',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=7iC8LaBuU1E&ab_channel=%E6%B8%B8%E6%9B%B8%E5%BA%AD'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='10分钟全身超燃脂有氧运动',
                    text='突破平台期加速减脂HIIT，强度升级【周六野Zoey】',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=Lzk7n3PK3Lk&ab_channel=%E5%91%A8%E5%85%AD%E9%87%8EZoey'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'


def hi_aerobic20(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='20分钟在家高强度全身燃脂运动🔥',
                    text=' 全程站立&无器械 | 20 Min Standing HIIT for Fat Burn',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=eUJk21wb2Y8&ab_channel=EileenYu'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/8BlV8Kc.jpeg',
                    title='【中階】居家瘦身',
                    text=' 20分鐘有氧運動 - 燃燒脂肪 無器械(中等強度)',
                    actions=[
                        URITemplateAction(
                            label='youtube link',
                            uri='https://www.youtube.com/watch?v=MXsfeBqdbHM&ab_channel=%E6%B8%B8%E6%9B%B8%E5%BA%AD'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, Carousel_template)
    return 'ok'
