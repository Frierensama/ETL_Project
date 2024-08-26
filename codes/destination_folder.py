import os
from datetime import datetime



now = datetime.today()
dest_path = "/home/ski/Documents/[yyyy]/[MMM] [yyyy]/[yyyyMMdd]/"

dest_path_format_change = dest_path.replace("[yyyy]",now.strftime("%Y")) 
dest_path_format_change = dest_path_format_change.replace("[MMM]", now.strftime("%b"))
dest_path_format_change = dest_path_format_change.replace("[yyyyMMdd]", now.strftime("%Y%m%d"))
dest_path_format_change = dest_path_format_change.replace("[MM]",now.strftime("%m"))
dest_path_format_change = dest_path_format_change.replace("[dd]",now.strftime("%d"))
dest_path_format_change = dest_path_format_change.replace("[yyyy-MM-dd]", now.strftime("%Y-%m-%d"))

print(dest_path_format_change)

os.makedirs(dest_path_format_change, exist_ok = True)