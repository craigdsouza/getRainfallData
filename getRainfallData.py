# -*- coding: utf-8 -*-
# Libraries you will require
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Download chromedriver for your OS from here http://chromedriver.storage.googleapis.com/index.html?path=2.41/
path_to_chromedriver = 'chromedriver_win32/chromedriver.exe' #  change this path as needed

# Open IMD website
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://aws.imd.gov.in/'
browser.get(url)

arg = browser.find_element_by_id('b')
aws = browser.find_element_by_id('c')
agro = browser.find_element_by_id('d')
daily = browser.find_element_by_id('f')

aws.click()		# Go to AWS page, for ARG, comment out the next line
#arg.click()

# Find elements for dropdowns 'state', 'datef', 'dateu', and button 'viewdata'
sta = browser.find_element_by_id('sta')
datef = browser.find_element_by_id('datef')
dateu = browser.find_element_by_id('dateu')
viewdata = browser.find_element_by_id('dataview')

# Get all dropdown choices as lists of web elements
all_states_options = sta.find_elements_by_tag_name("option")
datef_options = datef.find_elements_by_tag_name("option")
dateu_options = dateu.find_elements_by_tag_name("option")

#Convert all_states_options to a list of strings we can loop through
all_states_list = []
for state in range(len(all_states_options)):
    name = all_states_options[state].get_attribute("value")
    all_states_list.append(name)

all_states_list = all_states_list[1:]

# Define selectors to allow selection of dropdown options
select_sta = Select(browser.find_element_by_name('sta'))
select_datef = Select(browser.find_element_by_name('datef'))
select_dateu = Select(browser.find_element_by_name('dateu'))

datefstr = ''		#Customize these dates as needed in YYYY-MM-DD format
dateustr = ''		#Caution: downloading more than one week at one go may cause the website to throw an error

# Select dates
select_datef.select_by_visible_text(datefstr)
select_dateu.select_by_visible_text(dateustr)

# **********  Get data  *****************
# this code loops through the list of states, 
# extracts the table of data that loads for the chosen set of dates and
# stores the results as a csv file

for state in all_states_list:
    select_sta.select_by_value(state)
    viewdata.click()
    delay = 15 + random.random() * random.randint(1,10)   # Delays to allow page content to load
    time.sleep(delay)

    aws_soup = BeautifulSoup(browser.page_source,'lxml')  # Handover page content to Beautiful Soup to parse for table
    aws_table = aws_soup.find_all('table')

    df = pd.read_html(str(aws_table),header=0)[0]       # Give the HTML table to pandas to put in a dataframe object

    df.to_csv("PATH_TO_DATA/ARG_%s_%s.csv" % (state,datefstr), encoding='utf-8', index=False)    # Save df as csv file

