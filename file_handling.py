from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import io

app = FastAPI()
@app.post("/upload-image")
async def upolad_Image(file: UploadFile = File(...)):
    image_content = await file.read()
    img = Image.open(io.BytesIO(image_content))
    grayscale_image = img.convert("L")
    temp_file = f"temp_{file.filename}"
    grayscale_image.save(temp_file) 
    response = FileResponse(path=temp_file, filename=f"grayscale_{file.filename}", media_type='image/png') 
    return response 
