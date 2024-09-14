from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from codern import api

@AICommand("blackbox", "📦 BlackBox AI", 1)
async def blackbox(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await message.chat.send("🪄 Typing...")
    back = await backButton()
    buttons = back.add(InlineKeyboardButton("Reuse BlackBox", callback_data="ai:blackbox"))
    
    try:
        result:str = api.Ai_black_box(query.content)
        await msg.edit(result.removeprefix("v=undefined"), components=buttons)
    except Exception as e:
        await msg.edit("❌ Error")
        print(e)