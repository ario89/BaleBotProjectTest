from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("arzPrice", "💲Arz Price", 6)
async def arzPrice(message: Message, *args):
    url = "https://api.codebazan.ir/arz/?type=arz"
    msg = await message.reply("🔃 Please Wait...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        if response.json()["Ok"]:
            results = response.json()["Result"]
            output = ""
            for item in results:
                output += f"- {item['name']}: {item['price']} ریال\n"
            return await msg.edit(output, components=await backButton())
        return await msg.edit("❌ Error", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error", components=await backButton())