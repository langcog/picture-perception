from pdf2image import convert_from_path
from PIL import Image
import os
import subprocess

## note: using defult python pdf2image lib doesn't work correctly since it keeps the extra white space within the pdf
## while the CLI pdf2image acutally extracts the embedded image
def split_pdfs(pdf_dir, img_dir):
    """Splits pdf files into separate png image files while making sure all images are horizontal"""

    for file in sorted(os.listdir(pdf_dir)):
        if not file.endswith('.pdf'):
            continue
        if file.find("don_t") != -1:
            continue

        print(pdf_dir + "/" + file)
        pid = file.replace(".pdf", "")

        file_path = os.path.join(pdf_dir, file)
        subprocess.run(["pdfimages", "-png", file_path, img_dir + "/" + pid])


def rotate_vertical_pdfs(img_dir):
    """Rotate vertical images to horizontal images"""
    for file in sorted(os.listdir(img_dir)):
        if not file.endswith('.png'):
            continue
        
        file_path = os.path.join(img_dir, file)
        image = Image.open(file_path) 
  
        if image.height > image.width:
            print(file_path)
            image = image.rotate(90, expand=True)
            image.save(file_path, "PNG")

if __name__ == "__main__":
    pdf_dir = "../Kisumu 2024 Drawings and Consents"
    img_dir = "../drawing_images"
    # split_pdfs(pdf_dir, img_dir)
    rotate_vertical_pdfs(img_dir)