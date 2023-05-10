import datetime, time
while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"), end= "", flush= True)
    print("\r", end = "", flush= True)
    time.sleep(1)