import shutil
import customtkinter

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry("400x200")

label_finale = customtkinter.CTkLabel(app , text = "")

def button_submit_callback():
    try:
 ################################# COPY CODE ##################################################
        static_path = "/home/ski/Downloads/Telegram/"
        folder_name1 = text_entry1.get() + "/"
        folder_name2 = text_entry2.get() + "/"
        file_name = text_entry3.get() + ".txt"


        source_path = static_path + folder_name1 + folder_name2 + file_name 
        dest_path = "/home/ski/Documents/Save_here/"


        shutil.copy(source_path , dest_path)
        
################################################################################################
        label_finale.configure(text = "sucss")

    except Exception as e:
        label_finale.configure(text = e)



button_submit = customtkinter.CTkButton(app , text= "Fetch" , command=button_submit_callback)

text_entry1 = customtkinter.CTkEntry(app , placeholder_text="Month")
text_entry1.pack(padx = 60 , pady = 20)

text_entry2 = customtkinter.CTkEntry(app , placeholder_text="Date")
text_entry2.pack(padx = 60 , pady = 20)

text_entry3 = customtkinter.CTkEntry(app , placeholder_text="File Name")
text_entry3.pack(padx = 60 , pady = 20)


button_submit.pack(padx = 20 , pady = 20)
label_finale.pack(padx = 200 , pady = 40)

app.mainloop()