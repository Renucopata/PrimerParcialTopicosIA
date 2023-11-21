from fastapi import FastAPI, File, UploadFile
from api.endpoints import processing_images
from utils.save_image_temporal import save_in_disk

app = FastAPI()

@app.post("/processing_images")
async def call_processing_images(image: UploadFile = File(...)):
    image_bytes  = await image.read()
    image_path = save_in_disk(image_bytes)
    result = await processing_images.processing_images(image_path)
    return result

@app.get("/")
async def root():
    return {"message": "Primer Parcial Rene Rengel"}