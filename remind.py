import schedule
from time import sleep
from requests import post
from random import choice
from os import environ
from datetime import datetime,date,timedelta
year = int(environ['DAY'].split('-')[0])
month = int(environ['DAY'].split('-')[1].lstrip('0'))
day = int(environ['DAY'].split('-')[2].lstrip('0'))
count_day = date(year,month,day)
greets = environ['GREETS'].split(',')
def sms():
	tday = datetime.utcnow() + timedelta(hours=5,minutes=30)
	tday = tday.date()
	rem = count_day - tday
	rem = rem.days
	data = {'phone':environ['NUM'],'message':f'{choice(greets)} {message} {rem}යි.','key':'textbelt'}
	req = post('https://textbelt.com/text',data=data)
	print(req.json())
schedule.every().day.at(environ['TIME']).do(sms)
while True:
    schedule.run_pending()
    sleep(60)
