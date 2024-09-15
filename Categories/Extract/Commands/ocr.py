from bale import Message
from Categories.Extract.extractors import extractorCommand, backButton
from utils import inlineComponents
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
@extractorCommand("ocr", "💬 Extract Text From Image", 1)
async def ocr(message:Message, query:Message=False, lang:str=False, *args):
    if not query and not lang:
        components = inlineComponents({"Persian": "ocr:fas", "English": "ocr:eng"})
        return await message.reply("Select Lang: ", components=components)
        
    if not query.attachment:
        return await query.reply("❌ No Attachment Found!")
    
    msg = await query.reply("🔃 Please Wait...")
    
    try:
        with open("Assets/temp/temp.png", 'wb') as f:
            await query.attachment.save_to_memory(f)

        img = Image.open("Assets/temp/temp.png")
        extracted_text = pytesseract.image_to_string(img, lang=lang)

        if extracted_text.strip():
            return await msg.edit(f"🖼️ Extracted Text: {extracted_text}", components=await backButton())
        else:
            return await msg.edit("❌ Could not extract any text from the image", components=await backButton())

    except Exception as e:
        print(f"Error: {e}")
        return await msg.edit("❌ Error extracting text", components=await backButton())