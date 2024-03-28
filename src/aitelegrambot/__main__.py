from aitelegrambot.bot import TelegramBot
from dotenv import load_dotenv
import logging
import os


def main():
    load_dotenv()

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

    # Check if the token has been given.
    required_values: list[str] = [
        "TELEGRAM_BOT_TOKEN",
    ]
    missing_values: list[str] = [
        value for value in required_values if os.environ.get(value) is None
    ]
    if len(missing_values) > 0:
        logging.error(
            f'The following environment values are missing in your .env: {", ".join(missing_values)}'
        )
        exit()

    # Run the bot.
    bot: TelegramBot = TelegramBot(
        ollama_host=os.environ.get("OLLAMA_HOST", "localhost:11434"),
        bot_token=os.environ["TELEGRAM_BOT_TOKEN"],
        default_model=os.environ.get("DEFAULT_MODEL", "tusharhero/rationalai"),
        administrator_user_id=int(os.environ.get("ADMIN_ID", 0)),
        enable_streaming_response=bool(
            os.environ.get("ENABLE_STREAMING_RESPONSE", "disable") == "enable"
        ),
        message_chunk_size=int(os.environ.get("MESSAGE_CHUNK_SIZE", 5)),
    )

    bot.run()


if __name__ == "__main__":
    main()
