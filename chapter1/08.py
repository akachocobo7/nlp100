def cipher(sentence):
    result = ""
    for i in range(len(sentence)):
        if sentence[i].islower():
            result += chr(219 - ord(sentence[i]))
        else:
            result += sentence[i]
    
    return result

s = "aBcdEf"
print(s)
s = cipher(s)
print(s)
s = cipher(s)
print(s)