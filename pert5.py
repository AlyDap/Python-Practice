# pip list => untuk melihat list
# pip install pandas => menginstall pandas
import pandas as pd

data_menu={
'menu':['Sedap','Indomie','Samyang'],
'harga':[5500,6000,10000],
}
print(data_menu)

data=pd.DataFrame(data_menu)
print(data)

# # data ke csv
# data.to_csv('baru.csv',index=False)

# # data ke excel
# data.to_excel('baru.xlsx',index=False)
