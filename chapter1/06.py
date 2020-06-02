def make_n_gram(sentence, n):
    word_list = sentence.split()
    
    word_n_gram = []
    for i in range(len(word_list) - n + 1):
        word_n_gram.append("")
        for j in range(n):
            word_n_gram[i] += word_list[i + j]
    
    char_list = "".join(sentence.split())
    
    char_n_gram = []
    for i in range(len(char_list) - n + 1):
        char_n_gram.append("")
        for j in range(n):
            char_n_gram[i] += char_list[i + j]
    
    return (word_n_gram, char_n_gram)

s1 = "paraparaparadise"
s2 = "paragraph"

tmp, x = make_n_gram(s1, 2)
tmp, y = make_n_gram(s2, 2)

X = {t for t in x}
Y = {t for t in y}
print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)