import datetime


def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime.datetime(year,month,day)
    return birthday


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta = date2 - date1
    
    days = delta.total_seconds() / 60 /60 /24

    return days




#--------------------------------------------------------------

bd = get_user_birthday()
now = datetime.datetime.now()
c = int(abs(calculate_dates(bd,now)))
print(c)
