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
ENABLE_STREAMING_RESPONSE=disable
MESSAGE_CHUNK_SIZE=5
```

Here is a table detailing each option.

| Option                      | Description                                                                                                | Examples                                         | Required                               | Runtime modifiable |
|-----------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------|--------------------|
| `TELEGRAM_BOT_TOKEN`        | Telegram bot token issued by Telegram's botfather                                                          | `9999999999:XXXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXX` | Yes                                    | No                 |
| `DEFAULT_MODEL`             | The default model to be used by the Telegram Bot (It can be changed during runtime by the admin)           | `tusharhero/rationalai`                          | No                                     | Yes                |
| `OLLAMA_HOST`               | Host address of the `ollama` service.                                                                      | `localhost:11434`                                | No                                     | No                 |
| `ADMIN_ID`                  | Telegram user id of the administrator, this userid will be able to change multiple options during runtime. | `9999999999`                                     | No (Admin commands won't be available) | No                 |
| `ENABLE_STREAMING_RESPONSE` | Select whether, the bot will stream responses or not.                                                      | `enable` or `disable`                            | No (disabled by default)               | No                 |
| `MESSAGE_CHUNK_SIZE`        | The number of words to be send at a time, when streaming responses.                                        | `5`, `6`, any integer.                           | No (`5` by default)                    | No                 |


5. Run the bot.

```bash
aitelegrambot
```
