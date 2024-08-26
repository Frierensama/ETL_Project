#inports
from datetime import datetime

now = datetime.today()

#formats
formats = ["yyyy","yy","yyyyMMdd","MMM"]
formats_map = ["%Y","%y","%Y%m%d","%b"]
datetime_str = now.strftime("%Y%m%d")
print(datetime_str)

#monday == 0 , sunday == 6
print(now.weekday())

