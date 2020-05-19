#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import os
import json
import time
import urllib3

url='http://dummy.restapiexample.com/api/v1/create'

#inputName = 'Kaushal P. Thakkar'
#inputSalary ='$100000000'
#inputAge = '24'

inputName = os.environ.get('name') #'Kaushal P. Thakkar'
inputSalary = os.environ.get('salary')#'$100000000'
inputAge = os.environ.get('age')#'24'

def employee(name,salary,age):
    try:
        headers = {'Content-Type': 'application/json', "User-Agent": "XY"}
        myData = '{{'name':"{inputName}" ,'salary': "{inputSalary}", 'age':"{inputAge}"}}'.format(inputName=name,inputSalary=salary,inputAge=age)
        #format will convert the data from jenkins to Python... we have to use string since .format  
        #the "{}" is used as excape variable in unix other wise it will be read as 'key'
        response = requests.post( url=url, data=myData, headers=headers) #Since we sending dictionary as string we will use data instead f Json
        #print (response.content)
        print(response.text) # doesnt work
    except Exception:
        return False

#Main method declaration
if __name__ == '__main__':
    if inputName is None or inputSalary is None or inputAge is None:
        print("Insufficient Parameters")
        
    else:
        employee(inputName,inputSalary,inputAge)
      


# In[ ]:





# In[ ]:




