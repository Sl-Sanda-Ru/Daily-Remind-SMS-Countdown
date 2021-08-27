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
    today_str = datetime.today().strftime('%A')
	today = (datetime.utcnow() + timedelta(hours=5,minutes=30)).date()
	remaining_days = (count_day - today).days
	req = client.messages.create(body=f'Today Is {today_str}. {choice(greets)} {message} {rem}යි.',from_=environ['FROM'],to=environ['NUM'])
	print(req.sid)
def main():
    schedule.every().day.at(environ['TIME']).do(sms)
if __name__ == '__main__':
    main()
    while True:
        schedule.run_pending()
        sleep(60)
