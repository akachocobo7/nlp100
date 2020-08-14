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
        flag = False
        for word in sentence:
            if word["surface"] == "猫":
                flag = True
        
        if not flag:
            continue
        
        for word in sentence:
            if word["surface"] == "猫":
                continue
            if word["surface"] not in mp:
                mp[word["surface"]] = 1
            else:
                mp[word["surface"]] += 1
    
    cnt = sorted(mp.items(), key=lambda x: x[1], reverse=True)
    
    size = 10
    left = [i for i in range(1, size + 1)]
    height = [cnt[i][1] for i in range(size)]
    label = [cnt[i][0] for i in range(size)]
    plt.bar(left, height, tick_label=label, align="center")
    plt.show()