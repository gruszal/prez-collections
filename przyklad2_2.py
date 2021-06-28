from collections import defaultdict

names = ['Ambroży', 'Adela', 'Bożena', 'Barnaba', 'Celina']

result = defaultdict(list)

for name in names:
    result[name[0]].append(name)

print(dict(result))
