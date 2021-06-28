from collections import namedtuple

Place = namedtuple('Place', ['city', 'country'])

gdansk = Place('Gdańsk', 'Poland')

print(gdansk)
print(gdansk.country)