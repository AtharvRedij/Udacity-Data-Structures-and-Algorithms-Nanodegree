"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

timeOnPhone = {}

for record in calls:
    if record[0] not in timeOnPhone:
        timeOnPhone[record[0]] = int(record[3])
    else:
        timeOnPhone[record[0]] += int(record[3])

    if record[1] not in timeOnPhone:
        timeOnPhone[record[1]] = int(record[3])
    else:
        timeOnPhone[record[1]] += int(record[3])


caller = max(timeOnPhone, key=timeOnPhone.get)
time = timeOnPhone[caller]

print(f"{caller} spent the longest time, {time} seconds, on the phone during September 2016.")
