import time
from datetime import datetime as dt
import os 

os.chdir('/Users/zico/Dev/Mega_course/App3 - Website Blocker')

hosts_temp = ("hosts")
hosts_path = ('/etc/hosts')
redirect = ('127.0.0.1')
website_list = ['www.facebook.com', 'facebook.com', 'www.gazeta.pl', 'gazeta.pl']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working hours...')
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in website_list:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
            
    else:
        print("Fun hours...")
        
    time.sleep(5)