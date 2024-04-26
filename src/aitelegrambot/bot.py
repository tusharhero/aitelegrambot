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

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    Application,
)
from ollama import Client
from aitelegrambot.commandhandlers import (
    NormalCommandHandlers,
    CommandHandlers,
    AdministrationCommandHandlers,
    OllamaState,
)


class TelegramBot:
    """
    A class that implements a Telegram bot using the Ollama framework.
    """

    def __init__(
        self,
        ollama_host: str,
        bot_token: str,
        default_model: str,
        administrator_user_id: int,
        enable_streaming_response: bool,
        message_chunk_size: int,
    ):
        """
        Initializes an instance of TelegramBot.

        Arguments:
        ==========
        ollama_host: Host address of the `ollama` service.
        bot_token: Bot token for telegram.
        default_model: The default model to load when the bot is
        initialized.
        administrator_user_id: Telegram user id of the administrator.
        enable_streaming_response: Enable streaming response option.
        message_chunk_size: The number of words to be send at a time.
        """
        ollama_state: OllamaState = OllamaState(
            Client(host=ollama_host), default_model, message_chunk_size
        )
        self.normal_command_handlers: CommandHandlers = NormalCommandHandlers(
            ollama_state
        )
        self.normal_command_handlers.inference = (
            self.normal_command_handlers.stream_inference
            if enable_streaming_response
            else self.normal_command_handlers.basic_inference
        )

        self.administrative_command_handlers: CommandHandlers = (
            AdministrationCommandHandlers(ollama_state, administrator_user_id)
        )

        self.application: Application = ApplicationBuilder().token(bot_token).build()

    def run(self):
        """
        Run the bot.
        """
        self.application.add_handler(
            CommandHandler("start", self.normal_command_handlers.start),
        )
        self.application.add_handler(
            CommandHandler("infer", self.normal_command_handlers.inference),
        )
        self.application.add_handler(
            CommandHandler(
                "list_models", self.administrative_command_handlers.list_models
            )
        )
        self.application.add_handler(
            CommandHandler(
                "change_model",
                self.administrative_command_handlers.change_model,
            )
        )
        self.application.add_handler(
            CommandHandler(
                "pull_model",
                self.administrative_command_handlers.pull_model,
            )
        )
        self.application.add_handler(
            CommandHandler(
                "remove_model",
                self.administrative_command_handlers.remove_model,
            )
        )

        self.application.run_polling()
