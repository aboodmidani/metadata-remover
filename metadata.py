import streamlit as st
from PIL import Image
import PyPDF2
from io import BytesIO

def remove_image_metadata(image_file):
    image = Image.open(image_file)
    output = BytesIO()
    image.save(output, format=image.format)
    return output.getvalue()

def remove_pdf_metadata(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({})
    output = BytesIO()
    writer.write(output)
    return output.getvalue()

st.title("Metadata Stripper")

uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    if file_extension in ["jpg", "jpeg", "png"]:
        processed_file = remove_image_metadata(uploaded_file)
    elif file_extension == "pdf":
        processed_file = remove_pdf_metadata(uploaded_file)
    else:
        st.error("Unsupported file format")
        processed_file = None

    if processed_file:
        st.download_button("Download Cleaned File", processed_file, f"cleaned_{uploaded_file.name}")
