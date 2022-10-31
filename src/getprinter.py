import os
import requests

import moonrakerpy as moonpy

from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App

dotenvPath = Path('/home/pi/bots/3dprintbot/.env')
load_dotenv(dotenv_path=dotenvPath)
SERVER = os.getenv('SERVER')
SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
TOKEN = os.getenv('SLACK_BOT_TOKEN')
FILE_PATH = os.getenv('FILE_PATH')
IMAGE_URL = "{}/webcam/?action=snapshot.jpg".format(SERVER)
PRINT_CHANNEL = os.getenv('PRINT_CHANNEL')

printer = moonpy.MoonrakerPrinter(SERVER)

app = App(
    token = TOKEN,
    signing_secret = SIGNING_SECRET
)

def get_printer(ack, body, say):
    ack()
    image = requests.get(IMAGE_URL)
    open("image.jpg", "wb").write(image.content)
    location = printer.query_status(object='toolhead')
    ex = printer.query_status(object='extruder')
    bed = printer.query_status(object='heater_bed')
    toolLocation = location['position']
    positionX = str(toolLocation[0])
    positionY = str(toolLocation[1])
    positionZ = str(toolLocation[2])
    exTemp = str(ex['temperature'])
    exTarget = str(ex['target'])
    bedTemp = str(bed['temperature'])
    bedTarget = str(bed['target'])
    posStr = "x={}, y={}, z={}".format(positionX,positionY,positionZ)

    result = app.client.files_upload_v2(
        channel=PRINT_CHANNEL,
        file="image.jpg"
    )
    slackImageUrl = result['files'][0]['url_private']
    print(slackImageUrl)

    mBlocks = [
        {
           "text":
                {
                    "text": "Printer Status",
                    "type": "plain_text"
                },
            "type": "header"
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "fields":
            [
                {
                    "text": "*Extruder Temperature:*",
                    "type": "mrkdwn"
                },
                {
                    "text": exTemp,
                    "type": "plain_text"
                },
                {
                    "text": "*Extruder Target:*",
                    "type": "mrkdwn"
                },
                {
                    "text": exTarget,
                    "type": "plain_text"
                },
                {
                    "text": "*Bed Temperature:*",
                    "type": "mrkdwn"
                },
                {
                    "text": bedTemp,
                    "type": "plain_text"
                },
                {
                    "text": "*Bed Target:*",
                    "type": "mrkdwn"
                },
                {
                    "text": bedTarget,
                    "type": "plain_text"
                },
                {
                    "text": "*Toolhead Position:*",
                    "type": "mrkdwn"
                },
                {
                    "text": posStr,
                    "type": "plain_text"
                }
            ],
        "accessory": 
            {
                "type": "image",
                "image_url": slackImageUrl,
                "alt_text": "screenshot"
            }
        }
    ]
    app.client.chat_postMessage(
        channel='C01FPR1HND9',
        blocks=mBlocks,
        text="Printer Status"
    )