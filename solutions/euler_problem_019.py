"""

https://projecteuler.net/problem=19

"""

dayspermonth = {'January': 31, 'February': 28, 'March': 31,
                'April': 30, 'May': 31, 'June': 30,
                'July': 31, 'August': 31, 'September': 30,
                'October': 31, 'November': 30, 'December': 31}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    current_day = {'weekday': 'Monday', 'month': 'January', 'day': 1, 'year': 1900}

    sundays1st = 0

    while (current_day['month'], current_day['day'], current_day['year']) != ('December', 31, 2000):
        current_day['weekday'] = weekdays[(weekdays.index(current_day['weekday']) + 1) % 7]
        if isleap(current_day['year']):
            dayspermonth['February'] = 29
        else:
            dayspermonth['February'] = 28
        if current_day['day'] != dayspermonth[current_day['month']]:
            current_day['day'] += 1
        else:
            current_day['day'] = 1
            current_day['month'] = months[(months.index(current_day['month']) + 1) % 12]
        if (current_day['day'], current_day['month']) == (1, 'January'):
            current_day['year'] += 1
        if current_day['weekday'] == 'Sunday' and current_day['day'] == 1 and 1901 <= current_day['year'] <= 2000:
            sundays1st += 1

    return sundays1st


if __name__ == '__main__':
    print(main())
