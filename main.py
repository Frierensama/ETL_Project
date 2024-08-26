from functions_seperate import *

path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
password ="1234"

decrypted_file = decrypt_func(path,password)

data_frame = pd.read_excel(decrypted_file , engine = 'openpyxl')

print(data_frame)