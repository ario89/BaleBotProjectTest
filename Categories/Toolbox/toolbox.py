from functools import wraps
from bale import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Variable import Variable
import os
import importlib.util
import utils

async def main(message: Message, *args):
    compenents = utils.menuCompentents("toolbox", Variable.variableList())
    await message.reply("⚙️ *Bot ToolBox*\nUse Buttons In Keyboard Below To Navigate...", components=compenents)

async def backButton() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🔙 Back To ToolBox 🔙", callback_data="back:toolbox"))
    return markup
    
def toolboxCommand(name: str, display_name: str, row: int, disabled=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            return result
        if not disabled: Variable(name, display_name, "toolbox", func, row)
        return wrapper
    return decorator

def loadToolbox(folder_path="./Categories/Toolbox/Commands"):
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            file_path = os.path.join(folder_path, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
