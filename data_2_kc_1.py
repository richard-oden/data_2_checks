import requests
import pandas as pd

schools = ['conjuration', 'necromancy', 'evocation', 'abjuration', 'transmutation', 'divination', 'enchantment', 'illusion']
for school in schools:
    json_response = requests.get(f'https://www.dnd5eapi.co/api/spells?school={school}').json()
    print(f'Number of {school} spells: {len(json_response["results"])}')

level = 1
while level < 10:
    json_response = requests.get(f'https://www.dnd5eapi.co/api/spells?level={level}').json()
    print(f'Number of level {level} spells: {len(json_response["results"])}')
    level += 1