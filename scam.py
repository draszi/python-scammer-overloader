import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$S%^&*()'
random.seed = (os.random(1024)

#request URL                
url = 'insert_scammer_url'

names = json.loads(open('names.json').read())

for name in names:
  name_number = ''.join(random.choice(string.digits))
  
   username = name.lower() + name_extra + '@hotmail.com'
   password = ''.join(random.choice(chars) for i in range(9))
   
   requests.post(url, allow_redirets=False, data={
    #these values are retrieved from browser console, look for FORM DATA
    'some_id': some_name,
    'some_other_id': some_other_name
   })
   
