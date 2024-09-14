from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from codern import api

ERORR_RESULT = """خروجی ناقص امکان وجود خطا در سرور !
لطفا در دقایقی دیگر تلاش کنید"""

@AICommand("chatgpt", "🤖 ChatGPT", 0)
async def ChatGPT(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await message.chat.send("🪄 Typing...")
    
    try:
        result = api.Ai_chat_GPT(query.content)
        if result == ERORR_RESULT:
            raise Exception(result)
        back = await backButton()
        buttons = back.add(InlineKeyboardButton("Reuse ChatGPT", callback_data="ai:chatgpt"))
        await msg.edit(result, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=await backButton())
        print(e)