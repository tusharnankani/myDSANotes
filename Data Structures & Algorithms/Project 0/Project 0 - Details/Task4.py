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



#CODE STARTS:



#This part code collects the numbers that receive incoming calls, send texts and receive texts;
totalNumbers = set() 

for item in calls:
	totalNumbers.add(item[1])

for item in texts:
	totalNumbers.add(item[0])
	totalNumbers.add(item[1])



teleNumbers = set()

for item in calls:
	#if the number that is calling does not receive incoming calls, send texts and receive texts; then it could be a telemarketer;
	if item[0] not in totalNumbers:
		teleNumbers.add(item[0])


print("\nThese numbers could be telemarketers: ")
for value in sorted(list(teleNumbers)):
	print(value)

    

#CODE ENDS.
