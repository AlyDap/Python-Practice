# pip list => untuk melihat list
# pip install pandas => menginstall pandas
import pandas as pd

# data=pd.read_csv('machine.csv')
data=pd.read_csv('baru.csv')
print(data)
print(f'Dimenasi data nya {data.shape}')