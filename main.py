from asyncio import sleep
from pyrogram import client, filters
from pyrogram.errors import FloodWait
import config
import asyncio

app = client.Client('tttt', api_hash=config.api_hash, api_id=config.api_id)

@app.on_message(filters.command('help', '.') & filters.me)
async def help(_, msg):
    await msg.edit(r'''
**Команды**
.help - вывести это сообщение
.zxc - считает 1000-7 редактируя сообщение
.ghoul - считает 1000-7 отправляя сообщения
.type - эффект печати
.chat id - пишет айди чата
.message id - пишет айди сообщения (нужно ответить на сообщение)
''')

@app.on_message(filters.command('zxc', '.') & filters.me)
async def zxc(_, msg):
    x = 1000
    while x > 7:
        try:
            await msg.edit(f'{x}-7={x-7}')
            x-=7
        except FloodWait as f:
            await sleep(f.value)

@app.on_message(filters.command('ghoul', '.') & filters.me)
async def ghoul(_, msg):
    x = 1000
    while x > 7:
        try:
            await app.send_message(msg.chat.id, f'{x}-7={x-7}')
            x-=7
        except FloodWait as f:
            await sleep(f.value)
    await app.send_message(msg.chat.id, 'я гуль')

@app.on_message(filters.command('type', '.') & filters.me)
async def type(_, message):
    _, msg=message.text.split(maxsplit=1)
    stroka=''
    for symbol in msg[:-1]:
        stroka+=symbol
        try:
            await message.edit(stroka+'¦')
        except FloodWait as f:
            await sleep(f.value)
    await message.edit(msg)

@app.on_message(filters.command('chat id', '.') & filters.me)
async def chat_id(_, msg):
    await msg.edit(f'id чата: {msg.chat.id}')

@app.on_message(filters.command('message id', '.') & filters.me)
async def message_id(_, msg):
    if msg.reply_to_message_id:
        await msg.edit(f'id сообщения: {msg.reply_to_message_id}')
    else: 
        await msg.edit(f'Нужно ответить на сообщение')
        await asyncio.sleep(2)
        await msg.delete()

app.run()