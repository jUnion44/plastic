from bs4 import BeautifulSoup
import camelot
import requests
import csv
from core.models import mcpsSchool

ROOT_URL = "https://www.montgomeryschoolsmd.org/"

datadump = [["Middle School","ppp_2014_2015","ppp_2015_2016","ppp_2016_2017","ppp_2017_2018","ppp_2018_2019"]]

html = open("high school links.html","r").read()

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
for link in links:
    school = link.contents[0]
    href = link['href']
    pdfdata = requests.get(ROOT_URL+href).content

    temppdf = open("temp.pdf","wb")
    temppdf.write(pdfdata)
    temppdf.close()

    
    tables = camelot.read_pdf("temp.pdf")
    print("Total tables extracted for " + school + ":", tables.n)
    tables[0].to_csv("temp.csv")

    datareader = csv.reader(open("temp.csv"))
    schooltable = ['"'+school+'"',0.0,0.0,0.0,0.0,0.0]
    
    
    
    for row in datareader:
        for count in range(len(row)):
            try:
                row[count] = row[count].replace("*","")
                schooltable[count] = schooltable[count] + float(row[count])
            except:
                pass
    for count in range(1,6):
        schooltable[count] = str(schooltable[count]/12)

    datadump.append(schooltable)

out = open("outputmiddle.csv","w")
for row in datadump:
    rowstring = ",".join(row)
    out.write(rowstring+"\n")
out.close()
