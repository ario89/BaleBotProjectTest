from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import csv
import requests

@toolboxCommand("timeInfo", "⏰ Date/Time Info",5)
async def timeInfo(message: Message, query: Message = False, *args):
    if not query:
        await message.reply("Enter City Name (English):")
        return "query"
    msg = await query.reply("🔃 Please Wait...")
    try:
        latitude, longitude = getCords(query.content)
        if not latitude or not longitude:
            return await msg.edit("❌ Invalid City", components=await backButton())
        response = requests.get(f"https://api.sunrisesunset.io/json?lat={latitude}&lng={longitude}", stream=True)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'OK':
            results = data['results']
            utc_offset = results['utc_offset']
            
            hours = utc_offset // 60
            minutes = abs(utc_offset % 60)
            utc_offset_str = f"{hours:+d}:{minutes:02d}"
            
            await msg.edit(f"🏙️ {query.content.lower().title()}\n"
                            f"📅 Date: {results['date']}\n"
                            f"🌅 Sunrise: {results['sunrise']}\n"
                            f"🌇 Sunset: {results['sunset']}\n"
                            f"☀️ Solar Noon: {results['solar_noon']}\n"
                            f"🕒 Day Length: {results['day_length']}\n"
                            f"🌍 Timezone: {results['timezone']}\n"
                            f"🕓 UTC Offset: {utc_offset_str}", components=await backButton())
        else:
            return await msg.edit("❌ Error!", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())
    
def getCords(sk):
    lat,lng = None,None
    with open('./Assets/worldcities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0].lower() == sk.lower():
                lat=row[1]
                lng=row[2]
                break
    
    return lat,lng