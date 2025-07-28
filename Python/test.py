from datetime import date , datetime,timedelta

today=date.today()




now = datetime.now()
print(now)





future_day = now+timedelta(hours=2)
print(future_day)


today =date.today()
today-timedelta(days=31)
print(today)