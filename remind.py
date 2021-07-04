import schedule
from twilio.rest import Client
from time import sleep
from random import choice
from os import environ
from datetime import datetime,date,timedelta
sid = environ['SID']
token = environ['TOKEN']
client = Client(sid,token)
year = int(environ['DAY'].split('-')[0])
month = int(environ['DAY'].split('-')[1].lstrip('0'))
day = int(environ['DAY'].split('-')[2].lstrip('0'))
count_day = date(year,month,day)
greets = environ['GREETS'].split(',')
message = environ['MESSAGE']
def sms():
	tday = datetime.utcnow() + timedelta(hours=5,minutes=30)
	tday = tday.date()
	rem = count_day - tday
	rem = rem.days
	req = client.messages.create(body=f'{choice(greets)} {message} {rem}යි.',from_=environ['FROM'],to=environ['NUM'])
	print(req.sid)
schedule.every().day.at(environ['TIME']).do(sms)
while True:
    schedule.run_pending()
    sleep(60)
