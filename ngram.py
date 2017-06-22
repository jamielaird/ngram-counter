# Import the csv module
import csv

# Import the counter module from collections
from collections import Counter

# Import the itemgetter module
from operator import itemgetter

# Import the time module and set the start time
import time
start_time = time.time()

# Set the length of the ngram
n = input("Set ngram length: ")
n = int(n)

# Define the ngrams function
def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

# Define the input and output files
ihandle = 'C:/Users/jamie.laird/OD/My Documents/2017/2017-06-12 Key Phrase Analysis/Prepared Text/Salford_Emails.csv'
ohandle = 'C:/Users/jamie.laird/OD/My Documents/2017/2017-06-12 Key Phrase Analysis/Python Output/'+str(n)+'grams.csv'

# Create output file
with open(ohandle, 'w', newline='') as csvfile:
    fieldnames = ['crms_number', 'email_id', 'n', 'ngrams']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Print runtime info
print ('------------------------')
print ('Input file: '+ihandle)
print ('Output file: '+ohandle)
print ('------------------------')
print ('Processing ngrams')

# Open the target csv file
with open (ihandle) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # Read from the specified fields
        full_text = row['body']
        crms_number = row['crms_number']
        email_id = row['email_id']

        # Convert crms_number and id to string
        crms_number = str(crms_number)
        email_id = str(email_id)

        # Convert body text to lowercase
        full_text = str.lower(full_text)

        # Split words in email
        words = full_text.split()

        # Add words to the list 'input_list'
        input_list = list(words)

        # Invoke the ngrams function
        ngram_list = find_ngrams(input_list,n)

        # Tally occurrences of ngrams for this piece of text
        cnt = Counter(ngram_list)

        # Sort the dictionary by value
        sorted(cnt.items(), key=itemgetter(0))

        # Write current record to CSV
        with open(ohandle, 'a', newline='') as csvfile:
            fieldnames = ['crms_number', 'email_id', 'n', 'ngrams']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'crms_number':crms_number, 'email_id':email_id, 'n':str(n), 'ngrams':cnt})

# Print runtime info
print ('------------------------')
print('Completed in %s seconds' % (time.time() - start_time))
