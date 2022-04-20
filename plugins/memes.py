import httpx

from kannax import Message, kannax

@kannax.on_cmd(
    "bird",
    about={
        "header": "send beta",
        "usage": "send a msg {tr}send <text>",
    },
)
async def bird_photo(message: Message):
   http = httpx.AsyncClient()
   r = await http.get("http://shibe.online/api/birds")
   bird = r.json()
   await message.delete()
   await message.reply_photo(bird[0], caption="🐦")


@kannax.on_cmd(
    "redpanda",
    about={
        "header": "send beta",
        "usage": "send a msg {tr}send <text>",
    },
)
async def redpanda_photo(message: Message):
   http = httpx.AsyncClient()
   r = await http.get("https://some-random-api.ml/img/red_panda")
   rpanda = r.json()
   await message.delete()
   await message.reply_photo(rpanda["link"], caption="🐼")



@kannax.on_cmd(
    "panda",
    about={
        "header": "send panda",
        "usage": "send photo panda {tr}panda",
    },
)
async def panda_photo(message: Message):
   http = httpx.AsyncClient()
   r = await http.get("https://some-random-api.ml/img/panda")
   panda = r.json()
   await message.delete()
   await message.reply_photo(panda["link"], caption="🐼")


@kannax.on_cmd(
    "fox",
    about={
        "header": "send beta",
        "usage": "send a msg {tr}send <text>",
    },
)
async def fox_photo(message: Message):
   http = httpx.AsyncClient()
   r = await http.get("https://some-random-api.ml/img/fox")
   fox = r.json()
   await message.delete() 
   await message.reply_photo(fox["link"], caption="O que a Raposa diz?")
