'''
Utility for Date
'''

from datetime import date

from datetime import datetime,timedelta 

def compare_date_to_todays_date(input_date_string):
    year, month_in_string, day = input_date_string.split("-")
    input_date= date(int(year),datetime.strptime(month_in_string, '%m').month,int(day))
    today = date.today()
    #print(today)
    if input_date>today:
        return 1
    return 0

def date_Check(d1, d2):
    new_d1 = datetime.strptime(d1, "%Y-%m-%d")
    
    new_d2 = datetime.strptime(d2, "%Y-%m-%d")
    
    res = new_d1.date() < new_d2.date()
    
    return res

def calculate_age_from_to(from_day,to_day):
    if to_day is None:
        to_day = date.today()        
    return to_day.year - from_day.year - ((to_day.month, to_day.day) < (from_day.month, from_day.day))

def build_date(gedline):
    return date(int(gedline.remaining[2]),datetime.strptime(gedline.remaining[1], '%b').month,int(gedline.remaining[0]))

from datetime import datetime
from dateutil import relativedelta

def build_date(fromDay, toDay):
    date1 = datetime.strptime('2019-01-15', '%Y-%m-%d')
    date2 = datetime.strptime('2019-08-15', '%Y-%m-%d')
    r = relativedelta.relativedelta(date2, date1)
    months = r.months * (r.years+1)
    return months


from datetime import datetime
from dateutil import relativedelta

'''
def checkDiffInMonths(fromDay, toDay):
    date1 = datetime.strptime(fromDay, '%Y-%m-%d')
    date2 = datetime.strptime(toDay, '%Y-%m-%d')
    obj = relativedelta();
    if fromDay > toDay:
       obj= relativedelta.relativedelta(date2, date1)
    else:
       obj= relativedelta.relativedelta(date2, date1)
        
    months= obj.months * (obj.years+1)
    return months
'''
from calendar import monthrange

def checkDiffInMonths(date1, date2):
    delta = 0
    d1 = datetime.strptime(date2, '%Y-%m-%d')
    d2 = datetime.strptime(date1, '%Y-%m-%d')
    while True:
        mdays = monthrange(d1.year, d1.month)[1]
        d1 += timedelta(days=mdays)
        if d1 <= d2:
            delta += 1
        else:
            break
    return delta