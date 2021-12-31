import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction
from bs4 import BeautifulSoup
import requests
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
                # 1 無名早點
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/d6RvEjD.jpeg',
                    title='無名早點',
                    text='活力早點  成大學生喜愛の早餐店之ㄧ',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/55a5994cc03a10241de673d6-%E7%84%A1%E5%90%8D%E6%97%A9%E9%BB%9E#reviews'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E6%B4%BB%E5%8A%9B%E6%97%A9%E9%BB%9E/@22.9929214,120.2214666,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMrYe7zv_UMDKL8HmP_VZJFMvjCVYNseUmUTQFW!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMrYe7zv_UMDKL8HmP_VZJFMvjCVYNseUmUTQFW%3Dw224-h298-k-no!7i3024!8i4032!4m11!1m2!2m1!1z54Sh5ZCN5pep6bueIOiHuuWNl-W4guadseWNgOmVt-amrui3r-S4ieautTPomZ8!3m7!1s0x346e7693e507c52b:0x408648216bef785a!8m2!3d22.9929214!4d120.2214666!14m1!1BCgIYIQ!15sCi_nhKHlkI3ml6npu54g6Ie65Y2X5biC5p2x5Y2A6ZW35qau6Lev5LiJ5q61M-iZn1o6IjjnhKHlkI0g5pep6bueIOiHuuWNlyDluIIg5p2x5Y2AIOmVt-amriDot68g5LiJIOautSAzIOiZn5IBFGJyZWFrZmFzdF9yZXN0YXVyYW50'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 2 阿公阿婆蛋餅
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/0yiztd7.jpeg',
                    title='阿公阿婆蛋餅',
                    text='超大份量粉漿蛋餅銅板價～台南傳統古早味',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5598e75540b5e30f5545f2a4-%E9%98%BF%E5%85%AC%E9%98%BF%E5%A9%86%E8%9B%8B%E9%A4%85'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/An+Gong+Avocado/@22.9994044,120.2276641,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipM5Y1EN6Ls0jsFgCBYqrdDwe1eZIENuQf4iMklS!2e10!3e12!6s%2F%2Flh4.googleusercontent.com%2F-I2V1TH5j6qI%2FX6nz96P11pI%2FAAAAAAAAp2g%2FHV6S66q3zgMX3GfjLt-8LzCsfZsY0jkpACJUFGAYYCw%2Fw224-h298-k-no%2F!7i3024!8i4032!4m7!3m6!1s0x346e76ea7b464111:0x87d8e73fe4e8f48a!8m2!3d22.9994044!4d120.2276641!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 3 春牛豆漿大王
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/vidzhE9.jpeg',
                    title='春牛豆漿大王',
                    text='台南美食北區。鴨母寮市場旁邊，來自台東知名的早餐店，',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/594570f92756dd524dd08e66-%E6%98%A5%E7%89%9B%E8%B1%86%E6%BC%BF%E5%A4%A7%E7%8E%8B'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E6%98%A5%E7%89%9B%E8%B1%86%E6%BC%BF%E5%A4%A7%E7%8E%8Bl%E5%8F%B0%E5%8D%97%E8%B1%86%E6%BC%BFl%E4%B8%AD%E5%BC%8F%E6%97%A9%E9%A4%90%E6%8E%A8%E8%96%A6l%E7%87%92%E9%A4%85%E6%B2%B9%E6%A2%9Dl%E9%AE%AA%E9%AD%9A%E8%9B%8B%E9%A4%85l%E9%B9%B9%E8%B1%86%E6%BC%BFl%E9%8D%8B%E8%B2%BCl%E8%98%BF%E8%94%94%E7%B3%95/@22.9988974,120.2041014,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMPzxKSivCcPQo0vhF3NT8vyfwowD5SN1g_9YM!2e10!3e12!6s%2F%2Flh4.googleusercontent.com%2F-TTVAfSyamjg%2FX410C2haLzI%2FAAAAAAAAP1A%2FCyzU4Eqhx8kg0QHmGrp4_V9vAQEHsX6QACJUFGAYYCw%2Fw397-h298-k-no%2F!7i2048!8i1536!4m7!3m6!1s0x346e766033f2b8a1:0x5f458ecdc3b39b4a!8m2!3d22.9988974!4d120.2041014!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 4 益緣早餐
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/cwmgljt.jpeg',
                    title='益緣早餐',
                    text='台南 成大周邊 - 益緣早餐 [早餐店',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5c2cc92e2756dd161d02ee85-%E7%9B%8A%E7%B7%A3%E6%97%A9%E9%A4%90'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E7%9B%8A%E7%B7%A3%E6%97%A9%E9%A4%90/@23.007312,120.2203476,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOUZ66EN2n4nTuO7lJTVMStk8ip2wEgK4xBEUOD!2e10!3e12!6s%2F%2Flh3.googleusercontent.com%2F-sKiA__YAXjk%2FXl8Evuj6c7I%2FAAAAAAAA1i0%2FphG-66LpXVc-L6xj4JFXeXMtLeL--VJ8wCLIBGAYYCw%2Fw397-h298-k-no%2F!7i4032!8i3024!4m7!3m6!1s0x346e76ef6d369aa5:0xbfd5f6dc1f30f79b!8m2!3d23.007312!4d120.2203476!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 5 祝君早安
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/QH21mCa.jpeg',
                    title='祝君早安',
                    text='好吃的古早味粉漿蛋餅，加起司更美味～',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5d76f2bc8c906d23a231f754-%E7%A5%9D%E5%90%9B%E6%97%A9%E5%AE%89'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E7%A5%9D%E5%90%9B%E6%97%A9%E5%AE%89/@22.9956804,120.2148626,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPsy1o8PKN5WLy-ztkWOdD9uhcPu2fABJMHg-UE!2e10!3e12!6s%2F%2Flh5.googleusercontent.com%2F-QI2qeCdjw8E%2FYBidivtngOI%2FAAAAAAAASf4%2FHWnUst0zvgAgSSTM-GvkeZFLIr1PTf-aQCJUFGAYYCw%2Fw224-h298-k-no%2F!7i3024!8i4032!4m7!3m6!1s0x346e77406e0b155b:0xe4667ef041a9244a!8m2!3d22.9956804!4d120.2148626!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
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
                # 1 開元路無名虱目魚
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/pRInZRQ.jpeg',
                    title='開元路無名虱目魚',
                    text='沒有招牌無名小吃 台南人早午餐就吃肉臊飯-開元路無名虱目魚 ‧ 肉燥飯 ',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/560440352756dd161730bcd9-%E9%96%8B%E5%85%83%E8%B7%AF%E7%84%A1%E5%90%8D%E8%99%B1%E7%9B%AE%E9%AD%9A%E3%80%81%E8%82%89%E7%87%A5%E9%A3%AF'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E9%96%8B%E5%85%83%E8%B7%AF%E7%84%A1%E5%90%8D%E8%99%B1%E7%9B%AE%E9%AD%9A+%E2%80%A7+%E8%82%89%E7%87%A5%E9%A3%AF/@23.0082034,120.2215916,3a,75y,90t/data=!3m8!1e2!3m6!1s-ndDjK8YIyTU%2FYGiejG5h4rI%2FAAAAAAAAC7g%2FvOkCDebh16g-ZElQAjU1e3OqBuTPWX_pACJUFGAYYCw!2e4!3e12!6s%2F%2Flh4.googleusercontent.com%2F-ndDjK8YIyTU%2FYGiejG5h4rI%2FAAAAAAAAC7g%2FvOkCDebh16g-ZElQAjU1e3OqBuTPWX_pACJUFGAYYCw%2Fw397-h298-k-no%2F!7i4032!8i3024!4m7!3m6!1s0x346e76e61255bcbd:0xbbd2a730898c3fd!8m2!3d23.0082034!4d120.2215916!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 2 貴一郎 S.R.T 燒肉
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/cclzmBS.jpeg',
                    title='貴一郎 S.R.T 燒肉',
                    text='台南最厲害的現烤和牛便當 |台南美食| |燒肉推薦| |燒肉便當|',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5659ed1b2756dd1225aa7c0b-%E8%B2%B4%E4%B8%80%E9%83%8E-S.R.T-%E7%87%92%E8%82%89'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E5%81%A5%E5%BA%B7%E7%87%92%E8%82%89%E5%B1%8B+%E8%B2%B4%E4%B8%80%E9%83%8E/@23.0034726,120.2194086,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOrW9Ziy4XBIxVjJL2RLw3HoUdNdjAMqI0A2ouA!2e10!3e12!6s%2F%2Flh6.googleusercontent.com%2F-bfGi-exUau0%2FYYeZWcsWxlI%2FAAAAAAAAS3A%2FEp8TpgV7CZEiZ5OoYg3fTuG-cOFry6heQCJUFGAYYCw%2Fw224-h398-k-no%2F!7i2268!8i4032!4m7!3m6!1s0x346e775e2a7eed2f:0xea17394d4767efc1!8m2!3d23.0034726!4d120.2194086!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 3 蚵男燒烤海物
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/zrrQfKm.jpeg',
                    title='蚵男燒烤海物',
                    text='蚵男生蠔海物燒烤 台南北區 — 幸福平價海味大爆炸的好滋味',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5598ebbc40b5e30f5545f4f5-%E8%9A%B5%E7%94%B7%E7%87%92%E7%83%A4%E6%B5%B7%E7%89%A9'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E8%9A%B5%E7%94%B7+%E7%94%9F%E8%A0%94+%E6%B5%B7%E7%89%A9+%E7%87%92%E7%83%A4/@23.0190273,120.2001606,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOr0BWHfVCIpdTiLt0Z6uR-HSmY5srpo6kmR6z8!2e10!3e12!6s%2F%2Flh3.googleusercontent.com%2F-9-xc-d6vQhg%2FX1uLa3vAbLI%2FAAAAAAAAonc%2FLyjEBoPuQZEAD-MDMXDv4L5DQF8FzGObgCJUFGAYYCw%2Fw397-h298-k-no%2F!7i4000!8i3000!4m7!3m6!1s0x346e77eb9f248db9:0x97514aae3e50c6ae!8m2!3d23.0190273!4d120.2001606!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 4 當月麵店
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/1j2KBnW.jpeg',
                    title='當月麵店',
                    text='成大周邊日式老宅文青麵店 當月麵店 台南麵店 台南美',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5fe35d5a8c906d27a93b7338-%E7%95%B6%E6%9C%88%E9%BA%B5%E5%BA%97'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E7%95%B6%E6%9C%88%E9%BA%B5%E5%BA%97/@22.9937812,120.2225701,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipM9IERP66TahCalaucjH2KfCCMC3ofUKx6998C_!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipM9IERP66TahCalaucjH2KfCCMC3ofUKx6998C_%3Dw421-h298-k-no!7i2437!8i1721!4m7!3m6!1s0x346e777ae04cd6df:0xdad17901daba3ae0!8m2!3d22.9937812!4d120.2225701!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 5 富盛號碗粿
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/L4aQ8ju.jpeg',
                    title='富盛號碗粿',
                    text='國華街美食 | 台南 富盛號碗粿 民國36年開始飄香的好味道',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5598391c40b5e30894d725bb-%E5%AF%8C%E7%9B%9B%E8%99%9F%E7%A2%97%E7%B2%BF'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E5%AF%8C%E7%9B%9B%E8%99%9F%E7%A2%97%E7%B2%BF/@22.9976082,120.1992113,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOPW-mg9_MpMnFpmtqUomVsiXgYp2s51coBrga_!2e10!3e12!6s%2F%2Flh6.googleusercontent.com%2F-PU6usPfk5wM%2FX-DBhxQH7JI%2FAAAAAAAARoU%2Fzd3BDqhBO-cghOY5pnsdVia55Q0abi0tACJUFGAYYCw%2Fw397-h298-k-no%2F!7i4032!8i3024!4m7!3m6!1s0x346e77ca0bb0307b:0x94c9fffaa462db0d!8m2!3d22.9976082!4d120.1992113!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),

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
                # 1 寬窄巷子四川麻辣鍋
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/w75MocW.jpeg',
                    title='寬窄巷子四川麻辣鍋',
                    text='純正濃郁麻香四川麻辣鍋！吃了走路都有風！人氣火鍋輕鬆在家嚐~',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/58f8f84f2756dd27438b4f7f-%E5%AF%AC%E7%AA%84%E5%B7%B7%E5%AD%90%E5%9B%9B%E5%B7%9D%E9%BA%BB%E8%BE%A3%E9%8D%8B'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E5%AF%AC%E7%AA%84%E5%B7%B7%E5%AD%90%E5%9B%9B%E5%B7%9D%E9%BA%BB%E8%BE%A3%E9%8D%8B-%E4%B8%AD%E8%A5%BF%E5%A4%96%E5%B8%B6%E9%BA%BB%E8%BE%A3%E6%B9%AF%E5%BA%95%7C%E9%8D%8B%E5%BA%95%E5%AE%85%E9%85%8D%7C%E7%89%B9%E8%89%B2%E9%8D%8B%E7%89%A9%7C%E8%81%9A%E9%A4%90%E6%8E%A8%E8%96%A6%7C%E5%BF%85%E5%90%83%E7%81%AB%E9%8D%8B%7C%E4%BA%BA%E6%B0%A3%E9%BA%BB%E8%BE%A3%E9%8D%8B%7C%E5%A4%96%E5%B8%B6%E5%B0%8F%E7%81%AB%E9%8D%8B/@22.9925148,120.2057693,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOUAGLuhzUCFXKaeF4nZOGh3lE3jLeXNiiAQKc0!2e10!3e12!6s%2F%2Flh6.googleusercontent.com%2F-coed0HS45Ws%2FYQL3OgxpikI%2FAAAAAAAE5V4%2FI_vWJ_t2jrsIlH5-s5azYJTpvIFGpi-rwCJUFGAYYCw%2Fw224-h334-k-no%2F!7i2360!8i3524!4m7!3m6!1s0x346e76882e4310cd:0xaadb8ab1e60e37d6!8m2!3d22.9925148!4d120.2057693!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 2 劉家莊牛肉爐
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/2Zj21jm.jpeg',
                    title='劉家莊牛肉爐',
                    text='台南永康美食 溫體牛涮涮鍋、牛肉火鍋 用餐空間舒適、有免費大型停車場',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5a57a8662756dd2c5cec90da-%E5%8A%89%E5%AE%B6%E8%8E%8A%E7%89%9B%E8%82%89%E7%88%90'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/Liujiazhuang+beef+furnace/@23.0316015,120.2528093,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPDMIY86dIl-A2t3_EH27-gapNZ-XKvcWG_FyBf!2e10!3e12!6s%2F%2Flh3.googleusercontent.com%2F-ZpX86xOyWHU%2FX2lyG5J03QI%2FAAAAAAAAnFw%2FiwVKCmxUf04HTch6tt5SQRGfgPDRIyOVQCJUFGAYYCw%2Fw224-h298-k-no%2F!7i3024!8i4032!4m7!3m6!1s0x346e70cb4e9e5845:0x66fbc9f2a31e7d3b!8m2!3d23.0316015!4d120.2528093!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 3 輝哥本土牛肉爐
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/xm2SIsh.jpeg',
                    title='輝哥本土牛肉爐 ',
                    text='台南牛肉爐-輝哥本土牛肉爐 肉燥飯吃到飽 溫體牛肉湯超暖',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/56817a9d2756dd3feba20308-%E8%BC%9D%E5%93%A5%E6%9C%AC%E5%9C%9F%E7%89%9B%E8%82%89%E7%88%90'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E8%BC%9D%E5%93%A5%E6%9C%AC%E7%94%A2%E7%89%9B%E8%82%89%E7%88%90/@22.9700547,120.2667777,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipPrFlcVJYyDGWF7DomG1vt2tMVVCMGC70N0K-7K!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPrFlcVJYyDGWF7DomG1vt2tMVVCMGC70N0K-7K%3Dw397-h298-k-no!7i4032!8i3024!4m7!3m6!1s0x346e715918044c43:0x802d6313e7a3ba32!8m2!3d22.9700547!4d120.2667777!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 4 尖叫 SCREAM 精緻炭火燒肉
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/4ThK70M.jpeg',
                    title='尖叫 SCREAM 精緻炭火燒肉',
                    text='高檔吃到飽燒肉 Scream 尖叫精緻炭火燒肉 蝦蟹海鮮吃到爽!!',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/5d32dc818c906d2116c38194-%E5%B0%96%E5%8F%AB-SCREAM-%E7%B2%BE%E7%B7%BB%E7%82%AD%E7%81%AB%E7%87%92%E8%82%89-%E5%8F%B0%E5%8D%97%E6%97%97'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/search/%E5%B0%96%E5%8F%AB%20SCREAM%20%E7%B2%BE%E7%B7%BB%E7%82%AD%E7%81%AB%E7%87%92%E8%82%89%20%E5%8F%B0%E5%8D%97%E6%97%97%E8%89%A6%E5%BA%97%20%E8%87%BA%E5%8D%97%E5%B8%82%E6%9D%B1%E5%8D%80%E4%B8%AD%E8%8F%AF%E6%9D%B1%E8%B7%AF%E4%B8%80%E6%AE%B5209%E8%99%9F'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),
                # 5 初幸居食屋
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/kFUGYHP.jpeg',
                    title='初幸居食屋',
                    text='日料火鍋「初幸 居食屋」超道地關西壽喜燒！北海道A5和牛、日本廣島牡蠣！',
                    actions=[
                        URITemplateAction(
                            label='更多圖片與評論',
                            uri='https://ifoodie.tw/restaurant/6073e9fe781cc07663c1dffc-%E5%88%9D%E5%B9%B8%E5%B1%85%E9%A3%9F%E5%B1%8B-%E5%BF%A0%E7%BE%A9%E5%BA%97'
                        ),
                        URITemplateAction(
                            label='看菜單 地圖',
                            uri='https://www.google.com.tw/maps/place/%E5%88%9D%E5%B9%B8%E5%B1%85%E9%A3%9F%E5%B1%8B%EF%BC%88%E5%BF%A0%E7%BE%A9%E5%BA%97%EF%BC%89/@22.9969385,120.2041785,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipOkMERJDh3lYS-6iXvXsG1GgrGfCjk4UhKIDvs!2e10!3e12!6s%2F%2Flh5.googleusercontent.com%2F-tp7gyOVXJJE%2FYV0olBLS0jI%2FAAAAAAAA8Wo%2FZqCQTH1A4gY1_Uqrn1dxnj9OQ7cHPNVUACJUFGAYYCw%2Fw397-h298-k-no%2F!7i4032!8i3024!4m7!3m6!1s0x346e779ea5d311ed:0xfe3bec7c9d01cb49!8m2!3d22.9969385!4d120.2041785!14m1!1BCgIYIQ'
                        ),
                        MessageTemplateAction(
                            label='再吃一次',
                            text='dine'
                        )
                    ]
                ),

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
                    thumbnail_image_url='https://i.imgur.com/YaoDBO3.png',
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
                    thumbnail_image_url='https://i.imgur.com/EKUq1Cq.png',
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
                    thumbnail_image_url='https://i.imgur.com/Y6XH7C9.png',
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
                    thumbnail_image_url='https://i.imgur.com/qcFcReE.png',
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
                    thumbnail_image_url='https://i.imgur.com/YAbDeGn.png',
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
                    thumbnail_image_url='https://i.imgur.com/dJjCQhm.png',
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
                    thumbnail_image_url='https://i.imgur.com/QN4VVVg.png',
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
                    thumbnail_image_url='https://i.imgur.com/mvRrRES.png',
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
                    thumbnail_image_url='https://i.imgur.com/eC3g1pb.png',
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
                    thumbnail_image_url='https://i.imgur.com/G69BivM.png',
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
                    thumbnail_image_url='https://i.imgur.com/OIR5FjW.png',
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
                    thumbnail_image_url='https://i.imgur.com/AGLH9KC.png',
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


def scrapenews_social():
    response = requests.get(
        "https://www.ettoday.net/news/focus/%E9%A6%96%E9%A0%81/%E9%A0%AD%E6%A2%9D/")
    soup = BeautifulSoup(response.content, "html.parser")
    sel = soup.select("div.part_list_3 a")
    content = ""
    for i in range(3):
        content += "第{}則:".format(i+1)+sel[i]["title"]+"\n"+"詳細內容請洽:" + \
            "https://www.ettoday.net/"+sel[i]["href"]+"\n\n\n"
    return content


def scrapenews_health():
    response = requests.get(
        "https://health.ettoday.net/")
    soup = BeautifulSoup(response.content, "html.parser")
    sel = soup.select("div.box_2 a")
    # print(sel)
    # print()
    # print(sel[0]['title'])
    content = ""
    for i in range(3):
        content += "第{}則:".format(i+1)+sel[i]["title"]+"\n"+"詳細內容請洽:" + \
            ""+sel[i]["href"]+"\n\n\n"
    return content


# def scrapenews():
#     response = requests.get(
#         "https://health.ettoday.net/")
#     soup = BeautifulSoup(response.content, "html.parser")
#     sel = soup.select("div.box_2 a")
#     print(sel)
#     print()
#     print(sel[0]['title'])
#     content = ""
#     for i in range(3):
#         content += "第{}則:".format(i+1)+sel[i]["title"]+"\n"+"詳細內容請洽:" + \
#             ""+sel[i]["href"]+"\n\n\n"
#     return content
