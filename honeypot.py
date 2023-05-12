from pyHoneygain import HoneyGain
from discord_webhook import DiscordWebhook
from datetime import date
import os

# Get email and pass from env var
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

CACHED_TOKEN_PATH = '/.jwt-token'

def login():
    if os.path.exists(CACHED_TOKEN_PATH):
        with open(CACHED_TOKEN_PATH, 'r+') as file:
            user.set_jwt_token(file.read())
    else:
        user.login(EMAIL, PASSWORD)

        with open(CACHED_TOKEN_PATH, 'w') as file:
            file.write(user.jwt)

user = HoneyGain()

login()

if(os.path.exists(CACHED_TOKEN_PATH) and not user.me()):
    os.remove(CACHED_TOKEN_PATH)
    login()

user_balance = "\nUser HG balance {}, JT balance {}".format(user.wallet_stats()["data"]["{}".format(
    date.today())]["hg_credits"], user.wallet_stats()["data"]["{}".format(date.today())]["jt_credits"])
honeypot_status = user.get_honeypot_status()
message = "error"
if str(honeypot_status["winning_credits"]) != "None":
    message = "{} already claimed the honeypot today.{}".format(
        user.me()['email'], user_balance)
else:
    if honeypot_status["progress_bytes"] == honeypot_status["max_bytes"]:
        result = user.open_honeypot()
        if result["success"]:
            message = "Opened honeypot for {}, resulting in {} credits.{}".format(
                user.me()['email'], result["credits"], user_balance)
        else:
            message = "Couldn\'t open honeypot for {}, unknown error.{}".format(
                user.me()['email'], user_balance)
    else:
        message = "Couldn\'t open honeypot for {}, did not gather 15MB.{}\nProgress in bytes: {}/15000000".format(
            user.me()['email'], user_balance, user.get_honeypot_status()["progress_bytes"])

print(message)
