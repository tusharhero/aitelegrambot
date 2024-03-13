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

from telegram import Update
from telegram.ext import ContextTypes
from ollama import Client
import aitelegrambot.constants as constants
import re


class CommandHandlers:
    """
    Class for handling commands, and ollama.
    """

    def __init__(self, ollama_client: Client, model: str):
        """
        Arguments:
        ==========
        ollama_client: The Olama client to use for sending messages.
        model: The model to use for inference.
        """
        self.ollama_client = ollama_client
        self.model = model

    async def start(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Informs the user about its version.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=constants.WELCOME_MESSAGE
        )

    async def inference(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ):
        """
        Performs inference on the given update.

        Arguments:
        ==========
        update: The update to be processed.
        context: The context for the inference.
        """

        # extracting query from incoming message using regex
        query: str = re.split(" ", update.message.text, 1)[1]

        await update.message.reply_text(
            text=self.ollama_client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
            )["message"]["content"],
        )
