# Setup

## Setting up Ollama
To run this bot you need to get setup Ollama seperately, please find
the tutorial at [Ollama's github repository](https://github.com/ollama/ollama).

## Getting a Telegram bot token
To obtain a Telegram bot token, you can request it from BotFather, the
official bot management bot.

## Setup the bot.

1. Make sure your python is up-to date
2. Install pipx
	- For Debian and it's derivatives
    ```
    apt install pipx
    ```
	- For ArchLinux and it's derivatives
    ```
    pacman -S python-pipx
    ```
	- For Gentoo
    ```
    sudo emerge --sync
    sudo emerge --ask --update --deep --newuse @world
    sudo emerge --ask dev-python/pip
    sudo pip install pipx
    ```
	And finally, do to make sure its packages are on the path run,
	```
	pipx ensurepath
	```
3. Open your terminal, and install aitelegrambot by running
   ```bash
   pipx install aitelegrambot
   ```
4. make a `.env` file With the following contents:

```env
TELEGRAM_BOT_TOKEN=tokenhere
DEFAULT_MODEL=defaultmodelhere
OLLAMA_HOST=ollamahosthere
ADMIN_ID=adminuserid
MESSAGE_CHUNK_SIZE=5
```

You may omit `DEFAULT_MODEL` and `OLLAMA_HOST`, if you are going to
use the default settings (`OLLAMA_HOST` being `localhost:11434` and
`DEFAULT_MODEL` being `tusharhero/rationalai`).

5. Run the bot.

```bash
aitelegrambot
```
