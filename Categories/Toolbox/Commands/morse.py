from bale import Message
from Categories.Toolbox.toolbox import toolboxCommand, backButton
from utils import inlineComponents

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-'
}

@toolboxCommand("morse", "🗝️ Morse Translator", 9)
async def main(message:Message, query:Message=False, action:str=None, *args):
    if not action and not query:
        components = inlineComponents({"To Morse": "morse:to",
                                            "From Morse": "morse:from"})
        return await message.reply("💬 *Choose Lang:* ", components=components)
    
    if action == "to":
        return await toMorse(query)
    return await fromMorse(query)

async def fromMorse(query:Message, *args):
    if len(query.content) >= 4096 or len(query.content) < 1:
        return await query.reply("❌ Invalid Length", components=await backButton())
    
    msg = await query.reply("🔃 Decoding...")
    back = await backButton()

    result = decrypt(query.content)
    if result == 'invalid':
        return await msg.edit("❌ Invalid Syntax", components=back)
    if not result: return await msg.edit("❌ Error", components=back)
    
    return await msg.edit(f"✒️ Decoded Code: *{result}*", components=back)

async def toMorse(query:Message, *args):
    allowed = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '.', ',', '?', "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '@', ' ', '\n'
    ]
    
    if len(query.content) >= 4096 or len(query.content) < 1:
        return await query.reply("❌ Invalid Length")
    
    msg = await query.reply("🔃 Encoding...")
    
    back = await backButton()
        
    for i in query.content.upper():
        
        if i not in allowed:
            return await msg.edit("❌ Invalid Entry", components=back)
            
    result = encrypt(query.content.upper())
    if not result: return await msg.edit("❌ Error", components=back)
    return await msg.edit(f"✒️ Your Morse Code: *{result}*", components=back)

def decrypt(message):
    message = message.strip()
    decipher = ''
    words = message.split(' / ')

    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in MORSE_CODE_DICT.values():
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)]
            else:
                return 'invalid'
        decipher += ' '

    return decipher.strip()

def encrypt(message):
    cipher = ''
    try:
        for letter in message:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:

                cipher += ' / '
        return cipher
    except:
        return False