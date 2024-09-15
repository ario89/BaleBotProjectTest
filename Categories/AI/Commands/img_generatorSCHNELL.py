from bale import Message, InputFile, InlineKeyboardButton
from Categories.AI.AI import AICommand, backButton
from dotenv import load_dotenv
import os
import requests

load_dotenv()

OUTPUT_PATH = "Assets/temp/generated_imgSCHNELL.png"

@AICommand("imgGenerator-schnell", "🖼️ Image Generator v1", 1)
async def imageGenerator(message:Message, query:Message=False, *args):
    if not query:
        await message.reply("Enter Query: ")
        return "query"
    
    msg = await query.reply("🔃 Generating\n_This Might Take a While..._")
    
    back = await backButton()
    buttons = back.add(InlineKeyboardButton("Reuse Generator", callback_data="ai:img-SCHNELL"))
    try:
        await generateImage(query.content, OUTPUT_PATH)
    
        if os.path.exists(OUTPUT_PATH):
            with open(OUTPUT_PATH, "rb") as f:
                file = InputFile(f, file_name="Generated.png")
        else: raise Exception("File Not Found")
    
    except Exception as e:
        await msg.edit("❌ Error", components=back)
    
    else:     
        await query.reply_photo(file, caption="✅ Generated", components=buttons)
        return await msg.delete()
    
async def generateImage(prompt: str, output_path: str):
    url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
    headers = {
        "Authorization": f"Bearer {os.getenv("HF_TOKEN")}"
    }
    data = {
        "inputs": prompt
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            try:
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(f"Image saved to {output_path}")
            except Exception as e:
                print(f"Failed to save image. Error: {e}")
        else:
            print(f"Failed to generate image. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")