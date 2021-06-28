from collections import ChainMap

dict1 = {'a': 'AAA', 'b': 'BBB'}
dict2 = {'b': 'BBB', 'c': 'CCC'}
dict3 = {'c': 'CCC', 'd': 'DDD'}

# jak scalić trzy słowniki w jeden NOWY?

new_dict = dict()
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print(new_dict)

# działa, ale jest mało elastyczne (co jeśli ilość słowników jest zmienna?)
