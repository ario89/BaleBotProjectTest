from bale import MenuKeyboardMarkup, MenuKeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def menuCompentents(category:str, varList) -> MenuKeyboardMarkup:
    print([var.name for var in varList])
    markup = MenuKeyboardMarkup()
    
    for var in varList:
        if(var.category == category):
            markup.add(MenuKeyboardButton(var.displayName), row=var.row)
        
    return markup

def inlineComponents(buttons:dict[str, str]) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for text, callback_data in buttons.items():
        markup.add(InlineKeyboardButton(text, callback_data=callback_data))
    
    return markup