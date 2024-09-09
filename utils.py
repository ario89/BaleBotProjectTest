import csv
import re
from bale import MenuKeyboardMarkup, MenuKeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def menuCompentents(category:str, varList):
    markup = MenuKeyboardMarkup()
    
    for var in varList:
        if(var.category == category):
            markup.add(MenuKeyboardButton(var.displayName), row=var.row)
        
    return markup


    
