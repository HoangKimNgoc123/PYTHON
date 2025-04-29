import pandas as pd
import requests
from io import BytesIO

url = "https://docs.google.com/spreadsheets/d/1BnOzoEG0s6c8MpiUANZ0_pawXNHqdkid/export?format=xlsx"
response = requests.get(url)
df = pd.read_excel(BytesIO(response.content))

cols_to_convert = ['vpv2', 'pDisCharge', 'prec', 'vBus1', 'vBus2']
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

filtered_df = df[
    (df['vpv2'] % 2 == 0) &
    (df['pDisCharge'] % 2 == 0) &
    (df['prec'] % 2 == 1)
].copy()

filtered_df['Sum_vBUS'] = filtered_df['vBus1'] + filtered_df['vBus2']
filtered_df.to_csv("Bai2_Data_new.csv", index=False, encoding='utf-8-sig')