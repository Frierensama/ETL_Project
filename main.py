from functions_seperate import *

path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
path2 = "C:/Users/dhanr/Downloads/File1.xlsx"
password ="1234"

decrypted_file = decrypt_func(path,password)

pure_data = extract_actual_data(decrypted_file)
pure_data2 = extract_actual_data(path2)

print(pure_data2)