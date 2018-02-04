from datetime import date

DAYS = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDayRaw(day, month, year):
	# March is considered the first month of the year
	# So that leap years don't affect the formula.
	if month <= 2:
		month += 10
		year -= 1
	else:
		month -= 2
	C = year // 100
	D = year % 100
	return DAYS[((day + ((13*month)-1)//5) + D + (D//4) + (C//4) - (2*C)) % 7]

def getDay(date):
	month = date.month
	day = date.day
	year = date.year
	# March is considered the first month of the year
	# So that leap years don't affect the formula.
	if month <= 2:
		month += 10
		year -= 1
	else:
		month -= 2
	C = year // 100
	D = year % 100
	return DAYS[((day + ((13*month)-1)//5) + D + (D//4) + (C//4) - (2*C)) % 7]


def getWeekOfMonth(year, month, day):
	return (day // 8) + 1

def isLeapyear(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysInMonth(year, month):
	if month == 2:
		return 29 if isLeapyear(year) else 28
	return monthDays[month - 1]

