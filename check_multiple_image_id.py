import pandas as pd
from io import StringIO


file_path = 'C:\\Users\Anthony\\Documents\\UIUC\\CS 513\\CS513_Project_Summer24\\MenuPage_Cleaned.csv'
# Load data into DataFrame
df = pd.read_csv(file_path)

# Group by 'image_id', 'menu_id', and 'page_number' and get the count of occurrences
grouped = df.groupby(['image_id', 'menu_id', 'page_number']).size().reset_index(name='count')

# Filter to get rows where the count is greater than 1
filtered = grouped[grouped['count'] > 1]

print("Groups where image_id, menu_id, and page_number are the same and occur more than once:")
print(filtered)