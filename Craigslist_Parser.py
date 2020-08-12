# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:59:50 2018

@author: Joseph
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://vancouver.craigslist.ca/d/apts-housing-for-rent/search/apa'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
"""containers = page_soup.findAll("li",{"class":"result-row"})"""

container = page_soup.findAll("li",{"class":"result-row"})

for i in range(0, 120):
    print("\n")
    try:
        price_container = container[i].find("span", {"class":"result-price"})
        price = price_container.text
    except:
        price = "nAn"
        
    try:
        dateTime_container = container[i].find("time", {"class":"result-date"})
        dateTime = dateTime_container['datetime']
    except:
        dateTime = "nAn"
        
    try:
        type_container = container[i].find("span", {"class":"housing"})
        housingType = type_container.text.replace(' ', '')
        housingType = housingType.replace('\n', '')
    except:
        housingType = "nAn"
        
    try:
        location_container = container[i].find("span", {"class":"result-hood"})
        location = location_container.text.replace(' ', '')
        location = location.replace('(', '')
        location = location.replace(')', '')
    except:
        location = "nAn"
        
    try:
        maptag_container = container[i].find("span", {"class":"maptag"})
        maptag = maptag_container['data-pid']
    except:
        maptag = "nAn"
        
    try:
        title_container = container[i].find("a", {"class":"result-title hdrlnk"})
        title = title_container.text
    except:
        title = "nAn"        
        
    print(title)
    print(price)
    print(dateTime)
    print(housingType)
    print(location)
    print(maptag)