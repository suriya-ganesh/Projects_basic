import datetime
import time

birth_date = "27/4/1997"
array = birth_date.split("/")
integer = list(map(int,array))
b_year = integer[2]
b_month = integer[1]
b_day = integer[0]
today = datetime.date.today()
birthdate = datetime.date(year = b_year, month = b_month, day = b_day)
days = today.toordinal() -  birthdate.toordinal()
age = int(days/365.25)
age_days = int (days%365.25)