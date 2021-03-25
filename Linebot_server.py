# -*- coding: utf-8 -*-

from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from apscheduler.schedulers.background import BackgroundScheduler

import configparser

import Homework as HW
import json
import os

app = Flask(__name__)  # 建立 Flask 物件

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel-access-token'))
handler = WebhookHandler(config.get('line-bot', 'channel-secret'))

maskdata = list()


@app.route("/callback", methods=['POST'])  # 路由
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    if text.find('查詢姓名:') == 0 and text.find('查詢姓名:') < text.find('/學號:'):
        result = HW.HW2(event.message.text, event.source.user_id)  # 直接給字串
        response = result[0]
        print(result[1])
    elif text.find('姓名:') == 0 and text.find('姓名:') < text.find('/學號:'):
        response = HW.HW3_1(event.message.text, event.source.user_id)
    elif text[0:3] == '機構:' and text[-8:-4] == '剩下多少' and text[-2:] == '口罩':
        response = HW.HW3_3(event.message.text, maskdata[:])
    elif text[0:3] == '地區:' and text[-8:-4] == '剩下多少' and text[-2:] == '口罩':
        response = HW.HW3_4(event.message.text, maskdata[:])
    elif text[0:4] == '請在每週' and text[5] == '的' and text[8:] == '時提醒我作業進度':
        response = HW.HW4_1(event.message.text, event.source.user_id)
    elif text == '查詢我的作業繳交情況':
        response = HW.HW4_2(event.source.user_id)
    elif text[0:11] == '請問全班有幾位同學拿到' and text[-3:] == '的成績':
        response = HW.HW4_3(event.message.text, event.source.user_id)

    else:
        response = '格式錯誤！'

    # 回覆文字訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response))


if __name__ == "__main__":
    if not os.path.isfile('./registered_data.json'):
        with open('registered_data.json', 'w', encoding='utf-8') as file:
            json.dump({}, file, ensure_ascii=False, indent=4)

    maskdata_temp = list(HW.HW3_2())

    for item in maskdata_temp:
        data = dict()
        for key, value in item.items():
            data[key] = value
        maskdata.append(data)

    app.run(debug=True)
