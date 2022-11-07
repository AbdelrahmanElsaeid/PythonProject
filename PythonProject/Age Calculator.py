from datetime import date
year = int(input('When is your birthday? [YY] '))
month = int(input('When is your birthday? [MM] '))
day = int(input('When is your birthday? [DD] ')) 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age
     

re = calculateAge(date(year, month, day))

print(re, "years")
