from datetime import datetime , timedelta

now = datetime.today()

offset = -1

source_path_offset = 0
source_file_offset = 0
desetination_path_offset = 0
desetination_file_offset = 0

lastbday = datetime.today()
nextbday = datetime.today()
########################################### LAST BUSINESS DAY ###################################################
def last_bday_calc(lastbday) -> datetime:
    if datetime.weekday(lastbday) == 5:
        lastbday = lastbday - timedelta(days = 1)
    elif datetime.weekday(lastbday) == 6:
        lastbday = lastbday - timedelta(days = 2)
    return lastbday


def offset_with_last_bday_calc(lastbday, offset) -> datetime:
    while offset != 0 :
        offset -= 1
        lastbday = lastbday - timedelta(days = 1)
        lastbday = last_bday_calc(lastbday)
    return lastbday

####################################################################################################################


########################################### NEXT BUSINESS DAY ######################################################
def next_bday_calc(nextbday) -> datetime:
    if datetime.weekday(nextbday) == 5:
        nextbday = nextbday + timedelta(days = 2)
    elif datetime.weekday(lastbday) == 6:
        nextbday = nextbday + timedelta(days = 1)
    return nextbday


def offset_with_next_bday_calc(nextbday, offset) -> datetime:
    while offset != 0 :
        offset -= 1
        nextbday = nextbday + timedelta(days = 1)
        nextbday = next_bday_calc(nextbday)
    return nextbday

#####################################################################################################################


if offset < 0:
    offset = -offset
    lastbday = offset_with_last_bday_calc(now,offset)
elif offset > 0:
    nextbday = offset_with_next_bday_calc(now,offset)

#print(lastbday,nextbday)