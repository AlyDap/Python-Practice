
import pandas as pd

# Query Pandas
# Seleksi Data / Conditional Selection

data = pd.DataFrame(
    data={
        'Menu': ['Nasi Goreng', 'Nasi Megono', 'Tempe Goreng'],
        'Harga': [14000, 5000, 2500]
    })
print(data, '\n')

print(f'{data["Menu"]=="Tempe Goreng"}', '\n')
print(data.loc[data['Menu'] == 'Tempe Goreng'].head(), '\n')
print(data.loc[data['Menu'] != 'Tempe Goreng'].head(), '\n')
print(data.loc[data['Harga'] <= 5000].head(), '\n')


# Method isin
print('Method isin \n')
data_mhs = pd.read_excel('./data-mahasiswa.xlsx', sheet_name='data_mhs')
print(data_mhs, '\n')

print(data_mhs.loc[data_mhs['Progdi'].isin(['SI', 'KA'])], '\n')

# Method isna dan notna
# isna = Is not Available, notna = not Available
print('Method isna dan notna \n')
print(data_mhs.loc[data_mhs['IPK'].isna()], '\n')
print(data_mhs.loc[data_mhs['IPK'].notna()], '\n')
