class Day:

    def __init__(self, num, month):
        self.num = num
        self.month = month
        self.year = month.giveYear()

    def getDay(self):
        return self.num

    def getMonth(self):
        return self.month.getMonth()

    def giveMonth(self):
        return self.month

    def getYear(self):
        return self.year.getYear()

    def giveYear(self):
        return self.year

    def getDate(self):
        return [self.num, self.month.getMonth(), self.year.getYear()]

    def setDayofWeek(self, num): #1 = Sunday, 7 = Saturday
        self.day = num

    def getDayofWeek(self):
        return self.day

    

class Month:

    def __init__(self, num, year):
        self.num = num
        self.monthsDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.monthsLeapDict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        self.year = year

    def getMonth(self):
        return self.num

    def getYear(self):
        return self.year.getYear()

    def giveYear(self):
        return self.year

    def getDate(self):
        return [self.num, self.year.getYear()]

    def numDays(self):
        if self.year.isLeap():
            return self.monthsLeapDict[self.num]
        return self.monthsDict[self.num]
    

class Year:

    def __init__(self, num):
        self.num = num

    def getYear(self):
        return self.num

    def isLeap(self):
        if self.num%4 != 0:
            return False
        if self.num%100 == 0 and self.num%400 != 0:
            return False
        if self.num%400 == 0:
            return True
        else:
            return True
        
#January 1st, 1901 was a Tuesday
#day.getDate() is expressed as a list [day, month, year]
years = [Year(i) for i in range(1901, 2001)]
months = []
for year in years:
    yearMonths = [Month(i, year) for i in range(1, 13)]
    months.append(yearMonths)
#months[year][month]
#months[num] gives the year 1901+num
#months is a list of lists. The sublists are lists of Month objects, organized by year.
days = []
yearNum = 0#represents the seconday list that represents one year
for year in months:
    monthNum = 0#represents the tertiary list that represents one month
    days.append([])
    for month in year:
        dayNums = month.numDays()
        days[yearNum].append([])#adds one month list into the appropriate year lis
        days[yearNum][monthNum] += [Day(i, month) for i in range(1, dayNums+1)]
        monthNum += 1#goes forward one month list
    monthNum = 0
    yearNum += 1
    
dates = []

for year in days:
    for month in year:
        for day in month:
            dates += [day]

current = 3

for day in dates:
    day.setDayofWeek(current)
    if current==7:
        current = 1
    else:
        current += 1

answer = 0

for day in dates:
    if day.getDayofWeek() == 3 and day.getDay() == 1:
        answer += 1

print(answer)

