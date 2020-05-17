# PROJECT 0 - Investigating Texts and Calls
##### Project Specifications - Unscramble Computer Science Problems

### Project Overview
* In this project, you will complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. You will use Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, you will perform run time analysis of your solution and determine its efficiency. 

## About the Data:
* The text and call data are provided in csv files.
* The text data (text.csv) has the following columns: 
  * sending telephone number (string)
  * receiving telephone number (string)
  * timestamp of text message (string)
* The call data (call.csv) has the following columns: 
  * calling telephone number (string)
  * receiving telephone number (string)
  * start timestamp of telephone call (string)
  * duration of telephone call in seconds (string)
  
###### All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

* Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. 
    * Example: "(022)40840621". 
* Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. 
    * Example: "93412 66159".
* Telemarketers' numbers have no parentheses or space, but start with the code 140. 
    * Example: "1402316533".

### Criteria
* Code Quality --> Your code should be well-structured and readable.
* Output --> Print only the solution outputs. Feel free to use other print statements during the development process, but remember to remove them for submission.
#### Task 0 
* Task 0 - The script correctly prints out the information of first record of texts and last record of calls.
#### Task 1
* Task 1 - The script correctly prints number of distinct telephone numbers in the dataset.
#### Task 2
* Task 2 - The script correctly prints the telephone number that spent the longest time on the phone and the total time in seconds they spend on phone call.
#### Task 3 
* Task 3 - The script correctly prints the telephone codes called by fixed-line numbers in Bangalore and the percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.
#### Task 4 
* Task 4 - The script correctly prints the list of numbers that could be telemarketers.
##### Time - Complexity
* Student provides a text file accurately explaining their run time analysis (Worst-Case Big-O Notation) for each solution they produced.
