##############################################
# Run this script locally to add bot commands
##############################################
import requests
import os
from dotenv import load_dotenv

load_dotenv()

bot_id = os.getenv('bot_id')
bot_key = os.getenv('bot_key')


json = {
    "name": "botbury",
    "description": "A Helpful Bot!",
    "options": [
        {
            "name": "signup",
                    "description": "Sign-up a user for discord and guilded alerts.",
                    "type": 1,
                    "options": [
                        {
                            "name": "username",
                            "description": "twitch user name found at the end of their url",
                            "type": 3,
                            "required": True
                        }
                    ]
        }
    ]
}


headers = {
    "Authorization": f"Bot {bot_key}"
}


def update_commands(url):
    r = requests.post(url, headers=headers, json=json)

    print(r.content)


def get_commands(url):
    r = requests.get(url, headers=headers)

    print(r.content)


def delete_commands(url):
    r = requests.delete(url, headers=headers)

    print(r.content)


update_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# get_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# delete_commands(
#     f"https://discord.com/api/v8/applications/{bot_id}/commands/795912485793431583")
