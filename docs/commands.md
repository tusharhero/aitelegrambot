# Commands
Commands refer to the commands users can run in the telegram bot.
## Normal Commands
Commands only available for normal users.
### Start command
#### invocation
```
\start
```
#### description

It is the welcome message command, it just gives information the
version of aitelegram being used.

### Inference command
#### invocation
```
\infer <query>
```
#### description

It is used to run an inference on the LLM, it can act in two ways
according to the `ENABLE_STREAMING_RESPONSE` option, if it is disabled
(default), the bot will send at the entire response at once, when the
inference is done. If the option is enabled, the bot will stream the
tokens into the response as it is being generated.

## Administration Commands
Commands only available for the administrator.
### List model command
#### invocation
```
\list_models
```
#### description

It lists each available model along with the command to switch to it.

### Change model command
#### invocation
```
\change_model <model_name>
```
#### description

Changes the model to <model_name>.

### Pull model
#### invocation
```
\pull_model <model_name>
```
#### description

Pull <model_name> from Ollama's servers.

### Remove model
#### invocation
```
\delete_model <model_name>
```
#### description

Delete <model_name>.
