import re

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

tmp = re.split("[, .]", s)
word_list = []
for x in tmp:
    if x != "":
        word_list.append(x)

num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
for i in range(len(word_list)):
    word = ""
    if i + 1 in num_list:
        word = word_list[i][0]
    else:
        word = word_list[i][0:2]
        
    dic[word] = i + 1

print(dic)