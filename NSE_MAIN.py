url = 'https://www.google.com/finance/quote/ADANIPOWER:NSE?hl=en'
url = 'https://www.google.com/finance/quote/533096:BOM?hl=en'

#importing liberaries 

import requests # pip install request 
from bs4 import BeautifulSoup # pip install beautifulsoup4  
import time 


ticker = input('Stock Name:')
exchange = 'NSE'
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}' #we had used this f string so that we can use this ticker in this link using curly braces
for i  in range(3):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser') 
    # here we had get the class of that particular stock value 
    class1 = "YMlKec fxKbKc"
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    # To allow users to search for HTML elements by their class attribute, Beautiful Soup uses class_
    # this strip is used to remove rupee sign from the current value of the stock that is been displaying 
    # this replace sign is used to remove comma fromm the value of the stock that is been displaying 
    # we had displayed all the content in the float 
    print('price:',price)   
    time.sleep(10)


 


