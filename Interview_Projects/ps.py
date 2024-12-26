'''

data_sales = {
'OrderID': [1, 2, 3, 4, 5],
'ProductID': [101, 102, 101, 103, 102],
'Quantity': [2, 3, 1, 5, 4],
'Price': [20, 30, 20, 40, 30]
}
 
data_products = {
'ProductID': [101, 102, 103],
'ProductName': ['Widget', 'Gadget', 'Doodad'],
'Category': ['A', 'A', 'B']
}
 
 
Join the DataFrames on the ProductID column to combine sales data with product details

Calculate the total sales amount for each product.
'''

import pandas as pd

data_sales = {
'OrderID': [1, 2, 3, 4, 5],
'ProductID': [101, 102, 101, 103, 102],
'Quantity': [2, 3, 1, 5, 4],
'Price': [20, 30, 20, 40, 30]
}

data_products = {
'ProductID': [101, 102, 103],
'ProductName': ['Widget', 'Gadget', 'Doodad'],
'Category': ['A', 'A', 'B']
}

data_sales_df = pd.DataFrame(data_sales)
data_products_df = pd.DataFrame(data_products)

# new_df = data_sales_df.join(data_products_df, on=['ProductID'], how='left', lsuffix='_r')

# print(new_df)


new_df = data_products_df.merge(data_sales_df, on='ProductID')
print(new_df)

new_df['Total_sales'] = new_df['Quantity']* new_df['Price']
# print(new_df)
new_df1 = new_df.groupby('ProductID', as_index=False)
print(new_df1)