from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from openai import OpenAI
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = OpenAI(
    api_key=getenv("OPENAI_TOKEN"),
    base_url="https://api.chatanywhere.tech/v1"
)

@AICommand("chatgpt-3.5", "🤖 ChatGPT 3.5-Turbo", 2)
async def ChatGPT3(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await message.chat.send("🪄 Typing...")
    
    try:
        messages = [{'role': 'user','content': query.content},]
        result = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        back = await backButton()
        buttons = back.add(InlineKeyboardButton("Reuse GPT 3.5", callback_data="ai:chatgpt3.5"))
        await msg.edit(result.choices[0].message.content, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=buttons)
        print(e)