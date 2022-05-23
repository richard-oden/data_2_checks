import requests
import pandas as pd

schools = ['conjuration', 'necromancy', 'evocation', 'abjuration', 'transmutation', 'divination', 'enchantment', 'illusion']
for school in schools:
    json_response = requests.get(f'https://www.dnd5eapi.co/api/spells?school={school}').json()
    print(f'Number of {school} spells: {len(json_response["results"])}')