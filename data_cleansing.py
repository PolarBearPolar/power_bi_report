import os, random
import pandas as pd
import numpy as np

# Меняем рабочую директорию
work_dir = r'C:\Users\User\Desktop\Power BI\Projects\Project_1'
os.chdir(work_dir)

# Открываем csv файл
df = pd.read_csv('supermarket_sales.csv')

# Добаляем столбец Unit cost
df['Unit cost'] = np.nan

# Определяем себестоимость продукции по каждому подукту
distinct_products = df.groupby('Product line')['Unit price'].min()
for i in distinct_products.index:
    distinct_products[i] = round(random.uniform(distinct_products[i]*0.80, distinct_products[i]),2)

# Заполняем столбец Unit cost
for i in df.index:
    df.at[i, 'Unit cost'] = distinct_products[df['Product line'][i]] 
    
# Оставляем нужные колонки и сохраняем отредактированный csv файл
df = df[['Invoice ID', 'Date', 'City', 
    'Customer type', 'Gender', 'Product line', 
    'Unit cost','Unit price', 'Quantity']]
df.to_csv('supermarket_sales_edited.csv',index=False)