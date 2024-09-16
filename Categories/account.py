from bale import Message
from database import Database

db = Database("Assets/data.db")

async def main(message:Message, *args):
    data = db.getTableData("userData", f"userID='{message.author.id}'")
    await message.reply(f"👤 Account For User *{message.author.first_name}*:\n🪙 Coins: {data[0][2]}")