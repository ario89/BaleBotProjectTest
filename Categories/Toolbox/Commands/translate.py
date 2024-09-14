from bale import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Categories.Toolbox.toolbox import backButton, toolboxCommand
import translators as ts

@toolboxCommand("translate","💫 Translate", 10)
async def translate(message:Message, query:Message = False, lang:str=None, *args):
    if not lang and not query:
        return await message.reply("💬 *Choose Lang:* ", components=inlineComponents())
    
    toLang = lang
    fromLang = "enfa".replace(lang, '')
    
    try:
        result = ts.translate_text(query.content, from_language=fromLang ,to_language=toLang)
    except: 
        await query.reply("❌ Error", components=await backButton())
    await query.reply(f"✅ Translated Text From *{fromLang}* To *{toLang}*:\n *{result}*", components=await backButton())
    
def inlineComponents():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("فارسی به انگلیسی", callback_data="translate:en"))
    markup.add(InlineKeyboardButton("انگلیسی به فارسی", callback_data="translate:fa"))
    
    return markup