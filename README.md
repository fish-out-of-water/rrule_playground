# rrule_playground
A custom implementation of core features of the RRule component of RFC 2445 for handling recurring events.

The RRule in this implementation gives the user the ability to create RRules under the following common uses:
- Daily
     - Every day
     - Every day in a set (use ```setByWeekday```)
- Weekly
     - Every week on start day or some other days if using ```setByWeekday```)
- Monthly 
     - Every month on the date of the month (ex: March 5th, April 5th, May 5th) (set using ```setByMonthlyDate```)
     - Every month on the day of the week in the month (ex: 1st Friday of every month) (set using ```setByMonthlyDay```)
- Yearly
     - Every year on that day
     
 Additional features:
 - ```setUntil``` sets the last day of recurrance rule inclusively. Must be a python date object.
 - ```setStartDate``` sets the start date of the recurrence rule. Must be a python date object.
 - ```contains``` determines whether the date passed into the method is part of the recurrance rule. Must pass in a python date object.
