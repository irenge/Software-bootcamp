from datetime import datetime

# get current datetime
dt = datetime.now()
print('Datetime is:', dt)

# get weekday name
print('day Name:', dt.strftime('%A'))
