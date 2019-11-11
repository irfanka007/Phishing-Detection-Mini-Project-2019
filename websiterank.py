#Retrieving page ranking
import requests 
from bs4 import BeautifulSoup 
import csv 
import re

a=input("enter the URL ")
b="https://siterankdata.com/"

URL=b+a
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib')
a=soup.prettify()
#print(a) 

table = soup.find('div', attrs = {'class':'panel-body list'}) 
#print(table)

for row in table.findAll('h3', attrs = {'class':'no-margins font-extra-bold text-success'}):
    print("daily traffic is ",row.text)

