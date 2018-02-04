from datetime import date
from date_formulas import getDay, getWeekOfMonth, daysInMonth

class RRule:
	MO = 0
	TU = 1
	WE = 2
	TH = 3
	FR = 4
	SA = 5
	SU = 6

	DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

	DAILY = "DAILY"
	WEEKLY = "WEEKLY"
	MONTHLY = "MONTHLY"
	YEARLY = "YEARLY"

	FREQUENCIES = [DAILY, WEEKLY, MONTHLY, YEARLY]

	def __init__(self, freq):
		if freq in self.FREQUENCIES:
			self.freq = freq
		else:
			raise ValueError("Invalid frequency")
		self.dtstart = date.today()
		self.until = None
		self.setpos = None
		self.byweekday = []
		self.startDay = getDay(self.dtstart)

	# Sets the start date of the rule
	def setStartDate(self, startDate):
		self.dtstart = startDate
		self.startDay = getDay(startDate)
		return self

	# Sets the date at which this rule ends
	def setUntil(self, untilDate):
		self.until = untilDate
		return self

	# Sets days of the week that the rule applies to
	def setByWeekDay(self, weekday):
		if type(weekday) == list:
			self.byweekday.extend(weekday)
		elif type(weekday) == int:
			self.byweekday.append(weekday)
		else:
			raise ValueError("Improper type for weekday. Must be either a number or a list of numbers")
		return self

	def setByMonthlyDay(self):
		self.setpos = 1
		return self

	def setByMonthlyDate(self):
		self.setpos = None
		return self

	# Checks if a rule would contain a day
	def contains(self, other):
		# Check to make sure date is within the bounds of the rule
		if other < self.dtstart:
			return False
		elif self.until != None and self.until < other:
			return False
		if self.byweekday == []:
			days = [self.startDay]
		else:
			days = self.byweekday
		# Daily Frequency
		if self.freq == self.DAILY:
			if self.byweekday == []:
				return True
			else:
				return getDay(other) in days
		# Weekly Frequency
		elif self.freq == self.WEEKLY:
			return getDay(other) in days
		# Monthly Frequency
		elif self.freq == self.MONTHLY:
			# Only in use if using nth day of week of month
			if self.setpos != None:
				return getWeekOfMonth(other) == setpos and getDay(other) 
			else:
				return self.dtstart.day == other.day
		# Yearly Frequency
		elif self.freq == self.YEARLY:
			return other.day == self.dtstart.day and other.month == self.dtstart.month
		raise ValueError("Could not find properly match rule")

	def occurencesInRange(self, start, end):
		currentYear = start.year
		currentMonth = start.month
		currentDay = start.day
		occurences = []
		while currentYear != end.year or currentMonth != end.month or currentDay != end.day:
			currentDate = date(currentYear, currentMonth, currentDay)
			if self.contains(currentDate):
				occurences.append(currentDate)
			if daysInMonth(currentYear, currentMonth) == currentDay:
				currentDay = 1
				if currentMonth == 12:
					currentMonth = 1
					currentYear += 1
				else:
					currentMonth += 1
			else:
				currentDay += 1
		return occurences