from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("melliCodeVerify", "🗂️ Verify Melli Code", 8)
async def melliCodeVerifier(message: Message, query: Message = False, *args):
    if not query:
        await message.reply("Enter Melli Code: ")
        return "query"
    msg = await query.reply("🔃 Please Wait...")
    try:
        url = f"https://api.codebazan.ir/codemelli/?code={query.content}"
        response = requests.get(url, stream=True)
        response.raise_for_status()
        data = response.json()
        result = data["Result"]
        if result == "The code is valid" and data["OK"] == "true":
            return await msg.edit("✅ Valid Code", components=await backButton())
        return await msg.edit("❎ Invalid Code", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error", components=await backButton())