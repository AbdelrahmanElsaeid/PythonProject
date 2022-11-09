import datetime


def get_first_date():
    year = int(input('Enter Year ? [YY] '))
    month = int(input('Enter Month? [MM] '))
    day = int(input('Enter  Day? [DD] '))

    first = datetime.datetime(year,month,day)
    return first
def get_last_date():
    year = int(input('Enter Year ?  [YY] '))
    month = int(input('Enter Month?  [MM] '))
    day = int(input('Enter  Day?  [DD] '))

    last = datetime.datetime(year,month,day)
    return last

def calculate_dates(first_date, last_date):
    date1 = first_date
    delta = last_date - first_date
    days = delta.total_seconds() / 60 /60 /24
    return days
print("Enter First Date:- ")
f = get_first_date()
print()
print("Enter Last Date:- ")
l = get_last_date()

c = int(abs(calculate_dates(f,l)))
print(c)
