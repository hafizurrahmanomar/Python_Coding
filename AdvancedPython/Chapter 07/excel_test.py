# pip install openpyxl

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'].value = "Faisal Zamir"
sheet['B1'].value = "Faisal JafriCode"

a1 = sheet['A1'].value
print(a1)
wb.save("jafri.xlsx")