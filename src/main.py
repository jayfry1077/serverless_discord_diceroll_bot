import json
import logging
from utils import discord_funcs
from bot_funcs import bot

DISCORD_PING_PONG = {'statusCode': 200, 'body': json.dumps({"type": 1})}

commands = {'roll': bot.rollem}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main(event, context):

    if not discord_funcs.valid_signature(event):
        return discord_funcs.discord_body(200, 2, 'Error Validating Discord Signature')

    body = json.loads(event['body'])

    if body['type'] == 1:
        return DISCORD_PING_PONG

    command = body['data']['options'][0]['name']
    options = body['data']['options'][0]['options']

    try:
        message = commands[command](options)
        return discord_funcs.discord_body(200, 4, message)
    except Exception as e:
        logger.error(e)
        return discord_funcs(200, 2, 'Something went wrong')
