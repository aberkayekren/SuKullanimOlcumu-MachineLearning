import printData as pd
import datetime as dt

dates = []

for i in range(len(pd.dates)):
    epochTimeStamp = int(pd.dates[i])
    datetimeObject = dt.datetime.fromtimestamp(epochTimeStamp / 1000)
    dateString = datetimeObject.strftime('%Y-%m-%d')
    dates.append(dateString)