from bale import Message
from Categories.Toolbox.toolbox import backButton

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-'
}

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