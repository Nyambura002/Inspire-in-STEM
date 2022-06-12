#!/usr/bin/python

#Date : 10/06/2022

import requests  
from bs4 import BeautifulSoup as bs

user_name = "Nyambura002" #input("Enter your username")
url = "https://github.com/"+user_name # input("Enter site url")
results = requests.get(url) 

soup = bs(results.content, "html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'},['src'])

print(profile_pic)
