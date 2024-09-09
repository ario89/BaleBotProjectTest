from bale import Message
from random import choice
from Categories.Toolbox.toolbox import backButton, toolboxCommand

@toolboxCommand("randomMotiv", "😊 Random Motivation", 3)
async def random_motivation(message: Message, *args):
    MOTIVATION_PATH = "./Assets/motivation.txt"
    
    try:
        with open(MOTIVATION_PATH, 'r', encoding="utf-8") as f:
            data = f.read().replace("\n", "").split("***")
            await message.reply(f"🔰 {choice(data)}", components=await backButton())
    except FileNotFoundError:
        await message.reply("❌ Motivation file not found!", components=await backButton())