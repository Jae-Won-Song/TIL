from flask import Flask, request
import random
from utils import send_message
import requests

app = Flask('hi')

@app.route('/', methods=['POST'])
def home():
    # 서버로서 우리가 받은 요청을 의미 => request
    data = request.json
    input_message = data['message']['text']
    sender_id = data['message']['from']['id']

    if input_message == '안녕':
        send_message('안녕하세요', sender_id)
    elif input_message == '로또번호추첨':
        lotto = random.sample(range(1, 46), 6)
        send_message(lotto, sender_id)
    else:
        send_message('안녕 로또 번호중 하나만 말해주세오', sender_id)
    # 우리가 보내는 요청 => Client => requests
    return 'Hello Server!'

# def send_message(msg, sender_id):
    # token = '5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0'
    # url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={sender_id}&text={msg}'


app.run(port = 80, debug=True)


https://api.telegram.org/bot5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0/setWebhook?url=jwsong.pythonanywhere.com

