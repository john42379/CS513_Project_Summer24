import pandas as pd
from io import StringIO


file_path = 'C:\\Users\Anthony\\Documents\\UIUC\\CS 513\\CS513_Project_Summer24\\MenuPage_Cleaned.csv'
# Load data into DataFrame
df = pd.read_csv(file_path)

# Group by uuid and menu_id and collect ids
grouped = df.groupby(['uuid', 'menu_id', 'page_number'])['id'].apply(list).reset_index()

# Check for inconsistencies within the same menu_id and uuid pairs
inconsistent_entries = []

# Iterate over each group to find inconsistencies
for _, row in grouped.iterrows():
    uuid = row['uuid']
    menu_id = row['menu_id']
    ids = row['id']
    page_number = row['page_number']
    if len(set(ids)) > 1:  # If there are multiple unique ids for the same uuid and menu_id
        inconsistent_entries.append((uuid, menu_id, page_number, ids))

if not inconsistent_entries:
    print("No IC violations found: Each UUID and Menu_ID pair is consistent.")
else:
    print("Possible IC violations found: Some UUID and Menu_ID pairs have inconsistent IDs:")
    for entry in inconsistent_entries:
        print(f"UUID: {entry[0]}, Menu ID: {entry[1]}, PageNumber: {entry[2]} - IDs: {entry[3]}")