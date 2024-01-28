import pandas as pd
df = pd.read_excel("sampledata.xlsx", sheet_name="Sheet1")
print(df.head())
print(df.column)