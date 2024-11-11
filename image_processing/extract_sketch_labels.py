import easyocr
import os
import re

reader = easyocr.Reader(['en', 'sw'])  # 'en' == English; 'sw' == 'Swahili'
def run_ocr(reader, filename):
    reader_results = reader.readtext(base_dir + "/" + filename)
    
    labels = []
    for (bbox, text, confidence) in reader_results:
        label = {"text": text, "confidence": confidence}
        print(f"File {filename}, Text: {text}, Confidence: {confidence}")
        


def matche_first_page_pattern(s):
    # match strings for first five pages "page_1" to "page_5"
    pattern = r"^page_[1-5]$"
    return bool(re.match(pattern, s))


# base_dir = "../drawings_png"
base_dir = "/Users/arnav/Desktop/picture-perception/drawings_png"
for file in sorted(os.listdir(base_dir)):
    if not file.endswith(".png") or matche_first_page_pattern(file):
        continue

    file_name = base_dir + "/" + file
    run_ocr(reader, file_name)
    
