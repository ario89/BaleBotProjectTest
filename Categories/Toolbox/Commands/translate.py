from bale import Message
from Categories.Toolbox.toolbox import backButton, toolboxCommand
from utils import inlineComponents
import translators as ts
import requests

@toolboxCommand("translate","💫 Translate", 10)
async def translate(message:Message, query:Message = False, lang:str=None, *args):
    if not lang and not query:
        components = inlineComponents({"انگلیسی به فارسی": "translate:fa", 
                                        "فارسی به انگلیسی": "translate:en"})
        return await message.reply("💬 *Choose Lang:* ", components=components)
    
    msg = await query.reply("💫 Translating...")
    
    toLang = lang
    fromLang = "enfa".replace(lang, '')
    
    try:
        result = ts.translate_text(query.content, from_language=fromLang ,to_language=toLang)
        return await msg.edit(f"✅ Translated Text From *{fromLang}* To *{toLang}*:\n *{result}*", components=await backButton())
    except requests.exceptions.HTTPError:
        try:
            result = ts.translate_text(query.content, from_language=fromLang ,to_language=toLang, translator="google")
            return await msg.edit(f"✅ Translated Text From *{fromLang}* To *{toLang}*:\n *{result}*", components=await backButton())
        except:
            return await msg.edit("❌ Error", components=await backButton())