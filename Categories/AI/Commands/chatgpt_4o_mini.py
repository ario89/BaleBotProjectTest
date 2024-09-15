from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from openai import OpenAI
from os import getenv

client = OpenAI(
    api_key=getenv("OPENAI_TOKEN"),
    base_url="https://api.chatanywhere.tech/v1"
)

@AICommand("chatgpt-4o-mini", "🤖 ChatGPT 4o-Mini", 0)
async def ChatGPT4(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await message.chat.send("🪄 Typing...")
    
    try:
        messages = [{'role': 'user','content': query.content},]
        result = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        back = await backButton()
        buttons = back.add(InlineKeyboardButton("Reuse GPT-4o", callback_data="ai:chatgpt4o"))
        await msg.edit(result.choices[0].message.content, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=await backButton())
        print(e)