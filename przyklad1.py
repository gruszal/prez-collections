from collections import ChainMap

dict1 = {'a': 'AAA1', 'b': 'BBB1'}
dict2 = {'b': 'BBB2', 'c': 'CCC2'}
dict3 = {'c': 'CCC3', 'd': 'DDD3'}

# jak scalić trzy słowniki w jeden NOWY?

new_dict = ChainMap(dict3, dict2, dict1)

print(dict(new_dict))
