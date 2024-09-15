from bale import Message, InlineKeyboardButton, InlineKeyboardMarkup
from functools import wraps
from Variable import Variable
from utils import menuCompentents
import os,importlib

async def main(message: Message, *args):
    components = menuCompentents("downloader", Variable.variableList())
    await message.reply("Downloaders", components=components)
    
def DLCommand(name: str, display_name: str, row: int, disabled=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result
        if not disabled: 
            if not name in [var.name for var in Variable.variableList()]: 
                Variable(name, display_name, "downloader", func, row)
        return wrapper
    return decorator

def loadDownloader(folder_path="./Categories/Downloader/Commands"):
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            file_path = os.path.join(folder_path, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

async def backButton() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🔙 Back To Downloaders 🔙", callback_data="back:downloader"))
    return markup