from bale import Message, InputFile, InlineKeyboardButton
from Categories.Extract.extractors import extractorCommand, backButton
from codern import api
import os
import requests

FILE_PATH = 'Assets/temp/audio.mp3'

@extractorCommand("tts", "🗣️ Text-To-Speech", 2)
async def tts(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ Enter Text To Convert (Persian): ")
        return "query"
    
    msg = await message.chat.send("🕹️ Generating...")
    back = await backButton()
    buttons = back.add(InlineKeyboardButton("Reuse TTS", callback_data="extract:tts"))
    
    try:
        result:str = api.create_voice(query.content.replace("‌", " "), "FaridNeural")
        response = requests.get(result)
    
        with open(FILE_PATH, 'wb') as f:
            f.write(response.content)

        with open(FILE_PATH, 'rb') as f:
            if os.path.getsize(FILE_PATH) > 0:
                audio_file = InputFile(f, file_name="Audio.mp3")
            else: return await msg.edit("❌ Invalid Input", components=buttons)
        
        await msg.edit("🌐 Uploading...")
        await query.reply_document(document=audio_file,caption="✅ Generated",components=buttons)
        return await msg.delete()
    except Exception as e:
        await msg.edit("❌ Error", components=buttons)
        print(e)
        
    with open(FILE_PATH, 'w+') as f:
        f.write('')