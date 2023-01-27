import requests
token = '5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0'
me = '5787643045'


# url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={me}&text={out_message}'


def send_message(msg, sender_id):
    token = '5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={sender_id}&text={msg}'
    requests.get(url)

# send_message('안녕', '5787643045')











# update_url = f'https://api.telegram.org/bot{token}/getUpdates'
# response = requests.get(update_url).json()
# input_message = response['result'][-1]['message']['text']
# chat_id = response['result'][-1]['message']['from']['id']
# if input_message == '집 보내주세요':
#     output_message = '안돼. 돌아가 안 바꿔줘 '
# elif input_message == '제발요':
#     output_message = '집으로 돌아가!'
# else:
#     output_message = '뭐라는거야~'
# send_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={output_message}'
# requests.get(send_url)

# server_url = 'https://ab60-211-33-180-73.jp.ngrok.io'
# print(
#     f'https://api.telegram.org/bot{token}/setWebhook?url={server_url}'
















'''
for i in update_url:
    if 'hi' in i:
        print('hello')
    else:
        for i in update_url:
            if '안녕' in i:
                print('안녕하세요')

 requests.get(url)

'''


'''
https://api.telegram.org/bot5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0/sendMessage?chat_id=5787643045&text=hi
- 메시지 보내기


https://api.telegram.org/bot5482300788:AAFwcsZ9CYcSo4_oajIXJFJrjLuIGCAc0H0/getUpdates
- 수신함 확인


chat_id=5787643045


chat_id=__doc__
&
text=____ 
'''