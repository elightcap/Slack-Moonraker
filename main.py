import os
import re

from src.getprinter import get_printer
from src.setextemp import set_ex_temp
from src.setbedtemp import set_bed_temp
from src.preheat import set_preheat
from src.sethome import set_home
from src.getupload import get_upload
from src.setslice import set_slice
from slack_bolt import App
from dotenv import load_dotenv

load_dotenv()
SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
TOKEN = os.getenv('SLACK_BOT_TOKEN')
app = App(
    token = TOKEN,
    signing_secret = SIGNING_SECRET
)

@app.command("/getprinter")
def handle_printer(ack,body,say):
    """listener for get rpiner"""
    get_printer(ack,body,say)

@app.command("/setextemp")
def handle_set_ex_temp(ack,body,say):
    set_ex_temp(ack,body,say)

@app.command("/setbedtemp")
def handle_set_bed_temp(ack,body,say):
    set_bed_temp(ack,body,say)

@app.command("/preheat")
def handle_set_preheat(ack,body,say):
    set_preheat(ack,body,say)

@app.command("/sethome")
def handle_set_home(ack,body,say):
    set_home(ack,body,say)

@app.command("/test")
def handle_test(ack,body,say):
    get_test(ack,body,say)

@app.command("/slice")
def handle_slice(ack,body,say):
    set_slice(ack,body,say)

@app.shortcut("upload_files")
def handle_upload(ack,body,say):
    get_upload(ack,body,say)



if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3001)))
