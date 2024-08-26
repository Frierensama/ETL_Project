import customtkinter as ctk
import tkinter as tk
import shutil
from offset_and_bday import *
import os


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
appWidth , appHeight = 600 , 700


source_file_name = ""
file_type = ".txt"
destination_file_name = ""

#format change variables intianlize
source_file_name_format_change = ""
destination_file_name_format_change = ""
source_path_format_change = ""
destination_path_format_change = ""
full_source_path_with_file = ""
full_destination_path_with_file =""



source_file_offset = 0
source_path_offset = 0
desetination_file_offset = 0
desetination_path_offset = 0


now = datetime.today()
someday = datetime.today()

today_for_source_path = datetime.today()
today_for_destination_path = datetime.today()
today_for_source_file = datetime.today()
today_for_destination_file = datetime.today()



lastbusday = datetime.today()


def date_formater(file_name , now)->str:
    x = file_name.replace("[yyyy]",now.strftime("%Y")) 
    x = x.replace("[MMM]", now.strftime("%b"))
    x = x.replace("[yyyyMMdd]", now.strftime("%Y%m%d"))
    x = x.replace("[MM]",now.strftime("%m"))
    x = x.replace("[dd]",now.strftime("%d"))
    x = x.replace("[yyyy-MM-dd]", now.strftime("%Y-%m-%d"))
    return x


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Dynamic File Copy GUI")
        self.geometry(f"{appWidth}x{appHeight}")
###################################################### SOURCE ##########################################################
        #Source Path Label
        self.Source_Path = ctk.CTkLabel(self, text = "Source Path : ")
        self.Source_Path.grid(row=0,column=0,padx=20,pady=30,sticky="ew")

        #Source Path Entry Field
        self.Source_Path_Entry = ctk.CTkEntry(self,placeholder_text="/path/to/file/directory/",width=60 ,height=20)
        self.Source_Path_Entry.grid(row=0,column=1,padx=10,pady=20,sticky="ew")

        #Offset Source Path
        self.Offset_Source_Path = ctk.CTkLabel(self, text = "Source Path Offset : ")
        self.Offset_Source_Path.grid(row = 0,column = 2,padx = 30,pady=20,sticky="ew")

        #OFfset Source Entry
        self.Offset_Source_Path_Entry = ctk.CTkEntry(self,placeholder_text="Default 0")
        self.Offset_Source_Path_Entry.grid(row=0,column=3,padx=10,pady=20,sticky="ew")
#########################################################################################################################

################################################ SOURCE FILE DETAILS ###########################################################
        #SFile Name Label
        self.Source_File_Name = ctk.CTkLabel(self, text = "Source File Name : ")
        self.Source_File_Name.grid(row=1,column=0,padx=20,pady=30,sticky="ew")

        #File Name Entry Field
        self.Source_File_Name_Entry = ctk.CTkEntry(self,placeholder_text="RandomBank",width=60 ,height=20)
        self.Source_File_Name_Entry.grid(row=1,column=1,padx=10,pady=20,sticky="ew")

        #Offset File Name
        self.Offset_Source_File = ctk.CTkLabel(self, text = "Source File Offset : ")
        self.Offset_Source_File.grid(row = 1,column = 2,padx = 30,pady=20,sticky="ew")

        #OFfset File Entry
        self.Offset_Source_File_Entry = ctk.CTkEntry(self,placeholder_text="Default 0")
        self.Offset_Source_File_Entry.grid(row=1,column=3,padx=10,pady=20,sticky="ew")

        #File Type DropDown
        file_types = [".txt",".xml"]
        self.File_Type_Menu = ctk.CTkOptionMenu(self,values=file_types, width=40)
        self.File_Type_Menu.grid(row=2,column=2, columnspan = 1,padx=20,pady=20,sticky="ew")
#########################################################################################################################

##################################################### DESTINATION #######################################################
        #Destination Path Label
        self.Destination_Path = ctk.CTkLabel(self, text = "Destination Path : ")
        self.Destination_Path.grid(row=3,column=0,padx=20,pady=30,sticky="ew")

        #Destination Path Entry Field
        self.Destination_Path_Entry = ctk.CTkEntry(self,placeholder_text="/path/to/copy/")
        self.Destination_Path_Entry.grid(row=3,column=1,ipadx = 120,padx=10,pady=20,sticky="ew")

        #Offset Destination Path
        self.Offset_Destination_Path = ctk.CTkLabel(self, text = "Destination Path Offset : ")
        self.Offset_Destination_Path.grid(row=3,column = 2,padx = 30,pady=20,sticky="ew")

        #OFfset Source Entry
        self.Offset_Destination_Path_Entry = ctk.CTkEntry(self,placeholder_text="Default 0")
        self.Offset_Destination_Path_Entry.grid(row=3,column=3,padx=10,pady=20,sticky="ew")
##########################################################################################################################
        
######################################## DESTINATION FILE DETAILS ###########################################################
        #SFile Name Label
        self.Destination_File_Name = ctk.CTkLabel(self, text = "Destination File Name : ")
        self.Destination_File_Name.grid(row=4,column=0,padx=20,pady=30,sticky="ew")

        #File Name Entry Field
        self.Destination_File_Name_Entry = ctk.CTkEntry(self,placeholder_text="RandomBank",width=60 ,height=20)
        self.Destination_File_Name_Entry.grid(row=4,column=1,padx=10,pady=20,sticky="ew")

        #Offset File Name
        self.Offset_Destination_File = ctk.CTkLabel(self, text = "Destination File Offset : ")
        self.Offset_Destination_File.grid(row = 4,column = 2,padx = 30,pady=20,sticky="ew")

        #OFfset File Entry
        self.Offset_Destination_File_Entry = ctk.CTkEntry(self,placeholder_text="Default 0")
        self.Offset_Destination_File_Entry.grid(row=4,column=3,padx=10,pady=20,sticky="ew")

#############################################################################################################
        ############################ ACTION ######################################
        
        def fetch_button_callback():

        
            file_type = self.File_Type_Menu.get()
            source_path = self.Source_Path_Entry.get()
            destination_path = self.Destination_Path_Entry.get()
            source_file_name = self.Source_File_Name_Entry.get()
            destination_file_name = self.Destination_File_Name_Entry.get()
            
            ## offsets
            source_file_offset = self.Offset_Source_File_Entry.get()
            source_path_offset = self.Offset_Source_Path_Entry.get()
            desetination_file_offset = self.Offset_Destination_File_Entry.get()
            desetination_path_offset = self.Offset_Destination_Path_Entry.get()
            
            

            if source_file_offset == '':
                source_file_offset = 0
            if source_path_offset == '':
                source_path_offset = 0
            if desetination_file_offset == '':
                desetination_file_offset = 0
            if desetination_path_offset == '':
                desetination_path_offset = 0
            
            
            if int(desetination_file_offset) <0:
                desetination_file_offset = -int(desetination_file_offset)
                today_for_destination_file = offset_with_last_bday_calc(now,int(desetination_file_offset))
            elif int(desetination_file_offset)>0:
                today_for_destination_file = offset_with_next_bday_calc(now,int(desetination_file_offset))
            else:
                today_for_destination_file = now

            if int(desetination_path_offset) <0:
                desetination_path_offset = -int(desetination_path_offset)
                today_for_destination_path = offset_with_last_bday_calc(now,int(desetination_path_offset))
            elif int(desetination_path_offset)>0:
                today_for_destination_path = offset_with_next_bday_calc(now,int(desetination_path_offset))
            else:
                today_for_destination_path = now

            if int(source_file_offset) <0:
                source_file_offset = -int(source_file_offset)
                today_for_source_file = offset_with_last_bday_calc(now,int(source_file_offset))
            elif int(desetination_file_offset)>0:
                today_for_source_file = offset_with_next_bday_calc(now,int(source_file_offset))
            else:
                today_for_source_file = now

            if int(source_path_offset) <0:
                source_path_offset = -int(source_path_offset)
                today_for_source_path = offset_with_last_bday_calc(now,int(source_path_offset))
            elif int(source_path_offset)>0:
                today_for_source_path = offset_with_next_bday_calc(now,int(source_path_offset))
            else:
                today_for_source_path = now


            ### format changes
            source_path_format_change = date_formater( source_path, today_for_source_path)
            source_file_name_format_change = date_formater( source_file_name, today_for_source_file)
            destination_path_format_change = date_formater( destination_path, today_for_destination_path)
            destination_file_name_format_change = date_formater( destination_file_name, today_for_destination_file)


            ## DIRECTORIES CREATION
            os.makedirs(destination_path_format_change, exist_ok = True)

            #full path with file 
            full_source_path_with_file = source_path_format_change + source_file_name_format_change + file_type
            full_destination_path_with_file = destination_path_format_change + destination_file_name_format_change + file_type
            
            try:
                shutil.copyfile(full_source_path_with_file,full_destination_path_with_file)
                print("Success")
                self.Final_Lable.configure(text = f"File Copied to{destination_path_format_change} Successfully")
            except Exception as e:
                print(e)
                self.Final_Lable.configure(text = e)


        self.Final_Lable = ctk.CTkLabel(self,text="IM HERE")
        self.Final_Lable.place(x=300,y=450)
        self.Fetch_Button = ctk.CTkButton(self,text = "Fetch File" , command=fetch_button_callback)
        self.Fetch_Button.place(x=400,y=490)





if __name__ == "__main__":
   app = App()
   app.mainloop()