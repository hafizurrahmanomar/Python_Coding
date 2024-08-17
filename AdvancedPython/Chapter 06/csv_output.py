import pandas 

data = {
    "Name": ['Ali','Jafri','Faisal'],
    "Age": [20,30,40],
    "Course": ["Python","Java","Pandas"]
}

df = pandas.DataFrame(data)
df.to_csv("mycsv.csv")
print(df)