import asyncio
import os
import random
import re
import requests
import wget
import datetime
import math
from cowpy import cow
from random import randint, choice

from kannax import Message, kannax


@kannax.on_cmd("(HUE)$", about={"header": "HUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUE"}, trigger="", allow_via_bot=False)
async def hue_(message: Message):
    """HUE"""
    hue = "HUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUE"
    for _ in range(4):
        hue = hue[:-7] + "HUEHUEHUHUEHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUEHUEHUHUE"
        await message.try_to_edit(hue)
