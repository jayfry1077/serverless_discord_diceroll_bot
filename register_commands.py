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
    "name": "DND",
    "description": "Dungeons and Dragons!",
    "options": [
        {
            "name": "roll",
                    "description": "Create a group.",
                    "type": 1,
                    "options": [
                        {
                            "name": "quantity",
                            "description": "Number of dice.",
                            "type": 3,
                            "required": True
                        },
                        {
                            "name": "maximum",
                            "description": "Highest number on the die",
                            "type": 3,
                            "required": True
                        },
                        {
                            "name": "minimum",
                            "description": "Lowest number on the die.",
                            "type": 3,
                            "required": False
                        },
                        {
                            "name": "modifier",
                            "description": "Any amount to add to the roll.",
                            "type": 3,
                            "required": False
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


# update_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# get_commands(f"https://discord.com/api/v8/applications/{bot_id}/commands")
# delete_commands(
#     f"https://discord.com/api/v8/applications/{bot_id}/commands/795912485793431583")
