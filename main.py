from functions_seperate import *

path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
password ="1234"

decrypted_file = decrypt_func(path,password)

pure_data = extract_actual_data(decrypted_file)

print(pure_data)