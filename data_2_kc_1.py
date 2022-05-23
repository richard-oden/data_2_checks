import pandas as pd
import requests
import re

# 1. Find and print TWO descriptive statistics about your data.

# Number of spells in each school of magic in D&D 5e.
schools = ['conjuration', 'necromancy', 'evocation', 'abjuration', 'transmutation', 'divination', 'enchantment', 'illusion']
for school in schools:
    spells_json = requests.get(f'https://www.dnd5eapi.co/api/spells?school={school}').json()
    print(f'Number of {school} spells: {len(spells_json["results"])}')

# Number of spells by spell level in D&D 5e.
level = 0
while level < 10:
    spells_json = requests.get(f'https://www.dnd5eapi.co/api/spells?level={level}').json()
    print(f'Number of level {level} spells: {len(spells_json["results"])}')
    level += 1

# 2. Write a query in Pandas to select a particular set of your data.

# Get details for all evocation cantrips:
evocation_cantrips_json = requests.get('https://www.dnd5eapi.co/api/spells?school=evocation&level=0').json()
cantrip_details = []
for cantrip in evocation_cantrips_json['results']:
    cantrip_details.append(requests.get(f'https://www.dnd5eapi.co/api/spells/{cantrip["index"]}').json())

dice_regex = r'(\d+)?d(\d+)([\+\-]\d+)?'

def get_average_damage(amount, num_sides, modifier):
    return (((num_sides + 1) / 2) * amount) + (modifier or 0)