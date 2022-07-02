import pandas as pd
import os

wb_df = pd.read_csv(os.path.join('data', 'API_NY.ADJ.NNTY.PC.CD_DS2_en_csv_v2_4261468.csv'), usecols=('Country Name', '2021'))
so_df = pd.read_csv(os.path.join('data', 'survey_results_public.csv'), usecols=('Country', 'ConvertedCompYearly'))

so_df.dropna(inplace=True)

# print(wb_df.columns)
# print(so_df.columns)
print(so_df.sample(30))
print(wb_df.sample(10))