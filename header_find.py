import pandas as pd
import msoffcrypto
from io import BytesIO


import numpy as np
#File Location and Password
path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
path2 = "C:/Users/dhanr/Downloads/File1.xlsx"
file_path = path
password = "1234"

# Decrypt the file
decrypted_file = BytesIO()
with open(file_path, "rb") as file:
    office_file = msoffcrypto.OfficeFile(file)
    office_file.load_key(password=password)
    office_file.decrypt(decrypted_file)


template1 = ["Grandparent Name","Child Account"]

data_frame = pd.read_excel(decrypted_file , engine = 'openpyxl')


def detect_header(df):
    # Heuristic to detect header: Find the first row with non-null values
    for i, row in df.iterrows():
        if row.notnull().all():
            return i
    return None

def detect_footer(df):
    # Heuristic to detect footer: Find the first row from the bottom with non-null values
    for i in range(len(df)-1, -1, -1):
        if df.iloc[i].notnull().all():
            return i
    return None

def extract_actual_data(file_path):
    # Read the entire Excel file
    df = pd.read_excel(file_path, header=None)

    # Detect header and footer
    header_row = detect_header(df)
    footer_row = detect_footer(df)

    if header_row is not None and footer_row is not None:
        # Extract the data between the detected header and footer
        actual_data = pd.read_excel(file_path, skiprows=header_row , skipfooter = footer_row)
        return actual_data
    else:
        return None  # Or raise an error if header/footer can't be detected


data = extract_actual_data(decrypted_file)

if data is not None:
    print(data)
else:
    print("Could not detect header or footer.")
