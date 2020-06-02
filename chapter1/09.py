import random

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word_list = s.split()
for i in range(len(word_list)):
    word = word_list[i]
    if len(word) <= 4:
        continue
    
    first = word[0]
    last = word[-1]
    mid = word[1:-1]
    mid = "".join(random.sample(mid, len(mid)))
    
    word_list[i] = first + mid + last

print(word_list)