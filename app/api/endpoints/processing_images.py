from typing import Dict
from .models import DataModel
from core import ia_processor

async def processing_images(data: str) -> Dict:
    data_model = data
    result = await ia_processor.process(data_model)
    return result