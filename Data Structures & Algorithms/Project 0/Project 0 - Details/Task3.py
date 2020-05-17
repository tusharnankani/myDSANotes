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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#CODE STARTS:



#PART - A:

listOfCodes = set()

for item in calls:
#iterating the for loop through the items in call;

	if item[0][:5] == "(080)":
	#if the calling number is a fixed line number and has banglore code;

		if item[1][0] in ['7', '8', '9'] or item[1][5] == " ":
		#if the recieving number is a mobile number; if starting digit is 7, 8 or 9 OR the 5th index has a space; 
			listOfCodes.add((item[1][:4]))
			#if it is a mobile number, adding the prefix of a mobile number which is its first four digits;


		elif item[1][:3] == "140":
		#if the recieving number is a Telemarketers' number;
			listOfCodes.add((item[1][:3]))
			#basically adding "140" to the set;


		elif item[1][:2] == "(0":
		#if the recieving number is a fixed line number; the area codes vary in length but always begin with 0.

			i = item[1].index(')')	
			#we have to find the index where the area code ends since the area codes vary in length;
			listOfCodes.add((item[1][1:i]))
			#adding that area code to the set; which is in between the parentheses;


print("\nThe numbers called by people in Bangalore have codes: ")

for value in sorted(list(listOfCodes)):
	print(value)

#len(sorted(list(listOfCodes))) = 39; there are 39 unique codes that fixed lines numbers from banglore called;




#PART - B:

count = 0
total = 0

for item in calls:
	if item[0][:5] == "(080)":
		total += 1
		if item[1][:5] == "(080)":
			count += 1


percentage = (count / total) * 100

print("\n{p:1.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(p = percentage))
#using the .format() method to have 2 decimal digits;


#CODE ENDS.
