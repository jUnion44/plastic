# Installation Instructions

## Required Dependencies:
-Python3

-Django

-Camelot (Python implementation of Tabula)

-BeautifulSoup

-GeoJSON [Area](https://github.com/mapbox/geojson-area)

## Setting up the database

Navigate to the folder where you wish to start your project.  Run 'django-admin startproject your_project_name' (plastic is recommended).  Navigate to the folder the command created, which should have the same name as the project.  In that folder, run `python3 manage.py startapp core`.  This command should make a folder called "core."  Please copy the admin, views, models, and url files from the core folder in this repository into the folder you created.  Run `python3 manage.py migrate` to set up the database.

If using the settings module provided, set the "SECRET_KEY" environmental variable to something secure.  Django uses the secret key 

Run `python3 manage.py createsuperuser` to make an administrator account on the server, which will allow the user to edit any data.

## Importing data

A list of Zip Codes in Montgomery County can be downloaded [here](https://www.zip-codes.com/county/md-montgomery.asp).  Some Zip Codes do not have geographical areas.  A list of Zip Codes used is also located in the geojson folder.

A data table with Median Household Income and population for Zip Code Tabulation Areas (Census-designated boundaries which roughly mimic Zip Codes) can be found [here](https://data.census.gov/cedsci/table?q=United%20States&t=Income%20and%20Earnings&g=0100000US.860000&tid=ACSST5Y2018.S1903&hidePreview=true).

Run extracthigh.py and extractmiddle.py to download all of the recycling data, which will be saved to outputmiddle.csv and outputhigh.csv.  For each file, there will be columns with the recycling pounds per person rate for five school years.  Make new columns to store the rankings of each school using the Excel rank function.  Save this output as a csv.

To obtain the latitude and longitude coordinates of middle schools, run `python3 manage.py shell` and then `exec(open("locatem.py").read())` to load in middle school addresses.  Some schools like Silver Creek MS must be manually searched on Google Maps.  High schools were manually searched before the automatic scraping program was written.  The program uses data from the Census Bureau API.  There is no charge or API Key required.

The data above, apart from the coordinates, were manually inputted into the database in the command line using `python3 manage.py shell.`  Depending on how the CSVs are set up with the ranking, import the data by reading each line in each CSV file and writting to the appropriate fields.  Import data into the mcpsSchool and zipcode models.

When the data importing is complete one may run `python3 manage.py runserver` to run the server on `127.0.0.1:8000` by default.

## Alternate Method

Simply clone the repo and run `python3 manage.py runserver` using the default admin credentials (username plastic password plastic).

# Model Field Reference

## mcpsSchool

schooltype - the type of school ("middle" or "high")

name - the name of the school

ppp_20XX_20XY - the pounds per person rate for the 20XX-20XY school year

ppp_20XX_20XY_rank - the pounds per person ranking for the 20XX-20XY school year relative to other schools

lat/long - geographical coordinates

desc - a description of any trends noted in each school

link - not used

## zipcode

code - 5 digit name of the Zip Code

geodata - geoJSON geometry of the Zip Code

area - Area of the Zip Code in square meters obtained with the area function

population - Total population of the Zip Code

average_income - Median household income (the mean household income was originally used, hence the field name)

density - Population density in persons per square meter (must be calculated manually)
