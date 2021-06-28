from collections import defaultdict

names = ['Ambroży', 'Adela', 'Bożena', 'Barnaba', 'Celina']

result = {}

for name in names:
    letter = name[0]
    if letter in result:
        result[letter].append(name)
    else:
        result[letter] = [name]

print(result)
