import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

# Depends on Selenium to open a browser due to javascript being on the webpage
# Uses BeautifulSoup to parse the HTML
# This program pulls 90 pages of crypto data and inputs it into a dictionary
# You can then enter any name of the crypto and it will tell you its current balance

crypto_dict= dict() 
for urls in range(90): # Opens Firefox to scroll down 
    if urls==0:
        webpage='https://coinmarketcap.com/'
        driver=webdriver.Firefox()
    else:    
        webpage=f'https://coinmarketcap.com/?page={urls+1}'
    
    driver.get(webpage)
    y = 1000
    for timer in range(0,7):   
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 2000
     time.sleep(.1)

    updated_content=driver.page_source # Pulls the HTML Source after scrolling down
    doc = BeautifulSoup(updated_content, 'html.parser') 
    tbody = doc.tbody 
    trs=tbody.contents
        
    for tr in trs[:100]: # All the data needed is in 'tr' in the HTML 
        crypto_name=tr.contents[2].p.string
        try:
            crypto_price=tr.contents[3].a.string
        except:
            crypto_price=tr.contents[3].text
        crypto_dict[crypto_name]=crypto_price  


currency=''

while currency != 'DONE':

    currency = input('What Crypto are you looking for? (Enter DONE to close) ')

    if currency in crypto_dict:
        print(crypto_dict[currency])
    elif currency == 'DONE': break
    else:
        print('Please input a valid currency.')
    
