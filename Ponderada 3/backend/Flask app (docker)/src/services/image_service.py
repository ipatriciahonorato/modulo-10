from PIL import Image
from rembg import remove
import io

from logs.logger import setup_logger
logger = setup_logger('image_service')

def remove_background(image):
    return remove(image)

def process_image_file(file_stream):
    try:
        logger.info("Processing image")
        image = Image.open(file_stream)
        processed_image = remove_background(image)

        img_io = io.BytesIO()
        processed_image.save(img_io, 'PNG')
        img_io.seek(0)

        return img_io
    except Exception as e:
        logger.error(f"Image processing failed: {str(e)}")
        raise ValueError(f"Image processing failed: {str(e)}")
