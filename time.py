

def getRandomDate(starDate, endDate):
    print("Printing random date between ", starDate, "and" , endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'
    starttime = time.mktime(time.strptim(starDate, dateFormat))
    starttime = time.mktime(time.strptim(starDate, dateFormat))
    endtime = time.mktime(time.strptim(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate


print("Random date = ", getRandomDate("1/1/2000", "12/31/2040"))
