from bale import Message
from Categories.Toolbox.toolbox import toolboxCommand
from Categories.Toolbox.Commands.Morse import toMorse, fromMorse

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '@': '.--.-'
}

@toolboxCommand("morse", "🗝️ Morse Translator", 9)
async def main(message:Message, query:Message=False,*args):
    if not query:
        await message.reply("✅ Enter Morse To Decode OR Text To Encode: ")
        return "query"
    
    allowed = ['-', '.', ' ', '/']
    for i in query.content:
        if i not in allowed:
            return await toMorse.toMorse(query)
        
    return await fromMorse.fromMorse(query)