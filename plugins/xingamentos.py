#by joaoppierri"

from kannax import Message, kannax

@kannax.on_cmd("Vsf|vsf", about={"header": "vai se foder"})
async def vsf_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        vsf = f"vai se foder"
        await message.edit(vsf)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" {user_.mention} vai tomar no seu cu"
    await message.edit(msg_)


@kannax.on_cmd("Pqp|pqp", about={"header": "puta que pariu"})
async def pqp_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        pqp = f"puta que pariu"
        await message.edit(pqp)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" {user_.mention} vai pra puta que pariu"
    await message.edit(msg_)

@kannax.on_cmd("Crl|crl", about={"header": "caralho"})
async def crl_(message: Message):
    reply_ = message.reply_to_message
    if not reply_:
        crl = f"caralho"
        await message.edit(crl)
        return
    user_ = await kannax.get_users(reply_.from_user.id)
    msg_ = f" {user_.mention} vai pra casa do caralho"
    await message.edit(msg_)
