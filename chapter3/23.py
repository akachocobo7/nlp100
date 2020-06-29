import json
import gzip
import re

def get_UK_text():
    with gzip.open("jawiki-country.json.gz") as f:
        for line in f:
            data = json.loads(line)
            if data["title"] == "イギリス":
                return data["text"]

if __name__ == "__main__":
    pattern = re.compile("^(={2,})\s*(.+?)\s*\\1.*$", re.MULTILINE)
    result = pattern.findall(get_UK_text())
    
    for line in result:
        level = len(line[0]) - 1
        print("{indent}{sect}({level})".format(indent="\t" * (level - 1), sect=line[1], level=level))