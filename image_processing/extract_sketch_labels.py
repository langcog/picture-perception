import os
import re
import pandas as pd
import easyocr

reader = easyocr.Reader(['en', 'sw'])  # 'en' == English; 'sw' == 'Swahili'
def run_ocr(reader, img_dir, file):
    file_path = os.path.join(img_dir, file)
    reader_results = reader.readtext(file_path)
    labels = {}
    for i, (bbox, text, confidence) in enumerate(reader_results):
        if i == 0:
            labels["english"] = text
            labels["english_ocr_confidence"] = confidence
        else:
            labels["swahili"] = text
            labels["swahili_ocr_confidence"] = confidence

    return labels

def match_first_n_page_pattern(s):
    """Match any string that ends with '-001' to '-004'."""

    pattern = r"-00[1-4]\.png$"
    return bool(re.search(pattern, s))

def extract_labels(base_dir):
    label_df = []
    for file in sorted(os.listdir(base_dir)):
        if not file.endswith(".png"):
            continue
        
        if match_first_n_page_pattern(file):
            labels = {"english": None, "english_ocr_confidence": None, "swahili": None, "swahili_ocr_confidence": None}
        else:
            labels = run_ocr(reader, base_dir, file)

        pid = file.split("-")[0]
        labels['file'] = file
        labels['participant_id'] = pid
        print(labels)
        label_df.append(labels)
    
    pd.DataFrame(label_df).to_csv("./image_labels.csv")
        
if __name__ == "__main__":
    base_dir = "../drawing_images"
    extract_labels(base_dir)