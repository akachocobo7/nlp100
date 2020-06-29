import json
import gzip

def get_UK_text():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]

if __name__ == "__main__":
    all_text = get_UK_text()
    text_list = all_text.split()
    for text in text_list:
        if text[0:11] == "[[Category:":
            print(text)