from flask import Flask, request
from telegram import Update
from src.main import create_updater
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

updater = create_updater()
updater.custom_start_webhook()


@app.route(f'/{environ.get("BOT_ID")}', methods=['POST'])
def route():
    try:
        data = request.json
        update = Update.de_json(data, updater.bot)
        updater.handle_update(update)
    finally:
        return '', 200
