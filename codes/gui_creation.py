import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
appWidth , appHeight = 600 , 700


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
        self.Offset_Source_Path = ctk.CTkLabel(self, text = "Source Offset : ")
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
        self.File_Type_Menu = ctk.CTkOptionMenu(self,values=[".txt",".xml"] , width=40)
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
        self.Offset_Destination_Path = ctk.CTkLabel(self, text = "Destination Offset : ")
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

        self.Fetch_Button = ctk.CTkButton(self,text = "Fetch File")
        self.Fetch_Button.place(x=400,y=490)





if __name__ == "__main__":
   app = App()
   app.mainloop()