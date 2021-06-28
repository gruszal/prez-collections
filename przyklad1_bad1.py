from collections import ChainMap

dict1 = {'a': 'AAA', 'b': 'BBB'}
dict2 = {'b': 'BBB', 'c': 'CCC'}
dict3 = {'c': 'CCC', 'd': 'DDD'}

# jak scalić trzy słowniki w jeden NOWY?

new_dict = dict(**dict3, **dict2, **dict1)

# UWAGA: nie zadziała dla duplikatów kluczy!

