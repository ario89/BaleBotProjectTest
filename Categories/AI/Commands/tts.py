from bale import Message, InputFile
from Categories.AI.AI import AICommand, backButton
from utils import inlineComponents
from codern import api
import requests

FILE_URL = 'Assets/temp/audio.mp3'

@AICommand("tts", "🗣️ Text-To-Speach", 2)
async def tts(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("❓ Enter Text To Convert ")
        return "query"
    
    msg = await query.reply("🕹️ Generating...")
    continueChat = inlineComponents({"Reuse TTS": "ai:tts"})
    buttons = continueChat.add(backButton())    
    
    try:
        result:str = api.create_voice(query.content)
        response = requests.get(result)
    
        with open(FILE_URL, 'wb') as f:
            f.write(response.content)

        with open(FILE_URL, 'rb') as f:
            audio_file = InputFile(f, file_name="Audio.mp3")
        
        await msg.edit("🌐 Uploading...")
        await query.reply_document(document=audio_file, components=buttons)
        return await msg.delete()
    except Exception as e:
        await msg.edit("❌ Error", components=backButton())
        print(e)
        
    with open(FILE_URL, 'w+') as f:
        f.write('')