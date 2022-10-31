import os
import requests

import moonrakerpy as moonpy

from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from src.getprinter import get_printer

dotenvPath = Path('/home/pi/bots/3dprintbot/.env')
load_dotenv(dotenv_path=dotenvPath)

TOKEN = os.getenv('SLACK_BOT_TOKEN')
SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
CANCEL_URL = "http://6.6.6.118/printer/print/cancel"
app = App(
    token = TOKEN,
    signing_secret = SIGNING_SECRET
)

def get_test(ack,body,say):
    ack()
    file = body['message']['files'][0]['url_private']
    name = body['message']['files'][0]['name']
    dl = requests.get(file, headers={'Authorization': 'Bearer {}'.format(TOKEN)})
    open("/home/pi/gcode_files/{}".format(name),"wb").write(dl.content)