print(models)
import csv
datareader = csv.reader(open("outputmiddle.csv"))
first=False
for row in datareader:
    if not first:
        first = True
        continue
    s = models.mcpsSchool()
    s.name = row[0]
    s.schooltype="middle"
    s.ppp_2014_2015 = row[1]
    s.ppp_2015_2016 = row[2]
    s.ppp_2016_2017 = row[3]
    s.ppp_2017_2018 = row[4]
    s.ppp_2018_2019 = row[5]
    s.ppp_2014_2015_rank = row[6]
    s.ppp_2015_2016_rank = row[7]
    s.ppp_2016_2017_rank = row[8]
    s.ppp_2017_2018_rank = row[9]
    s.ppp_2018_2019_rank = row[10]
    s.lat=0
    s.long=0
    s.save()
