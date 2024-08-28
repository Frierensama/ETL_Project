import pandas as pd
import msoffcrypto
from io import BytesIO
import numpy as np

######################      FOR DECRYPTION          #########################

# Decrypt the file
def decrypt_func(filepath , password):
    decrypted_file = BytesIO()
    with open(filepath, "rb") as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=password)
        office_file.decrypt(decrypted_file)
    return decrypted_file

##################### FOR HEADER AND FOOTER EXTRACTION #############################

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

###################           Sorting by Columns           ######################

def sort_by_col(dataframe , col_name , type):
    return dataframe.sort_values(by=[col_name],ascending=type)

##############         Filtering by query                  ######################

def filter_by_query(dataframe , query):
    return dataframe.query(query)

################           Group Records - Groupby          ####################
def group_rows(dataframe ,colname_to_groupby ,col_groupby_names , col_groupby_funcs ):
    res = {}
    for i in range(len(col_groupby_names)):
        res[col_groupby_names[i]]=col_groupby_funcs[i]

    col_names = list(dataframe.columns)
    for x in col_names:
        if(x not in res.keys()):
            res[x]="first"
    dataframe = dataframe.groupby(colname_to_groupby).agg(res)
    return dataframe

