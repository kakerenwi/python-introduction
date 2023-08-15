import datetime

def logging():
    print(datetime.datetime.now(), "sending logs to prometheus & datadog")

logging()

