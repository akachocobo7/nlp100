import re

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = []
for x in map(len, re.split("[, .]", s)):
    if x > 0:
        ans.append(x)

print(ans)