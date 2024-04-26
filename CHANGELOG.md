# CHANGELOG

## 0.0.0

- Add README, LICENSE, and pyproject.toml.

## 0.1.0

- Add basic functionality.
- Rename project to aitelegrambot from rationalai-telegram-bot.

## 0.1.1

- Add script for pipx.
- Add additonal instructions in README.

## 0.1.2

- Use a seperate module for constant messages.

## 0.1.3

- Fix bug because of which the command was being sent to the LLM.

## 0.2.0

- The bot now replies to the message which ran the infer command.

## 0.3.0

- The bot has an administration feature which allows the admin to:
  1. Change the current model.
  2. Pull a model.
  3. Delete a model.
  4. List models.

## 0.3.1

- Fix bug with list models command: Error and reply when no models are
  available.

## 0.4.0

- Add support for ~streaming responses~ (Receiving the messages, as
  the LLM generates them).

_The following two releases are just very basic bug fixes which should
  have been properly tested._
## 0.4.1

- Fix bugs

## 0.4.2

- Fix bugs

## 0.5.0

- Add support for both, streaming and non-streaming inference.
- Default to non-streaming.
- New option to customize streaming or non-streaming.

## 0.5.1

- Fix bug
