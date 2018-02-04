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

	def setDate(self, date):
		self.date.append(date)

	def setExclusionDate(self, date):
		self.exdate = date