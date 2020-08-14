import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Ricty Diminished"

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
    mp = {}
    for sentence in res:
        for word in sentence:
            if word["surface"] == "":
                continue
            if word["base"] + "_" + word["pos"] + "_" + word["pos1"] not in mp:
                mp[word["base"] + "_" + word["pos"] + "_" + word["pos1"]] = 1
            else:
                mp[word["base"] + "_" + word["pos"] + "_" + word["pos1"]] += 1
    
    cnt = sorted(mp.items(), key=lambda x: x[1])
    print(cnt)
    cnt = [x[1] for x in cnt]
    plt.hist(cnt, bins=100)
    plt.show()