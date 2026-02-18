"""
def num_days(month):

    if month == 'jan':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'mar':
        print('number of days in',month,'is',31)
    elif month == 'apr':
        print('number of days in',month,'is',30)
    elif month == 'may':
        print('number of days in',month,'is',31)
    elif month == 'jun':
        print('number of days in',month,'is',30)
    elif month == 'jul':
        print('number of days in',month,'is',31)
    elif month == 'aug':
        print('number of days in',month,'is',31)
    elif month == 'sep':
        print('number of days in',month,'is',30)
    elif month == 'oct':
        print('number of days in',month,'is',31)
    elif month == 'nov':
"""
# optimize/shorten the code in the function
# try to reduce the number of conditionals
def num_days(month):
    x = month
    month = month.lower()

    days_31 = ("jan", "mar", "maj", "juli", "aug", "okt", "dec")
    days_30 = ("apr", "jun", "sep", "nov")
    days_28 = "feb"
    if month in days_31:
        print(f"Number of days in {x} is 31")

    elif month in days_30:
        print(f"Number of days in {month} is 30")

    elif month in days_28:
        print(f"Number of days in {month} is 28, "
              f"except when it is a leap year and Februari has 29 days.")
    else:
        print("Input Error")

num_days("jan")

"""" # scrimba solution
def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        # if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in', month, 'is', days)


num_days('jan')
"""