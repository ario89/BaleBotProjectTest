from bale import Message
import requests
from Categories.Toolbox.toolbox import backButton, toolboxCommand

@toolboxCommand("cardInfo", "💳 Get Card Info", 10)
async def cardInfo(message: Message, query=False, *args):
    return await message.reply("⚠️ *This Feature Is W.I.P*", components=await backButton())
    if not query:
        await message.reply("Enter Card Number: ")
        return "query"
    try:
        response = requests.get(f"https://api.apieco.ir/finnotech-sandbox-card-number-check/cards/{query}?trackId=")
        response.raise_for_status()
        data = response.json()
        return await query.reply(data["name"], components=await backButton())
    except Exception:
        return await query.reply("❌ an Error Occurred!", components=await backButton())