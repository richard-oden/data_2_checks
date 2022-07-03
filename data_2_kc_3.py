import enum
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns

# I'm using an enum to store column names.
class ColumnName(enum.Enum):
    COUNTRY = 'Country'
    DEVELOPER_INCOME = 'Average Developer Income in USD ($)'
    OVERALL_INCOME = 'Income per Capita in USD ($)'

# Import data from income per capita report from World Bank:
# https://data.worldbank.org/indicator/NY.ADJ.NNTY.PC.CD
wb_df = pd.read_csv(os.path.join('data', 'API_NY.ADJ.NNTY.PC.CD_DS2_en_csv_v2_4261468.csv'), usecols=('Country Name', '2020'))

# Rename columns:
wb_df.rename(columns={
    'Country Name': ColumnName.COUNTRY.value,
    '2020': ColumnName.OVERALL_INCOME.value
}, inplace=True)

# Drop rows with null values:
wb_df.dropna(inplace=True)

# Import data from 2021 Stack Overflow developer survey:
# https://insights.stackoverflow.com/survey
so_df = pd.read_csv(os.path.join('data', 'survey_results_public.csv'), usecols=('Country', 'ConvertedComp'))

# Rename columns:
so_df.rename(columns={
    'ConvertedComp': ColumnName.DEVELOPER_INCOME.value
}, inplace=True)

# Drop rows with null values:
so_df.dropna(inplace=True)

# Group by country and get average income:
so_df = so_df.groupby(ColumnName.COUNTRY.value, as_index=False)[ColumnName.DEVELOPER_INCOME.value].mean()

# Merge dataframes:
merged_df = wb_df.merge(so_df, on=ColumnName.COUNTRY.value)

# Sort by developer income:
merged_df.sort_values(by=ColumnName.DEVELOPER_INCOME.value, inplace=True)

# Melt dataframe:
melted_df = merged_df.melt(id_vars=ColumnName.COUNTRY.value, value_name='USD ($)', var_name='Income')

# Create and display grouped bar chart:
sns.set_style('darkgrid')
sns.barplot(x=ColumnName.COUNTRY.value, y='USD ($)', hue='Income', data=melted_df,)
plt.xticks(rotation=90)
plt.show()