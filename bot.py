import sechat
from sechat.events import Events
import sys
import os
import re
import html

USERNAME = sys.argv[1]
ROOM = sys.argv[2]
EMAIL = os.environ["email"]
PASSWORD = os.environ["password"]
PHRASE = f"🐟 <i>{USERNAME}'s line quivers.</i>"

bot = sechat.Bot()
bot.login(EMAIL, PASSWORD)
r = bot.joinRoom(ROOM)
r.send("/fish")

def msg(e):
  if html.unescape(e.content) == PHRASE and e.user_id == 375672:
    r.send("/fish")
    r.send("I am automatically fishing! I am using [this Github repository](https://github.com/PlaceReporter99/auto-fish-action/) to do it. Note: this is an automatic message.")
    r.send("/fish")

r.on(Events.MESSAGE, msg)

try:
  while True:
    pass
finally:
  sys.exit(0)
