import requests
TOKEN = '7345309315:AAHUO-ORb0Uv7DFI2pZGRRPYfV5npNZBqss'
CHAT_ID = '-1002237411116'
def get_chat_id():
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    res = requests.get(url)
    data = res.json()['result'][0]['message']['chat']['id']
    return data
chat_id = get_chat_id()
print(chat_id)

def get_bot_permissions():
    url = f'https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={CHAT_ID}&user_id={TOKEN}'
    response = requests.get(url)
    return response.json()

permissions = get_bot_permissions()
print(permissions)