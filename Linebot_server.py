from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser
import Homework as HW
import json

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel-access-token'))
handler = WebhookHandler(config.get('line-bot', 'channel-secret'))


@app.route("/callback", methods=['POST'])
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
        result = HW.HW2(event.message.text, event.source.user_id)
        response = result[0]
        print(result[1])
    else:
        response = '格式錯誤！'

    # 回覆文字訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response))


if __name__ == "__main__":
    app.run(debug=True)