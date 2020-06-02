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

s = "I am an NLPer"
word_n_gram, char_n_gram = make_n_gram(s, 2)
print(word_n_gram, char_n_gram)