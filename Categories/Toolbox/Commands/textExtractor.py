from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import aiohttp

@toolboxCommand("textExtractor", "💬 Extract Text From Image",10, True)
async def textExtractor(message: Message, query: Message = None, *args):
    if not query:
        await message.reply("Send Image: ")
        return "query"
    if not query.attachment:
        return await query.reply("❌ No Attachment Found!")
    msg = await query.reply("🔃 Please Wait...")
    try:
        with open("Assets/temp/temp.png", 'wb') as f:
            await query.attachment.save_to_memory(f)
        with open("Assets/temp/temp.png", 'rb') as image_file:
            image_data = image_file.read()
        headers = {'apikey': 'Js4ifsq2ZbtuLD1ZQzHrRHXWq9LgnceG'}
        async with aiohttp.ClientSession() as session:
            files = {'image': image_data}
            async with session.post('https://api.apilayer.com/image_to_text/upload', headers=headers, data=files) as r:
                if r.status == 200:
                    response_data = await r.json()
                    data = response_data.get('text', '')
                    return await msg.edit(data, components=await backButton())
                return await msg.edit(f"Failed to extract text from image. Status code: {r.status}", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error extracting text", components=await backButton())
