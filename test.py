# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Importing date
from datetime import date

# Beginning day
bDay = date(2023, 8, 15)
# Get today
today = date.today()

# Opening the html file
HTMLFile = open("target.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
Parse = BeautifulSoup(index, 'html.parser')

# Using the select method
# Prints the second element from the li tag
ol = Parse.find('ol', start=(today - bDay).days)

lis = ol.find_all('li')

idx = 0
for li in lis:
    if idx == 0:
        idx = 1
        continue
    idx += 1
    print(idx)
    print(li.text)
