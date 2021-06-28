from collections import defaultdict

lucky = defaultdict(lambda: 13)

lucky['a']
lucky['b'] = lucky['c']

print(dict(lucky))
