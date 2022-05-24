import pandas as pd
import requests
import re

#1. Find and print TWO descriptive statistics about your data.

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

# Get details for all evocation cantrips:
evocation_cantrips_json = requests.get('https://www.dnd5eapi.co/api/spells?school=evocation&level=0').json()
cantrip_details = []
for cantrip in evocation_cantrips_json['results']:
    cantrip_details.append(requests.get(f'https://www.dnd5eapi.co/api/spells/{cantrip["index"]}').json())
cantrips_df = pd.DataFrame(data=cantrip_details, columns=cantrip_details[0].keys())

# Get average damage of each cantrip:
def get_average_damage(amount, num_sides, modifier):
    amount = amount or 0
    num_sides = num_sides or 0
    modifier = modifier or 0

    return (((int(num_sides) + 1) / 2) * int(amount)) + int(modifier)

dice_pattern = r'(\d+)?d(\d+)([\+\-]\d+)?'
average_damage = []

for cd in cantrip_details:
    damage = cd.get('damage')
    if damage is None:
        average_damage.append(0)
        continue

    damage_at_character_level = damage.get('damage_at_character_level')
    if damage_at_character_level is None:
        average_damage.append(0)
        continue

    first_level_damage = damage_at_character_level.get('1')
    if first_level_damage is None:
        average_damage.append(0)
        continue
    
    damage_match = re.search(dice_pattern, first_level_damage)
    average_damage.append(get_average_damage(damage_match.group(1), damage_match.group(2), damage_match.group(3)))

cantrips_df['average_damage'] = average_damage

# Get only the values we care about:
cantrips_summary_df = cantrips_df.filter(['name', 'average_damage', 'range'])

# Sort by highest average damage:
cantrips_summary_df.sort_values(by='average_damage', ascending=False, inplace=True)

# 2. Write a query in Pandas to select a particular set of your data.
print(cantrips_summary_df.query('average_damage == 0'))

# 3. Select and print the SECOND AND THIRD columns of your data frame.
print(cantrips_summary_df.iloc[:, 1:3])

# 4. Select and print the FIRST 4 rows of you data frame.
print(cantrips_summary_df.head(4))