from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("weatherInfo", "⛅ Weather Info", 5)
async def weatherInfo(message: Message, query=False, *args):
    if not query:
        await message.reply("Enter City Name: ")
        return "query"
    
    msg = await query.reply("🔃 Please Wait...")
    
    try:
        response = requests.get(f"https://api.codebazan.ir/weather/?city={query.content}", stream=True)
        response.raise_for_status()
        
        data = response.json()
        
        if 'list' in data:
            results = data['list'][0]
            main = results['main']
            wind = results['wind']
            
            # Provide detailed weather information
            return await msg.edit(f"🌤️ Weather Overview for *{data['city']['name']}/{data['city']['country']}*\n"
            f"🌡️ *Current Temp:* {main['temp']}°C\n"
            f"🔝 *Max Temp:* {main['temp_max']}°C\n"
            f"🔻 *Min Temp:* {main['temp_min']}°C\n"
            f"🧊 *Feels Like:* {main['feels_like']}°C\n"
            f"🌫️ *Humidity:* {main['humidity']}%\n\n"
            f"🌪️ *Wind Speed:* {wind['speed']} m/s\n"
            f"🧭 *Wind Direction:* {wind['deg']}°\n"
            f"💨 *Wind Gust:* {wind['gust']} m/s\n", components=await backButton())

        if data['Result'] == "The city or country is wrong":
            return await msg.edit("❌ Invalid City/Country", components=await backButton())
        
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())
