import os
import logging

from slack_bolt import App, Complete
from slack_bolt.adapter.socket_mode import SocketModeHandler


# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(level=logging.DEBUG)

# Register Function
@app.function("sample_function")
def sample_function(event, complete: Complete, logger: logging.Logger):
    try:
        message = event["inputs"]["message"]
        complete(
            outputs={
                "updatedMsg": f":wave: You submitted the following message: \n\n>{message}"
            }
        )
    except Exception as e:
        logger.error(e)
        complete(error="Cannot post the message, ask your admin to look at the logs")
        raise e

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()