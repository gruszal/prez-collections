from dataclasses import dataclass


@dataclass(frozen=True)
class Place:
    city: str
    country: str


gdansk = Place('Gdańsk', 'Poland')

print(gdansk)
print(gdansk.country)
