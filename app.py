import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token="xoxb-6088609219633-6794337178144-KJbHv9Jd4qUHC46tpSJ1EeiH")

if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A06NLJ47KCM-6771925629714-036d23b3de3f3540941419082a954a8e799b936af6320e931e890832d8960b1a").start()