from bale import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import re
import requests

async def esmFamilCheat(message:Message, letter:str=None, *args):
    if not letter:
        await message.reply("Please Choose Letter From List Below:", components=alphabetList())
        return
        
    url = f"https://api.codebazan.ir/esm-famil/?text={letter}"
    msg = await message.reply("🔃 Please Wait...")
    
    response = requests.get(url)
    try: 
        if response.status_code == 200:
            formatted_message = formatResponse(response.content.decode())
            return await msg.edit(formatted_message, components=await backButton())
        return await msg.edit("❌ Error", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())
    
    
def alphabetList():
    alphabet = [
    'الف', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 
    'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 
    'م', 'ن', 'و', 'ه', 'ی']

    markup = InlineKeyboardMarkup()
    for letter in alphabet:
        markup.add(InlineKeyboardButton(text=letter,callback_data=f"esmfamil:{letter}"))
        
    return markup
    
def formatResponse(data):
    sections = {
        "اسم": "🎤",
        "فامیل": "👥",
        "شهر": "🌍",
        "کشور": "🇮🇷",
        "میوه": "🍉",
        "غذا": "🍲",
        "رنگ": "🎨",
        "حیوان": "🐴",
        "ماشین": "🚗",
        "اشیاء": "🛠️",
        "گل": "🌸",
        "شغل": "👩‍🍳",
        "اعضای بدن": "🦵",
        "پوشاک": "👕",
        "مشاهیر": "👤",
        "ورزش": "🤸‍♂️",
        "فیلم": "🎥",
        "کارتون": "📺",
    }

    message = "🎮 *تقلب بازی اسم و فامیل* 🎮\n\n"

    clean_data = re.sub(r'<.*?>', '', data)
    clean_data = re.sub(r'\s+', ' ', clean_data).strip()

    flag = True
    for key, emoji in sections.items():
        if key in clean_data:
            pattern = rf'{key}\s*[:=]\s*(.*?)(?=\s*(?:[^\s:]+)\s*[:=]|$)'
            match = re.search(pattern, clean_data)
            if match:
                items = match.group(1).strip()
                if items and not items.isdigit() and items.strip() != "":
                    flag = False
                    message += f"{emoji} {key}: \n✅ {items}\n{'—'*20}\n\n"

    if not flag:
        return message
