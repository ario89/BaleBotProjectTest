from bale import Message
from utils import inlineComponents
from Categories.AI.AI import AICommand, backButton
from codern import api

@AICommand("chatgpt", "🤖 ChatGPT", 0)
async def ChatGPT(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await query.reply("🪄 Typing...")
    continueChat = inlineComponents({"Reuse ChatGPT": "ai:chatgpt"})
    buttons = continueChat.add(backButton())    
    
    try:
        result = api.Ai_chat_GPT(query.content)
        await msg.edit(result, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=backButton())
        print(e)