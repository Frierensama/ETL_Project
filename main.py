from functions_seperate import *

path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
path2 = "C:/Users/dhanr/Downloads/File1.xlsx"
password ="1234"

decrypted_file = decrypt_func(path,password) # Returns Decrypted File only decrypt_func()

pure_data = extract_actual_data(decrypted_file) # Returns Data Frame from file -- extract_actual_data()

pure_data2 = extract_actual_data(path2) 

sorted_pure_data2 = sort_by_col(pure_data2,"Debit Interest",True) # Sort the Data Frame by Column and Ascending sort_by_col

print(pure_data2)