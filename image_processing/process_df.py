import pandas as pd

df = pd.read_csv("./image_labels.csv")
replace_dict = {
    "Aırplane": "Airplane",
    "Ca:": "Car",
    "Ecycle": "Bicycle",
    'Brrd': "Bird",
    "Chalr": 'Chair',
    'Airplang': 'Airplane',
    'Habbi': 'Rabbit',
    'Blrd': 'Bird',
    'Bıra': 'Bird',
    'Houso': 'House',
    'Rabblt': 'Rabbit',
    'Bicicle': 'Bicycle',
    'Iree': 'Tree',
    'Arpiane': 'Airplane',
    'Blcycle': 'Bicycle',
    'Alrplane': 'Airplane', 
    'Bírd': 'Bird',
    'Aírplane': 'Airplane',
    'Rabbıt': 'Rabbit', 
    'Bira': 'Bird',
    'Chaır': 'Chair',
    'Bırd': 'Bird',
    'Walch': 'Watch', 
    'Arplane': 'Airplane',
    'folane': 'Airplane',
    'Trco': 'Tree', 
    'Birc': 'Bird',
    'Arplang': 'Airplane', 
    'Aabbit': 'Rabbit',
    'Kikombe': 'Cup',
    'Kıkombe': 'Cup',
    'Uird': 'Bird',
    'Kivombe': 'Cup',
    'Waich': 'Watch',
    'Vlatch': 'Watch',
    'Hou :1': 'House',
    'Paka': 'Cat',
    'Puka': 'Cat',
    'Mti': 'Tree',
    'Gari': 'Car',
    'Baiskeli': 'Bicycle',
    'Paka': 'Cat',
    'Gari': 'Car',
    'Kikombe': 'Cup',
    'Nyumba': 'House',
    'Saa': 'Watch',
    'Mti': 'Tree',
    'Kiti': 'Chair',
    'Ndege ya kubeba watu': 'Airplane',
    'Sungura': 'Rabbit',
    'Kofia': 'Hat',
    'Ndege mnyama': 'Bird'
}


def is_valid_english_label(r):
    valid_labels = ['Cup','Hat','Rabbit','Bird','Bicycle','Car','Cat','Airplane','Chair','Tree','Watch','House']
    return r in valid_labels

def replace_swahili_to_english(r):
    translation_dict = {
        'Bicycle': 'Baiskeli',
        'Cat': 'Paka',
        'Car': 'Gari',
        'Cup': 'Kikombe',
        'House': 'Nyumba',
        'Watch': 'Saa',
        'Tree': 'Mti',
        'Chair': 'Kiti',
        'Airplane': 'Ndege ya kubeba watu',
        'Rabbit': 'Sungura',
        'Hat': 'Kofia',
        'Bird': 'Ndege mnyama'
    }

    if is_valid_english_label(r['english']):
        r['swahili'] = translation_dict[r['english']]
        r['swahili_ocr_confidence'] = 1.1

    return r

def filter_labels(r):
    if not is_valid_english_label(r['english']):
        if is_valid_english_label(r['swahili']):
            r['english'] = r['swahili']
    return r

def set_replace_conf_to_one(r):
    if r['english'] in replace_dict.keys():
        r['english_ocr_confidence'] = 1.1
    return r

# df = df.apply(set_replace_conf_to_one, axis=1)
df = df.replace(replace_dict)
df = df.apply(filter_labels, axis=1)
df = df.apply(replace_swahili_to_english, axis=1)


print(df[~df['english'].apply(is_valid_english_label)]['english'].unique())

df.to_csv("./processed_image_labels.csv")

