from flask import Flask
from flask import request
import requests

keys = [
    {
        "user_key": "random key",
        "discord_id": "idk",
        "hwid": "",
        "note": "",
        "uid": ""
    },
    {
        "user_key": "random key",
        "discord_id": "idk",
        "hwid": "",
        "note": "",
        "uid": ""
    }
]

app = Flask(__name__)

@app.route('/')
def main():

    key = request.args.get("key")
    hwid = request.args.get("hwid")

    toreturn = "0"

    if len(hwid) > 2:
        for data in keys:
            if data["user_key"] == str(key):
                if data["identifier"] == "":
                    data["identifier"] = hwid

                if data["identifier"] == str(hwid):
                    toreturn = "1"

    return toreturn
