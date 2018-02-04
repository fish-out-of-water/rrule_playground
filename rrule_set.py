from rrule import RRule

class RRuleSet:

	def __init__(self):
		self.rrule = []
		self.exrule = []
		self.date = []
		self.exdate = []

	def setRule(self, rule):
		self.rrule.append(rule)

	def setExclusionRule(self, rule):
		self.exrule.append(rule)

	def setDate(self, year, month, day):
		self.date.append((year, month, day))

	def setExclusionDate(self, year, month, day):
		self.exdate = self.exdate.append((year, month, day))

	def contains(self, year, month, day):
		result = False
		for rule in self.rrule:
			if rule.contains(year, month, day):
				result = True
		for date in self.date:
			if (year, month, day) == date:
				result = True
		for rule in self.exrule:
			if rule.contains(year, month, day):
				result = False
		for date in self.exdate:
			if (year, month, day) == date:
				result = False
		return result
