from datetime import date
from rrule import RRule

def testAll():
	testDaily()
	testUntil()
	testWeekly()
	testMonthly()
	testYearly()
	testDaysOfWeek()

def testDaily():
	rule = RRule(RRule.DAILY)
	rule.setStartDate(date.today())
	assert rule.containsDate(date.today())
	rule.setStartDate(date(2018, 1, 1))
	assert rule.containsDate(date(2018,1,1))
	assert not rule.containsDate(date(2017, 12, 31))
	assert rule.containsDate(date(2018, 1, 2))
	assert rule.containsDate(date(2018, 1, 3))
	assert rule.containsDate(date(2018, 2, 1))
	assert rule.containsDate(date(2020, 1, 1))

def testUntil():
	rule = RRule(RRule.DAILY)
	rule.setStartDate(date(2018, 1, 1)).setUntil(date(2018, 1, 31))
	assert rule.containsDate(date(2018, 1, 5))
	assert not rule.containsDate(date(2018, 2, 1))
	assert not rule.containsDate(date(2019, 1, 5))
	rule = RRule(RRule.MONTHLY)
	rule.setStartDate(date(2018, 1, 1)).setUntil(date(2018, 5, 31))
	assert rule.containsDate(date(2018, 1, 1))
	assert rule.containsDate(date(2018, 2, 1))
	assert rule.containsDate(date(2018, 4, 1))
	assert rule.containsDate(date(2018, 5, 1))
	assert not rule.containsDate(date(2018, 5, 2))
	assert not rule.containsDate(date(2018, 6, 1))

def testWeekly():
	rule = RRule(RRule.WEEKLY)
	rule.setStartDate(date(2018, 1, 1)) # Monday
	assert rule.containsDate(date(2018, 1, 1)) # Monday
	assert not rule.containsDate(date(2018, 1, 2)) # Tuesday
	assert not rule.containsDate(date(2018, 1, 3)) # Wednesday
	assert not rule.containsDate(date(2018, 1, 4)) # Thursday
	assert not rule.containsDate(date(2018, 1, 5)) # Friday
	assert not rule.containsDate(date(2018, 1, 6)) # Saturday
	assert not rule.containsDate(date(2018, 1, 7)) # Sunday
	assert rule.containsDate(date(2018, 1, 8))
	assert rule.containsDate(date(2018, 1, 15))
	assert rule.containsDate(date(2018, 1, 22))
	assert rule.containsDate(date(2018, 2, 19))
	assert rule.containsDate(date(2024, 1, 8))
	rule.setStartDate(date(2018, 2, 3)) # Saturday
	assert not rule.containsDate(date(2018, 1, 1))
	assert not rule.containsDate(date(2018, 2, 2))
	assert not rule.containsDate(date(2018, 2, 4))
	assert rule.containsDate(date(2018, 2, 10))
	assert rule.containsDate(date(2018, 2, 17))
	assert rule.containsDate(date(2018, 6, 16))
	assert not rule.containsDate(date(2018, 6, 17))

def testMonthly():
	rule = RRule(RRule.MONTHLY)
	rule.setStartDate(date(2018, 1, 1))
	assert rule.containsDate(date(2018, 1, 1))
	assert rule.containsDate(date(2018, 2, 1))
	assert rule.containsDate(date(2018, 3, 1))
	assert rule.containsDate(date(2019, 4, 1))
	assert not rule.containsDate(date(2018, 1, 2))
	assert rule.containsDate(date(2020, 12, 1))

def testYearly():
	rule = RRule(RRule.YEARLY)
	rule.setStartDate(date(2018, 2, 1))
	assert rule.containsDate(date(2018, 2, 1))
	assert rule.containsDate(date(2019, 2, 1))
	assert rule.containsDate(date(2020, 2, 1))
	assert not rule.containsDate(date(2019, 2, 2))
	assert not rule.containsDate(date(2018, 4, 2))

def testDaysOfWeek():
	rule = RRule(RRule.WEEKLY)
	# Creates a rule for every MO, WE, FRI of 2018
	rule.setStartDate(date(2018, 1, 1)).setUntil(date(2018, 12, 31)).setByWeekDay(["MO", "WE", "FR"])
	assert rule.containsDate(date(2018, 1, 15))
	assert not rule.containsDate(date(2018, 1, 16))
	assert rule.containsDate(date(2018, 1, 17))
	assert not rule.containsDate(date(2018, 1, 18))
	assert rule.containsDate(date(2018, 1, 19))
	assert not rule.containsDate(date(2018, 1, 20))
	assert not rule.containsDate(date(2018, 1, 21))
	assert rule.containsDate(date(2018, 1, 22))
	assert not rule.containsDate(date(2018, 1, 21))

testAll()

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def visualTestRule(rule):
	year = 2018
	for month in range(11):
		print((20 - len(months[month]))//2 * " "+ months[month])
		print("M  T  W  T  F  S  S ")
		first = date(year, month + 1, 1)
		print((first.weekday()) * "   ", end='')
		for day in range(daysInMonth[month]):
			dt = date(year, month + 1, day + 1)
			if rule.containsDate(dt):
				print("X  ", end='')
			else:
				print(dt.day, end=' ')
				if dt.day < 10:
					print(" ", end='')
			if (dt.weekday() == 6):
				print()
		print()
		print()

rule = RRule(RRule.WEEKLY)
rule.setStartDate(date(2018, 1, 1)).setUntil(date(2018, 12, 31)).setByWeekDay(["MO", "WE", "FR"])
visualTestRule(rule)
