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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""



#CODE STARTS:


#initialising an empty set;
listOfNumbers = set()	


#Adding the numbers from texts records;
for item in texts:
	listOfNumbers.add(item[0])		#Adding sending telephone number;
	listOfNumbers.add(item[1])		#Adding receiving telephone number;

#Adding the numbers from calls records;
for item in calls:
	listOfNumbers.add(item[0])		#Adding sending telephone number;
	listOfNumbers.add(item[1])		#Adding receiving telephone number;

count = len(listOfNumbers)

print(f"There are {count} different telephone numbers in the records.")



#CODE ENDS.





'''
#ALTERNATIVE SOLUTION: Tried using pandas; but couldn't find time-complexity; but it is definitely faster, since pandas are fast.

import pandas as pd
df = pd.read_csv('calls.csv')
dff = pd.read_csv('texts.csv')
phoneNumbers = set ( list(df.A) + list(df.B) + list(dff.A) + list(dff.B)) 
count = len(phoneNumbers)

'''
