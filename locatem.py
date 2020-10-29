import csv
import requests, json
from core.models import mcpsSchool

from django.shortcuts import get_object_or_404
datareader = csv.reader(open("middleaddr.csv"))

BAD = [41,46]

for row in datareader:
    if int(row[0]) in BAD:
        continue
    obj = get_object_or_404(mcpsSchool,pk=row[0])
    pdfdata = json.loads(requests.get("https://geocoding.geo.census.gov/geocoder/locations/address?street="+row[2]+"&benchmark=9&format=json&zip="+row[3].split(" ")[-1]+"").content)
    print(pdfdata)
    obj.long = float(pdfdata["result"]["addressMatches"][0]['coordinates']["x"])
    obj.lat = float(pdfdata["result"]["addressMatches"][0]['coordinates']["y"])
    obj.save()
    
