#prints a quote to terminal
import datetime # get today's date
import requests # request a webpage
import bs4 # get your soup
import re # get your RegEx
import random # get something random

from bs4 import BeautifulSoup
from datetime import date

today = datetime.date.today() # this imports the time and date using the datetime library
print(today) # this prints it to the terminal
print('What will you do with your time today?') #this can be whatever you want it to be, it will be printed also.

webrequest = requests.get('https://blog.hubspot.com/sales/famous-quotes') # this pulls the website from the internet
soup = BeautifulSoup(webrequest.content, 'html.parser') # this uses the hmtl.parser function of the BeautifulSoup package
products = str(soup.find_all("p"))
products1 = re.findall(r'(?<=<p>\d\..)(.*?)(?=<\/p>)', products, re.MULTILINE)
products2 = re.findall(r'(?<=<p>.\d\..)(.*?)(?=<\/p>)', products, re.MULTILINE)

products = products1 + products2


list = []  
for quote in products:
    author = re.findall(r'(?<=-<em>)(.*)(?=<\/em>)',quote)
    quote = re.sub(r'-<em>(.*)\/em',"",quote)
    list.append(str(quote)+str(author))
    
a=random.randint(0,len(list)-1)
print(list[a])





