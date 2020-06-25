# For The-TG-Bot-3.0
# By Priyam Kalra
# Syntax .search <text>

from userbot import syntax


@bot.on(command(pattern="curtana ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    chat = event.chat_id
    async for message in bot.iter_messages(chat):
        msg = message.text
        if args in msg:
            await event.edit(msg)
            break
        else:
            await event.edit(f"Nothing found for query: **{args}**")
