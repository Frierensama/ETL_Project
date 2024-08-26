import shutil
from datetime import datetime

source_path = "/home/ski/Downloads/Telegram/[yyyy]/[MMM] [yyyy]/[yyyyMMdd]/"
destination_path = "/home/ski/Documents/[yyyy]/[MMM] [yyyy]/[yyyyMMdd]/"

now = datetime.today()

source_file_name = "RandomBank_[yyyy][MM][dd]"
file_type = ""
destination_file_name = ""

def date_formater(file_name)->str:
    x = file_name.replace("[yyyy]",now.strftime("%Y")) 
    x = x.replace("[MMM]", now.strftime("%b"))
    x = x.replace("[yyyyMMdd]", now.strftime("%Y%m%d"))
    x = x.replace("[MM]",now.strftime("%m"))
    x = x.replace("[dd]",now.strftime("%d"))
    x = x.replace("[yyyy-MM-dd]", now.strftime("%Y-%m-%d"))
    return x


source_file_name_format_change = date_formater(source_file_name)
destination_file_name_format_change = date_formater(destination_file_name)
source_path_format_change = date_formater(source_path)
destination_path_format_change = date_formater(destination_path)




#shutil.copyfile(source_path_format_change + file_name_full , dest_path_format_change + file_name_full )

