from pdf2image import convert_from_path
import os

def split_pdfs(pdf_dir):
    for file in os.listdir(pdf_dir):
        print(file)
        if not file.endswith('.pdf'):
            continue
        if file.find("Rescans") != -1 or file.find("don_t") != -1:
            continue
        
        pid = file.replace(".pdf", "")
        images = convert_from_path(pdf_dir + "/" + file)
        for i, image in enumerate(images):
            image.save(f"../drawings_png/{pid}_page_{i+1}.png", "PNG")
        print(f"Saved page {i+1} as image")

if __name__ == "__main__":
    pdf_dir = "../Kisumu 2024 Drawings and Consents"
    split_pdfs(pdf_dir)