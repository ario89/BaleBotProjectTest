from bale import Message, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from openai import OpenAI

client = OpenAI(
    api_key="sk-tWIbT34A0TuzckeViv9aIYy2o0Dtr0qnjcUM8QTR5Ny1d4DK",
    base_url="https://api.chatanywhere.tech/v1"
)

@AICommand("chatgpt", "🤖 ChatGPT", 0)
async def ChatGPT(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ What Do You Want Help With? ")
        return "query"
    
    msg = await message.chat.send("🪄 Typing...")
    
    try:
        messages = [{'role': 'user','content': query.content},]
        result = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        back = await backButton()
        buttons = back.add(InlineKeyboardButton("Reuse ChatGPT", callback_data="ai:chatgpt"))
        await msg.edit(result.choices[0].message.content, components=buttons)
    except Exception as e:
        await msg.edit("❌ Error", components=await backButton())
        print(e)