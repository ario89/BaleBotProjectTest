from dotenv import load_dotenv
from Categories.Extract.Commands import tts
from Variable import Variable
from utils import menuCompentents
from bale import Bot, CallbackQuery, Message
from Categories.Toolbox.Commands import esmFamilCheat
from Categories.AI.Commands import chatgpt_35,chatgpt_4o_mini,blackbox
from os import getenv
import asyncio
import Categories.Toolbox.toolbox as toolbox
import Categories.AI.AI as ai
import Categories.Downloader.downloader as downloader
import Categories.Extract.extractors as extract

load_dotenv()

# Initialize Bot
client = Bot(getenv("TOKEN"))

TOOLBOX = Variable("toolbox", "⚙️ ToolBox ⚙️", "main", toolbox.main)
AI = Variable("ai", "🤖 AI 🤖", "main", ai.main)
EXTRACTORS = Variable("extractors", "📨 Extractors", "main", extract.main)
# DOWNLOADER = Variable("downloader", "📩 Downloaders", "main",downloader.main)
# Constants
WELCOME_TEXT = """Hi {name}, Welcome to Ario's test bot!"""

toolbox.loadToolbox()
ai.loadAI()
extract.loadExtractors()
# downloader.loadDownloader()


async def mainCommand(message:Message):
    await message.reply(WELCOME_TEXT.format(name=message.author.first_name), components=menuCompentents("main", Variable.variableList()))

@client.event
async def on_ready():
    print(client.user.username, "is Online!")

@client.event
async def on_message(message: Message):
    options_list = [var.displayName for var in Variable.variableList()]
    content = message.content
            
    if content in ["/start", "🔙 Back To Main 🔙"]:
        await mainCommand(message)      
        
    elif content in options_list:
        msg = await Variable.getObjectByDisplayName(content).execute(message)
        if msg == "query": await queryInput(message, content)
        
@client.event
async def on_callback(callback: CallbackQuery):
    data = callback.data
    if data == "back:toolbox":
        await toolbox.main(callback.message)
        
    elif data == "back:ai":
        await ai.main(callback.message)
        
    elif data == "back:extract":
        await extract.main(callback.message)
    
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
        
    if data.startswith("ai:"):
        clean = data.removeprefix("ai:")
        if clean == "chatgpt3.5":
            await chatgpt_35.ChatGPT3(callback.message)
            return await queryInput(callback.message, Variable.getObjectByName('chatgpt-3.5').displayName)
        elif clean == "chatgpt4o":
            await chatgpt_4o_mini.ChatGPT4(callback.message)
            return await queryInput(callback.message, Variable.getObjectByName('chatgpt-4o-mini').displayName)
        elif clean == "blackbox":
            await blackbox.blackbox(callback.message)
            return await queryInput(callback.message, Variable.getObjectByName('blackbox').displayName)
    if data.startswith("extract:"):
        clean = data.removeprefix("extract:")
        if clean == "tts":
            await tts.tts(callback.message)
            return await queryInput(callback.message, Variable.getObjectByName('tts').displayName)

async def queryInput(message:Message, content:str, *args):
    options_list = [var.displayName for var in Variable.variableList()]
    def answer_checker(m: Message):
            return message.chat_id == m.chat_id and (bool(message.text) or bool(message.caption))
    try:
        answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=30.0)
    except asyncio.TimeoutError:
        return await message.chat.send('⏱️ Timeout')
    else:
        if answer_obj.content not in options_list:            
            return await Variable.getObjectByDisplayName(content).execute(message, answer_obj, *args)

if __name__ == "__main__":
    client.run()