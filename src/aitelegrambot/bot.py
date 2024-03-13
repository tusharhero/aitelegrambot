# The GPLv3 License (GPLv3)

# Copyright © 2024 aitelegrambot authors.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This module defines the TelegramBot class.
"""

from telegram.ext import ApplicationBuilder, CommandHandler
from ollama import Client
from aitelegrambot.commandhandlers import CommandHandlers


class TelegramBot:
    """
    A class that implements a Telegram bot using the Ollama framework.
    """

    def __init__(self, ollama_host: str, bot_token: str, default_model: str):
        """
        Initializes an instance of TelegramBot.

        Arguments:
        ==========
        ollama_host: Host address of the `ollama` service.
        bot_token: Bot token for telegram.
        default_model: The default model to load when the bot is
        initialized.
        """
        self.command_handlers = CommandHandlers(Client(host=ollama_host), default_model)
        self.application = ApplicationBuilder().token(bot_token).build()

    def run(self):
        """
        Run the bot.
        """
        self.application.add_handler(
            CommandHandler("start", self.command_handlers.start),
        )
        self.application.add_handler(
            CommandHandler("infer", self.command_handlers.inference),
        )
        self.application.run_polling()
