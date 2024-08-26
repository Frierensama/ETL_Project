from datetime import datetime

source_path = "/home/ski/Downloads/Telegram/[yyyy]/[MMM] [yyyy]/[yyyyMMdd]/"
file_name = "Testing.txt"

now = datetime.today()

def date_formater(file_name)->str:
    x = file_name.replace("[yyyy]",now.strftime("%Y")) 
    x = x.replace("[MMM]", now.strftime("%b"))
    x = x.replace("[yyyyMMdd]", now.strftime("%Y%m%d"))
    x = x.replace("[MM]",now.strftime("%m"))
    x = x.replace("[dd]",now.strftime("%d"))
    x = x.replace("[yyyy-MM-dd]", now.strftime("%Y-%m-%d"))
    return x

source_path_format_change = date_formater(source_path)
print(source_path_format_change)


