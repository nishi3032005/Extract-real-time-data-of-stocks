url = 'https://www.google.com/finance/quote/ADANIPOWER:NSE?hl=en'
url = 'https://www.google.com/finance/quote/533096:BOM?hl=en'

#importing liberaries 

import request # install request 
from bs4 import BeautifulSoup # install beautifulsoup4 
import time 


ticker = input('Stock Number:') # stock number: 543320 <-- this stock number is of zomato 
exchange = 'BOM'
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}' #f string is used for using ticker in this link using curly braces
for i  in range(3):
    response = request.get(url)
    soup = BeautifulSoup(response.text,'html.parser') 
    # here we had got the class of particular stock value 
    class1 = "YMlKec fxKbKc"
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    # To allow users to search for HTML elements by their class attribute, Beautiful Soup uses class_
    # this strip is used to remove rupee sign from the current value of the stock that is been displaying 
    # this replace sign is used to remove comma fromm the value of the stock that is been displaying 
    # we had displayed all the content in the float 
    print('price:',price)   
    time.sleep(10)


 


