import easyocr
import os 

reader = easyocr.Reader(['en', 'sw'])  # 'en' == English; 'sw' == 'Swahili'

base_dir = "../drawings_png"
for file in sorted(os.listdir(base_dir)):
    if not file.endswith(".png"):
        continue
    reader_results = reader.readtext(base_dir + "/" + file)

    for (bbox, text, confidence) in reader_results:
        print(f"File {file}, Text: {text}, Confidence: {confidence}")
        
    break
    
    
def run_ocr(reader, filename):
    reader_results = reader.readtext(base_dir + "/" + file)

    for (bbox, text, confidence) in reader_results:
        print(f"File {file}, Text: {text}, Confidence: {confidence}")