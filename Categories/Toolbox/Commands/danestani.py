from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("danestani", "⁉️ Danestani", 3)
async def danestani(message: Message, *args):
    url = "https://api.codebazan.ir/danestani/"
    msg = await message.reply("🔃 Please Wait...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return await msg.edit(f"⁉️ {response.content.decode()}", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())