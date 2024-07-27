import pandas as pd
from io import StringIO


file_path_menu_page = 'C:\\Users\Anthony\\Documents\\UIUC\\CS 513\\CS513_Project_Summer24\\MenuPage_Cleaned.csv'

file_path_menu = 'C:\\Users\Anthony\\Documents\\UIUC\\CS 513\\CS513_Project_Summer24\\Menu.csv'
# Load data into DataFrame
df_menu_page = pd.read_csv(file_path_menu_page)

df_menu = pd.read_csv(file_path_menu)

# Retrieve columns (replace 'column_name' with actual column names)
col1 = df_menu_page['menu_id']
col2 = df_menu['id']

# Find values in col1 that are not in col2
not_in_col2 = col2.isin(col1).all()

print(not_in_col2)