import os

import moonrakerpy as moonpy

from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from src.getprinter import get_printer

dotenvPath = Path('/home/pi/bots/3dprintbot/.env')
load_dotenv(dotenv_path=dotenvPath)

SERVER = os.getenv('SERVER')
SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
TOKEN = os.getenv('SLACK_BOT_TOKEN')
FILE_PATH = os.getenv('FILE_PATH')
PRINT_CHANNEL = os.getenv('PRINT_CHANNEL')

printer = moonpy.MoonrakerPrinter(SERVER)

app = App(
    token = TOKEN,
    signing_secret = SIGNING_SECRET
)

def set_home(ack, body, say):
    ack()
    app.client.chat_postMessage(
        channel=PRINT_CHANNEL,
        text="Going Home!"
        )
    printer.send_gcode("g28")
    get_printer(ack,body,say)