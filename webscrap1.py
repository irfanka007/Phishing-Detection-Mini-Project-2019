import requests 
from bs4 import BeautifulSoup 
import csv 
  
URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib')
a=soup.prettify()
#print(a) 
"""
f = open("b4.txt", "w","unicode")
f.write(str(a))
f.close()
  """
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'content'}) 
a=table.prettify()
  
for row in table.findAll('h1', attrs = {'class':'entry-title'}): 
    print(row.text)
