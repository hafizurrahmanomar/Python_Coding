import pandas as pd
data = {
    "Name": ['Ali','Jafri','Faisal'],
    "Age": [20,30,40],
    "Course": ["Python","Java","Pandas"],
    "Marks" : [10,20,30]
}

df = pd.DataFrame(data)
print(df)
df.to_json("myjsonfile.json", orient="records")