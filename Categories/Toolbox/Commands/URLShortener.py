from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("urlShortener", "🔗 URL Shortener", 4)
async def urlShortener(message: Message, query=False, *args):
    if not query:
        msg = await message.reply("🔗 Please Enter URL: ")
        return "query"
    msg = await query.reply("🔃 Please Wait...")
    try:
        response = requests.get(f"https://vurl.com/api.php?url={query.content}", stream=True)
        response.raise_for_status()
        data = response.content.decode()
        if data == "Invalid URL":
            return await msg.edit("❌ Invalid URL", components=await backButton())
        return await msg.edit(f"✅ Shortened URL: {data}", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())