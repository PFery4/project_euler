"""
https://projecteuler.net/problem=19
"""

DAYS_PER_MONTH = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
    'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31
}

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


def isleap(year: int) -> bool:
    return all([year % 4 == 0, year % 100 == 0, year % 400 == 0]) or all([year % 4 == 0, year % 100 != 0])


def solution():
    current_day = {'weekday': 'Monday', 'month': 'January', 'day': 1, 'year': 1900}
    sundays1st = 0
    while (current_day['month'], current_day['day'], current_day['year']) != ('December', 31, 2000):
        current_day['weekday'] = WEEKDAYS[(WEEKDAYS.index(current_day['weekday']) + 1) % 7]
        if isleap(current_day['year']):
            DAYS_PER_MONTH['February'] = 29
        else:
            DAYS_PER_MONTH['February'] = 28
        if current_day['day'] != DAYS_PER_MONTH[current_day['month']]:
            current_day['day'] += 1
        else:
            current_day['day'] = 1
            current_day['month'] = MONTHS[(MONTHS.index(current_day['month']) + 1) % 12]
        if (current_day['day'], current_day['month']) == (1, 'January'):
            current_day['year'] += 1
        if current_day['weekday'] == 'Sunday' and current_day['day'] == 1 and 1901 <= current_day['year'] <= 2000:
            sundays1st += 1
    return sundays1st


if __name__ == '__main__':
    print(solution())
