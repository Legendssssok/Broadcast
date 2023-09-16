from pyrogram import Client, filters
from pyrogram.types import Message
import os

from pyromod import listen 

import asyncio

API_ID = 11573285
API_HASH = "f2cc3fdc32197c8fbaae9d0bf69d2033"
TOKEN = "6138700672:AAEvQsV-N4LRIrCY0_M4bHLpNaRXnJWHyLg"

app = Client("Legend", api_id = API_ID, api_hash = API_HASH, bot_token = TOKEN )

@app.on_message(filters.command("start"))
async def _start(_, message):
    user = message.from_user.mention
    bot = (await _.get_me()).mention
    await message.reply_text("Hello")
    

async def broadcast(session, text, time):
    list = []
    async with Client("Legendss", api_id=API_ID, api_hash=API_HASH, session_string=session) as owo:
           async for dialog in owo.get_dialogs():
              if dialog.chat.permissions is not None and dialog.chat.permissions.can_send_messages:
              	list.append(dialog.chat.id)
           print(list)
           if len(list) > 300:
               return f"There is total {len(list)} which is greater than 300\nI Only Support upto 300 group so leave some group"
           while True:
           	for i in list:
                    try:
                        await owo.send_message(int(i), text)
                        if i < 5:
                            await asyncio.sleep(1)
                        if i < 10 and i > 5:
                             await asyncio.sleep(10)
                        if i < 50 and i > 10:
                             await asyncio.sleep(15)
                        if i < 80 and i > 50:
                             await asyncio.sleep(20)
                        if i < 100 and i > 80:
                            await asyncio.sleep(1)
                        if i < 120 and i > 100:
                             await asyncio.sleep(10)
                        if i < 150 and i > 120:
                             await asyncio.sleep(15)
                        if i < 300 and i > 150:
                             await asyncio.sleep(20)
                    except FloodWait as x:
                        print(f"Flood Wait Second of : {x.value}")
                        await asycio.sleep(x.value)
                    except:
			pass
           	await asyncio.sleep(int(time))
    return "Done ✅"
          
             	    
              
@app.on_message(filters.command("bc"))
async def bc(client, message):
	chat_id = message.chat.id
	print(message.chat.id)
	my_session = await client.ask(chat_id, "Give String Session")
	text = await client.ask(chat_id, "Give me text")
	time = await client.ask(chat_id, "Give me time in secon")
	await message.reply_text("Processing....")
	lol = await broadcast(my_session.text, text.text, time.text)
	await message.reply_text(f{lol}")


app.run()
