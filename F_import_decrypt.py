import pandas as pd
import msoffcrypto
from io import BytesIO
import numpy as np
#File Location and Password
path = "C:/Users/dhanr/Downloads/"
path2 = "C:/Users/dhanr/Downloads/File1.xlsx"
file_name = "Rawdata.xlsx"
file_path = path + file_name
password = "1234"

# Decrypt the file
decrypted_file = BytesIO()
with open(file_path, "rb") as file:
    office_file = msoffcrypto.OfficeFile(file)
    office_file.load_key(password=password)
    office_file.decrypt(decrypted_file)


template1 = ["Grandparent Name","Child Account"]

data_frame = pd.read_excel(decrypted_file , engine = 'openpyxl')

print(data_frame)
