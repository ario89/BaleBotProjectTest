from bale import Message
from Categories.AI.AI import AICommand, backButton
from utils import inlineComponents
from codern import api

@AICommand("blackbox", "📦 BlackBox AI", 1)
async def blackbox(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await query.reply("🪄 Typing...")
    continueChat = inlineComponents({"Reuse BlackBox": "ai:blackbox"})
    buttons = continueChat.add(backButton())    
    
    try:
        result:str = api.Ai_black_box(query.content)
        await msg.edit(result.removeprefix("v=undefined"))
    except Exception as e:
        await msg.edit("❌ Error")
        print(e)