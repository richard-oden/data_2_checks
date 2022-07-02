import enum
import os
import pandas as pd

class ColumnName(enum.Enum):
    COUNTRY = 'Country',
    DEVELOPER_INCOME = 'Average Developer Income in USD ($)',
    OVERALL_INCOME = 'Income per Capita in USD ($)'

# Import data from income per capita report from World Bank:
# https://data.worldbank.org/indicator/NY.ADJ.NNTY.PC.CD
wb_df = pd.read_csv(os.path.join('data', 'API_NY.ADJ.NNTY.PC.CD_DS2_en_csv_v2_4261468.csv'), usecols=('Country Name', '2021'))

wb_df.rename({
    'Country Name': ColumnName.COUNTRY.value,
    '2021': ColumnName.OVERALL_INCOME.value
})

wb_df.dropna(inplace=True)

# Import data from 2021 Stack Overflow developer survey:
# https://insights.stackoverflow.com/survey
so_df = pd.read_csv(os.path.join('data', 'survey_results_public.csv'), usecols=('Country', 'ConvertedCompYearly'))

wb_df.rename({
    'ConvertedCompYearly': ColumnName.DEVELOPER_INCOME.value
})

so_df.dropna(inplace=True)