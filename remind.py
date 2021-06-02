import schedule
import time
from requests import post
from random import choice
from os import environ
from datetime import datetime,date,timedelta
al = date(2021,10,4)
greets = ['Good Morning!','Hello There!','සුභ උදෑසනක්','නැගිටපන් යකෝ']
def sms():
	tday = datetime.utcnow() + timedelta(hours=5,minutes=30)
	tday = tday.date()
	rem = al-tday
	rem = rem.days
	data = {'phone':environ['NUM'],'message':f'{choice(greets)} ඒලෙවල් වලට තව දින {rem}යි.','key':'textbelt'}
	req = post('https://textbelt.com/text',data=data)
	print(req.json())
schedule.every().day.at("00:30").do(sms)
while True:
    schedule.run_pending()
    time.sleep(60)
