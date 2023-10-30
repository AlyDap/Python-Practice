# pip list => untuk melihat list
# pip install openpyxl => untuk membaca file excel
import pandas as pd

data =pd.read_excel('baru.xlsx',sheet_name='Sheet1')
print(data)