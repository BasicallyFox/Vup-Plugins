import random

from kannax import Message, kannax

@kannax.on_cmd('sort' , about={"header": 'estou com sorte?'})
async def sort_(message: Message):
    sort = f"Número da sorte: {random.choice(range(0, 10))}"
    await message.edit(sort)
