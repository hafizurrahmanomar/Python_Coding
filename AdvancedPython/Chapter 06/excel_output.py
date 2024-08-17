import pandas as pd
data = {
    "Name": ['Ali','Jafri','Faisal'],
    "Age": [20,30,40],
    "Course": ["Python","Java","Pandas"],
    "Marks" : [10,20,30]
}

df = pd.DataFrame(data)
writer = pd.ExcelWriter("myexcel.xlsx")
df.to_excel(writer, index=False)
writer._save()