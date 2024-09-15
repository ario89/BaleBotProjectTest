from functools import wraps
from bale import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Variable import Variable
import os
import importlib.util
import utils

async def main(message: Message, *args):
    compenents = utils.menuCompentents("📨 Extractors Category\nSelect From Menu Below...", Variable.variableList())
    await message.reply("Extractors", components=compenents)

async def backButton() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🔙 Back To Extractors 🔙", callback_data="back:extract"))
    return markup
    
def extractorCommand(name: str, display_name: str, row: int, disabled=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result
        if not disabled: 
            if not name in [var.name for var in Variable.variableList()]: 
                Variable(name, display_name, "extract", func, row)
        return wrapper
    return decorator

def loadExtractors(folder_path="./Categories/Extract/Commands"):
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            file_path = os.path.join(folder_path, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
