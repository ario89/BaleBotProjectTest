from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import string
import secrets

toolboxCommand("passwordGenerator", "🔒 Generate Random Password", 2)
async def generatePassword(message: Message, query: Message = False, *args):
    if not query:
        await message.reply("Enter Length: ")
        return "query"
    msg = await query.reply("🔃 Please Wait...")
    try:
        if not query.content.isnumeric():
            return await msg.edit("❌ Invalid Entry", components=await backButton())
        length = int(query.content)
        if length > 256 or length < 1:
            return await msg.edit("❌ Invalid Length", components=await backButton())
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return await msg.edit(f"🔑 Your Password: *{password}*", components=await backButton())
    except Exception:
        return await msg.edit("❌ Error!", components=await backButton())