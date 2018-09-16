# 1.getpastRainfallData
Python script that visits IMD website and downloads hourly station rainfall data as
state wise csv files. Overcomes limitations of the 'getRainfallData' script mentioned below.
Note: script does not have automated error handling hence running into an error may
require you to restart the script manually.

## Libraries needed
Beautiful Soup, pandas, datetime, time, random, requests, config

## Variables to be changed
- 'station' (Line 11)
- 'dateStart' and 'dateEnd' (Lines 21 and 22) 
Caution: this script is designed to download at most one month at a time to preserve the file naming
conventions. Hence 'dateStart' and 'dateEnd' should be the first and last dates of the month for 
which data is desired.
- 'data_folder' to be declared in a config.py file located in the same folder as getpastRainfallData.py
'data_folder' = "path/to/data/folder"

# 2.getRainfallData
Old version of Python script that visits IMD website and downloads hourly station 
rainfall data as state wise csv files. Main difference between this and 'getpastRainfallData'
is that this script can only download data from the past one week (a limitation placed by the
IMD website itself)

## Libraries needed
Selenium, Beautiful Soup, pandas, time, random

## Variables to be changed
The only variables you will need to change before running the script are 'datefstr' and 'dateustr'
For instance to download data from the last week 'dateustr' will be today's date in YYYY-MM-DD format
Caution: the IMD website only provides data for the last week, hence trying other dates may throw errors

# Acronyms
AWS - Automatic Weather Stations (573 stations)
ARG - Automatic Rain Gauge stations(1351 stations)
AGRO - Agro stations (128 stations)

# Data
Data downloaded using these scripts can be found at this dropbox [link](https://www.dropbox.com/sh/b9q0fo5rtuv0e8a/AABL5FvzCb-I-JiSzdiP0zXOa?dl=0)


Looking for help from volunteers who can run the script for past years and upload to the shared folder.
Also feedback is welcome! Mail me at craigds022@gmail.com
