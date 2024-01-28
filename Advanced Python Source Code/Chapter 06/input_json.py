import pandas as pd

with open("sample_data.json", "r") as file:
    data = file.read()
    df = pd.read_json(data)

print(df.head())