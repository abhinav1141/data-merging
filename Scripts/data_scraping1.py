from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import pandas as pd
import requests
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
print(page)
soup = bs(page.text,"html.parser")
start_table = soup.find("table")
print(len(start_table))
temp_list = []
table_rows = start_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names = []
distance = []
mass = []
radius = []
Lum =[]

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
df = pd.DataFrame(list(zip(star_names,distance,mass,radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df)
df.to_csv("bright_stars.csv")