from datetime import date

DAYS = ["SU", "MO", "TU", "WE", "TH", "FR", "SA"]

def getDayRaw(day, month, year):
	return getDay(date(year, month, day))

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


def getWeekOfMonth(day, month, year):
	return (day // 8) + 1

def testGetDay():
	assert "MO" == getDayRaw(1, 1, 2018)
	assert "TU" == getDayRaw(2, 1, 2018)
	assert "WE" == getDayRaw(3, 1, 2018)
	assert "TH" == getDayRaw(4, 1, 2018)
	assert "FR" == getDayRaw(5, 1, 2018)
	assert "SA" == getDayRaw(6, 1, 2018)
	assert "SU" == getDayRaw(7, 1, 2018)

	assert "MO" == getDayRaw(8, 1, 2018)
	assert "TU" == getDayRaw(9, 1, 2018)

	assert "TH" == getDayRaw(1, 2, 2018)
	assert "FR" == getDayRaw(2, 2, 2018)
	assert "SA" == getDayRaw(3, 2, 2018)
	assert "SU" == getDayRaw(4, 2, 2018)
	assert "MO" == getDayRaw(5, 2, 2018)

	assert "SU" == getDayRaw(31, 12, 2017)
	assert "SA" == getDayRaw(30, 12, 2017)
	assert "FR" == getDayRaw(29, 12, 2017)
	assert "TH" == getDayRaw(28, 12, 2017)

	assert "WE" == getDayRaw(12, 4, 2017)
	assert "FR" == getDayRaw(24, 2, 2017)

	assert "TU" == getDayRaw(15, 11, 2016)
	assert "TU" == getDayRaw(29, 3, 2016)

testGetDay()
