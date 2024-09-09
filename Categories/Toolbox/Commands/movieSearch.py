from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import re
import requests

@toolboxCommand("movieSearch", "🎬 Movie Search", 4)
async def movieSearch(message: Message, query: Message = False, *args):
    if not query:
        await message.reply("Enter Movie Title: ")
        return "query"
    sk = re.sub(r'\s+', ' ', query.content).strip()
    msg = await query.reply("🔃 Please Wait...")
    try:
        response = requests.get(f"https://www.omdbapi.com/?t={sk}&apikey=e430f1ee", stream=True)
        response.raise_for_status()
        data = response.json()
        if data["Response"] == "False":
            return await msg.edit("❌ Movie Not Found!", components=await backButton())
        await msg.edit(
            f"🎬 Title: {data['Title']}\n"
            f"📅 Year: {data['Year']}\n"
            f"⏳ Length: {data['Runtime']}\n"
            f"⭐ Rating: {data['Rated']}\n"
            f"🎞️ Genre: {data['Genre']}\n"
            f"🎥 Director: {data['Director']}\n"
            f"👥 Actors: {data['Actors']}\n"
            f"🌍 Country: {data['Country']}", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())