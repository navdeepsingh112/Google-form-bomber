from selenium import webdriver
import random
import time
web = webdriver.Chrome()



def a():
    b=random.randint(0,1)
    if b :
         return("Yes")

    else :
  
     return('No')

property_change = [
]


for i in property_change:
    try :
        web.get('')
        time.sleep(4)
        name = web.find_element('xpath','')
        name.send_keys(i)
        submit = web.find_element('xpath','')
        submit.click()
    except :
        print('errer')
    time.sleep(2)