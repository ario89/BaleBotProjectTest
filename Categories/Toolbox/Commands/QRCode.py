from bale import Message, InputFile
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import requests

@toolboxCommand("qrcode", "📊 QR Code Generator", 1)
async def qr_code(message: Message, query=False, *args):
    if not query:
        await message.reply("Please enter a query.")
        return "query"
    try:
        response = requests.get(f"https://quickchart.io/qr?text={query.content}&size=1024", stream=True)
        response.raise_for_status()
        data = response.content
        return await query.reply_photo(InputFile(data))
    except requests.RequestException as e:
        return await query.reply(f"❌ Error generating QR Code: {e}", components=await backButton())