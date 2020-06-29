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
    pattern = re.compile("^\{\{基礎情報.*?$(.*?)^\}\}$", re.MULTILINE + re.DOTALL)
    contents = pattern.findall(get_UK_text())
    
    pattern = re.compile("""^\|
                            (.*?)
                            \s*
                            =
                            \s*
                            (.+?)
                            (?:
                                (?=\n\|)    # 改行 + '|' の手前(肯定の先読み)
                                | (?=\n$)   # または、改行 + 終端の手前(肯定の先読み)
                            )
                        """, re.MULTILINE + re.VERBOSE + re.DOTALL)
    results = pattern.findall(contents[0])
    
    pattern = re.compile("\'{2,5}", re.MULTILINE)
    for field, value in results:
        print((field, pattern.sub("", value)))