#Made by W24
from util import hook
import random

fires = [
    "14*click*","14*click*" ,"4You died!" ,"14*click*"
]

@hook.command(autohelp=False)
def fire(inp):
    return fires[random.randint(0, len(fires) - 1)].decode("utf-8", "ignore")
