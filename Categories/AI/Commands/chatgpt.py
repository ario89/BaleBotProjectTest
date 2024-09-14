from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from codern import api

@AICommand("chatgpt", "🤖 ChatGPT", 0)
async def ChatGPT(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await query.reply("🪄 Typing...")
    
    try:
        result = api.Ai_chat_GPT(query.content)
        back = await backButton()
        buttons = back.add(InlineKeyboardButton("Reuse ChatGPT", callback_data="ai:chatgpt"))
        await msg.edit(result, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=await backButton())
        print(e)