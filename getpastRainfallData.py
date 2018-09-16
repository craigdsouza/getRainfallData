# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import timedelta
import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import config

########### Error handling - Retries ###########
def requests_retry_session(
    retries=3,
    backoff_factor=5,
    session=None,
):
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    #session.mount('https://', adapter)
    return session

########### Declare Type of station: AWS,ARG or AGRO ########
#station = 'aws'
station = 'arg'
#station = 'agro'

############# Get states list #############
r = requests.get('http://aws.imd.gov.in/AWS/sta.php',{'types':'aws'})
statesJSON = r.json()
stateslist = statesJSON['data']

############# Get dates range #############
dateStart = date(2018,8,1)		#This customizes dates as needed in YYYY-MM-DD format
dateEnd = date(2018,8,31)      

def date_range(dateStart,dateEnd):
    dtIndex = (dateEnd + timedelta(days=1) - dateStart).days #Counts difference between start and end dates
    dates = []
    for i in range(dtIndex):
        if i % 7 == 0:
            dates.append(dateStart + timedelta(days=i))
    return dates

dateListObj = date_range(dateStart,dateEnd)

############# Get all states data for given date range ############# 
for state in stateslist:
    for dt in dateListObj:
        datef = dt                         #datef is the id name for the select date from id box in the page html
        dateu = dt + timedelta(days=6)     #dateu is the id name for the select date until id box in the page html
        if dateu > dateEnd:
            dateu = dateEnd
        params = {'a': station,
                  'b': str(state),
                  'c':'ALL_DISTRICT',
                  'd':'ALL_STATION',
                  'e': str(datef),
                  'f': str(dateu),
                  'g':'ALL_HOUR',
                  'h':'ALL_MINUTE'}                     
        try:
            r = requests_retry_session().get('http://aws.imd.gov.in/AWS/dataview.php',params=params,timeout=20)
        except requests.exceptions.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
            print("\nResuming download of next date range")
            continue
        if(r.status_code==requests.codes.ok):
            dataSoup = BeautifulSoup(r.text,'html.parser')
            data_table = dataSoup.find_all('table')
            df = pd.read_html(str(data_table),header=0)[0]       # Give the HTML table to pandas to put in a dataframe object
            df.to_csv("{}/{}/{}_{}/{}_{}_{}_{}.csv".format(config.data_folder,station,datef.year,datef.month,station,state,datef,dateu), encoding='utf-8', index=False)    # Save df as csv file
        delay = 10
        time.sleep(delay) # spacing out requests
