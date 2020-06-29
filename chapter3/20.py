import json
import gzip

def get_UK_text():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]

if __name__ == "__main__":
    print(get_UK_text())