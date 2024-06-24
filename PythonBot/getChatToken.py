import requests
import json

def get_chat_ids(bot_token):
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")
    updates = response.json()

    chat_ids = []
    for update in updates["result"]:
        if 'message' in update and 'chat' in update['message']:
            chat_id = update["message"]["chat"]["id"]
            chat_ids.append(chat_id)

    return chat_ids

bot_token = "7345309315:AAHUO-ORb0Uv7DFI2pZGRRPYfV5npNZBqss"
chat_ids = get_chat_ids(bot_token)
print(chat_ids)
