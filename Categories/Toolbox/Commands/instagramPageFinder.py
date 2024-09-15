from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("instagramPageFinder", "🔭 Instagram Page Finder", 11)
async def instagramPageFinder(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("Enter instagram page id: ")
        return "query"
    
    url = f"https://api-free.ir/api/insta.php?name={query.content}"
    msg = await query.reply("🚀 Searching... ")
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            data = response.json()
            if data.get("ok") == True:
                result = data["Result"]
                return await msg.edit(
                    f"✨ Results for *@{result['username']}*:\n"
                    f"👤 Name: {result['name']}\n"
                    f"🎮 Bio: {result['bio']}\n"
                    f"👥 Followers: {result['followers']}\n"
                    f"🔗 Following: {result['following']}\n"
                    f"📝 Posts: {result['posts']}",
                    components=await backButton()
                )

            if data.get("error") == "not found page instagram":
                return await msg.edit("❌ Page Not Found!", components=await backButton())
            
        raise Exception(result)
    except Exception as e:
        print(e)
        await msg.edit("❌ Error", components=await backButton())
    