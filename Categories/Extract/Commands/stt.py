from bale import Message
from Categories.Extract.extractors import extractorCommand, backButton
from pydub import AudioSegment
import speech_recognition as sr
import os

@extractorCommand("stt", "🦜 Extract Text from Voice", 3)
async def stt(message: Message, query: Message = False, *args):
    if not query:
        await message.reply("Send Voice: ")
        return "query"
    if not query.audio:
        return await query.reply("❌ No Voice Found!")

    msg = await query.reply("🔃 Please Wait...")

    try:
        audio_path = "Assets/temp/temp.ogg"
        with open(audio_path, 'wb') as f:
            await query.audio.save_to_memory(f)

        extracted_text = convertToText(audio_path)
        return await msg.edit(f"🦜 Extracted Text: {extracted_text}", components=await backButton())

    except Exception as e:
        print(f"Error: {e}")
        return await msg.edit("❌ Error extracting text", components=await backButton())
    
def convertToWav(audio_file, output_file):
    audio = AudioSegment.from_file(audio_file)
    audio.export(output_file, format="wav")

def convertToText(audio_file):
    recognizer = sr.Recognizer()
    wav_file = "Assets/temp/temp.wav"
    
    try:
        convertToWav(audio_file, wav_file)

        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data, language='fa')

        if text.strip():
            return text
        else:
            return "❌ Could not extract any text from the voice"

    except sr.RequestError as e:
        return f"❌ Could not request results; {e}"
    except sr.UnknownValueError:
        return "❌ Could not understand the audio"
    except Exception as e:
        return f"❌ An error occurred: {e}"
    finally:
        if os.path.exists(wav_file):
            os.remove(wav_file)
