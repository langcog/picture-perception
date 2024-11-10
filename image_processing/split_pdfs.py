from pdf2image import convert_from_path
import os

def split_pdfs(pdf_dir, img_dir):
    """Splits pdf files into separate png image files while making sure all images are horizontal"""

    for file in os.listdir(pdf_dir):
        if not file.endswith('.pdf'):
            continue
        if "Rescans" in file or "don_t" in file:
            continue
        
        print(file)
        pid = file.replace(".pdf", "")
        images = convert_from_path(os.path.join(pdf_dir, file))
        
        for i, image in enumerate(images):
            if image.height > image.width:
                image = image.rotate(90, expand=True)
            
            file_name = os.path.join(img_dir, f"{pid}_page_{i+1}.png")
            image.save(file_name, "PNG")
            print(f"Saved page {i+1} as {file_name}")


if __name__ == "__main__":
    pdf_dir = "../Kisumu 2024 Drawings and Consents"
    img_dir = "../drawings_png"
    split_pdfs(pdf_dir, img_dir)