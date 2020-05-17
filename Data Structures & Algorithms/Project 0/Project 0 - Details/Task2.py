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



#CODE STARTS:



#initialising an empty set;
listOfNumbers = set()	

#Adding the numbers from calls records;
for item in calls:
	listOfNumbers.add(item[0])		#Adding sending telephone number;
	listOfNumbers.add(item[1])		#Adding receiving telephone number;


#making a dictionary to find the maximum time spent;
#keys = phone numbers;
#values = call durations (that will be kept adding);
totalTime = {}
	
for number in listOfNumbers:
	totalTime.update({number: 0})
	#initialising the keys as unique phone numbers.;
	#initialising the values as call duration = 0, then will be added later;


for item in calls:
	#Accessing the phone numbers, which are in column 0 and column 1; and updating the values of the respective keys;
	#And adding the time duration mentioned in the last column; also string --> integer (that's why int(item[-1]));
	totalTime[item[0]] += int(item[-1])
	totalTime[item[1]] += int(item[-1])


maxCallDuration = max(totalTime.values())	#The longest time spent talking by a speciic phone number;


for (key,value) in totalTime.items():	
	if value == maxCallDuration:
		resultingNumber = key 		#The phone number with the maximum call duration;
		break


print(f"{resultingNumber} spent the longest time, {maxCallDuration} seconds, on the phone during September 2016.")




#CODE ENDS.
