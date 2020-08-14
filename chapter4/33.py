def nekoTextSurfaceBasePosPos1List():
    filename = "./neko.txt.mecab"
    
    sentences = None
    with open(filename, mode="r", encoding="utf-8") as f:
        sentences = f.read().split("EOS\n")
        
    result = []
    for sentence in sentences:
        res = []
        for line in sentence.split("\n"):
            if line == "":
                continue
            (surface, attr) = line.split("\t")
            attr = attr.split(",")
            mp = {
                "surface": surface,
                "base": attr[6],
                "pos": attr[0],
                "pos1": attr[1]
            }
            res.append(mp)
        result.append(res)
    
    return result

if __name__ == "__main__":
    res = nekoTextSurfaceBasePosPos1List()
    for words in res:
        for i in range(len(words) - 2):
            if words[i]["pos"] == "名詞" and words[i + 1]["surface"] == "の" and words[i + 2]["pos"] == "名詞":
                print(words[i]["surface"] + words[i + 1]["surface"] + words[i + 2]["surface"])
            