from PIL import Image
import PyPDF2
from pathlib import Path

def remove_image_metadata(image_path, output_path):
    with Image.open(image_path) as image:
        image_without_metadata = image.copy()
        image_without_metadata.save(output_path)
    print(f"Metadata removed: {output_path}")

def remove_pdf_metadata(pdf_path, output_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)
        
        writer.add_metadata({})  # Remove metadata correctly
        
        with open(output_path, "wb") as output_pdf:
            writer.write(output_pdf)
    print(f"Metadata removed: {output_path}")

def process_file(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)
    
    if not input_path.exists():
        print("Error: File does not exist.")
        return
    
    image_extensions = {".jpg", ".jpeg", ".png", ".tiff", ".bmp"}
    if input_path.suffix.lower() in image_extensions:
        remove_image_metadata(input_path, output_path)
    elif input_path.suffix.lower() == ".pdf":
        remove_pdf_metadata(input_path, output_path)
    else:
        print("Error: Unsupported file format.")
        return

# Example usage: process_file("input.jpg", "output.jpg")
