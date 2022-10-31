import os
import requests

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
IMAGE_URL = "{}}/webcam/?action=snapshot.jpg".format(SERVER)
PRINT_CHANNEL = os.getenv('PRINT_CHANNEL')

printer = moonpy.MoonrakerPrinter(SERVER)
CANCEL_URL = "{}/printer/print/cancel".format(SERVER)
app = App(
    token = TOKEN,
    signing_secret = SIGNING_SECRET
)

def set_cancel(ack, body, say):
    ack()
    requests.post(CANCEL_URL)
