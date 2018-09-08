# getRainfallData
Python script that visits IMD website and downloads hourly station rainfall data as 
state wise csv files

# Libraries needed
Selenium, Beautiful Soup, pandas, time, random

# Variables to be changed
The only variables you will need to change before running the script are 'datefstr' and 'dateustr'
For instance to download data from the last week 'dateustr' will be today's date in YYYY-MM-DD format
Caution: the IMD website only provides data for the last week, hence trying other dates may throw errors

# AWS/ARG/AGRO
AWS - Automatic weather stations (573 stations)
ARG - Unknown acronym stations(1351 stations)
AGRO - Agro stations (128 stations)