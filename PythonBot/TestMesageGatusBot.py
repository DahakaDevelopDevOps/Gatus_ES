import requests

TOKEN = '7345309315:AAHUO-ORb0Uv7DFI2pZGRRPYfV5npNZBqss'
CHAT_ID = '-1002237411116'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response

response = send_message(CHAT_ID, 'Test message from Gatus bot')
print(response.json())

def check_bot_permissions():
    url = f'https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={CHAT_ID}&user_id={TOKEN}'
    response = requests.get(url)
    permissions = response.json()['result']['can_send_messages']
    return permissions

permissions = check_bot_permissions()
print(permissions)