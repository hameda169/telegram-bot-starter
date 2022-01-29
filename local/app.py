from src.main import create_updater
from dotenv import load_dotenv
from os import environ
load_dotenv()


def main() -> None:
    proxy = environ.get("BOT_PROXY_URL")
    updater = create_updater(request_kwargs= None if proxy is None else {'proxy_url': proxy})
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
