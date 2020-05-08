"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = []
incoming_calls = []

for call in calls:
    outgoing_calls.append(call[0])
    incoming_calls.append(call[1])

sending_texts = []
receiving_texts = []

for text in texts:
    sending_texts.append(text[0])
    receiving_texts.append(text[1])

outgoing_calls = list(set(outgoing_calls))
outgoing_calls.sort()

incoming_calls = list(set(incoming_calls))
incoming_calls.sort()

sending_texts = list(set(sending_texts))
sending_texts.sort()

receiving_texts = list(set(receiving_texts))
receiving_texts.sort()

filtered_numbers = []

for call in outgoing_calls:
    if call not in incoming_calls and call not in sending_texts and call not in receiving_texts:
        filtered_numbers.append(call)

print("These numbers could be telemarketers: ")
for num in sorted(filtered_numbers):
    print(num)
        
