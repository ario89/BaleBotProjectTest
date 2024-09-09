from dotenv import load_dotenv
from Variable import Variable
from utils import menuCompentents
from bale import Bot, CallbackQuery, Message
from os import getenv
import asyncio
import Categories.Toolbox.toolbox as toolbox
import Categories.AI as AI
import Categories.downloader as downloader

load_dotenv()

# Initialize Bot
client = Bot(getenv("TOKEN"))

TOOLBOX = Variable("toolbox", "⚙️ ToolBox ⚙️", "main", toolbox.main)
AI = Variable("ai", "🤖 AI 🤖", "main", AI.main)
DOWNLOADER = Variable("downloader", "📩 Downloaders", "main",downloader.main)
# Constants
WELCOME_TEXT = """Hi {name}, Welcome to Ario's test bot!"""

toolbox.loadToolbox()

@client.event
async def on_ready():
    print(client.user.username, "is Online!")

@client.event
async def on_message(message: Message):
    options_list = [var.displayName for var in Variable.variableList()]
    content = message.content
        
    if content == "/start":
        await message.reply(WELCOME_TEXT.format(name=message.author.first_name), components=menuCompentents("main", Variable.variableList()))

    elif content in options_list:
        msg = await Variable.getObj(content).execute(message)
        if(msg == "query"):
            def answer_checker(m: Message):
                return message.author == m.author and bool(message.text)
            try:
                answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=30.0)
            except asyncio.TimeoutError:
                return await message.chat.send('⏱️ Timeout')
            else:
                if answer_obj.content not in options_list:
                    return await Variable.getObj(content).execute(message, answer_obj)
        
@client.event
async def on_callback(callback: CallbackQuery):
    if callback.data == "back:toolbox":
        await toolbox.main(callback.message)
    if callback.data.startswith("esmfamil:"):
        clean = callback.data.removeprefix("esmfamil:")
        await toolbox.esmFamilCheat(callback.message, clean)

if __name__ == "__main__":
    client.run()