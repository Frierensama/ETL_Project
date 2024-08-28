from functions_seperate import *

path = "C:/Users/dhanr/Downloads/Rawdata.xlsx"
path2 = "C:/Users/dhanr/Downloads/File1.xlsx"
password ="1234"

decrypted_file = decrypt_func(path,password) # Returns Decrypted File only -- decrypt_func()

pure_data = extract_actual_data(decrypted_file) # Returns Data Frame from file -- extract_actual_data()

pure_data2 = extract_actual_data(path2) 

sorted_pure_data2 = sort_by_col(pure_data2,"Debit Interest",True) # Sort the Data Frame by Column and Ascending sort_by_col

filtered_pure_data2 = filter_by_query(sorted_pure_data2 , '`Debit Interest` > 20') # if column name has space [Debit Interest] use this symbol[``]# Filter the Data with Fileter_by_query(dataframe , query)

#Rows Aggregation -- groupby
colname_to_groupby = "Currency"
col_groupby_names = ["Value Date","Net Debit Balance","Debit Interest"]
col_groupby_funcs = ["first","mean","max"]

agg_pure_data2 = group_rows(pure_data , colname_to_groupby ,col_groupby_names , col_groupby_funcs)

print(agg_pure_data2)