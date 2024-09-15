from bale import Message, InputFile
from Categories.Extract.extractors import backButton, extractorCommand
from moviepy.editor import VideoFileClip
import os

VIDEO_PATH = "Assets/temp/video.mp4"
AUDIO_PATH = "Assets/temp/extracted.mp3"

@extractorCommand("audioextractor", "🎥 Extract Audio From Video", 4)
async def audioExtractor(message: Message, query: Message = False):
    if not query:
        await message.reply("Send Video as *Document*: ")
        return "query"
    
    if query.video:
        return await message.reply("❌ Send Video as Document!")
    
    if not query.document:
        return await message.reply("❌ No Video Found")
    
    msg = await query.reply("🔃 Please Wait...")
        
    try:
        video_file_path = VIDEO_PATH
        with open(video_file_path, 'wb') as f:
            await query.attachment.save_to_memory(f)

        extractAudio(video_file_path, AUDIO_PATH)
        
        with open(AUDIO_PATH, "rb") as f:
            file = InputFile(f, file_name="Export.mp3")
            
            await query.reply_document(file, caption="✅ Done", components=await backButton())
            return await msg.delete()

    except Exception as e:
        print(f"Error: {e}")
        return await msg.edit("❌ Error extracting audio", components=await backButton())

def extractAudio(video_file_path, audio_file_path):
    video = VideoFileClip(video_file_path)
    audio = video.audio
    audio.write_audiofile(audio_file_path)
    audio.close()
    video.close()
