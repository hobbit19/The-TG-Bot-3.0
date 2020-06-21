# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# For The-TG-Bot-3.0
# Syntax: .wikipedia <query>

from userbot import syntax
import wikipedia


@bot.on(command(pattern="wiki (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.edit(f"Searching wikipedia for {input_str}")
    result = ""
    results = wikipedia.search(input_str)
    for i in results:
        page = wikipedia.page(i)
        url = page.url
        result += f"[{i}]({url})\n"
    await event.edit("**Wikipedia search complete**\n**Query**: {}\n**Result**:\n{}".format(input_str, result))

syntax.update({"wikipedia": "\
```.wiki <query>```\
\nUsage: Search for query on Wikipedia.\
"})
