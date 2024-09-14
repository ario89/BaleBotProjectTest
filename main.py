from dotenv import load_dotenv
from Variable import Variable
from utils import menuCompentents
from bale import Bot, CallbackQuery, Message
from Categories.Toolbox.Commands import esmFamilCheat
from os import getenv
import asyncio
import Categories.Toolbox.toolbox as toolbox
import Categories.AI.AI as ai
import Categories.downloader as downloader

load_dotenv()

# Initialize Bot
client = Bot(getenv("TOKEN"))

TOOLBOX = Variable("toolbox", "⚙️ ToolBox ⚙️", "main", toolbox.main)
AI = Variable("ai", "🤖 AI 🤖", "main", ai.main)
DOWNLOADER = Variable("downloader", "📩 Downloaders", "main",downloader.main)
# Constants
WELCOME_TEXT = """Hi {name}, Welcome to Ario's test bot!"""

toolbox.loadToolbox()
ai.loadAI()

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
        msg = await Variable.getObjectByDisplayName(content).execute(message)
        if msg == "query": await queryInput(message, content)
        
@client.event
async def on_callback(callback: CallbackQuery):
    data = callback.data
    if data == "back:toolbox":
        await toolbox.main(callback.message)
        
    elif data == "back:ai":
        await AI.main(callback.message)
    
    if data.startswith("esmfamil:"):
        clean = data.removeprefix("esmfamil:")
        await esmFamilCheat.esmFamilCheat(callback.message, clean)
        
    if data.startswith("translate:"):
        clean = data.removeprefix("translate:")
        await callback.message.reply("Enter Query: ")
        await queryInput(callback.message, Variable.getObjectByName("translate").displayName, clean)
        
    if data.startswith("morse:"):
        clean = data.removeprefix("morse:")
        await callback.message.reply("Enter Query: ")
        await queryInput(callback.message, Variable.getObjectByName("morse").displayName, clean)
        
async def queryInput(message:Message, content:str, *args):
    options_list = [var.displayName for var in Variable.variableList()]
    def answer_checker(m: Message):
            return message.chat_id == m.chat_id and bool(message.text)
    try:
        answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=30.0)
    except asyncio.TimeoutError:
        return await message.chat.send('⏱️ Timeout')
    else:
        if answer_obj.content not in options_list:            
            return await Variable.getObjectByDisplayName(content).execute(message, answer_obj, *args)

if __name__ == "__main__":
    client.run()