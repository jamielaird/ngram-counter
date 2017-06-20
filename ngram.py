# Import the csv module
import csv

# Import the counter module
from collections import Counter

# Import the time module and set start time
import time
start_time = time.time()

# Set the length of the ngram
n = 5

# Set the number of common ngrams to return
c = 5

# Print runtime info
print ('------------------------')
print ('Ngram length = '+str(n))
print ('Number of common ngrams = '+str(c))

# Define the ngrams function
def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

# Define the input and output files
ihandle = 'C:/Users/jamie.laird/OD/My Documents/2017/2017-06-12 Key Phrase Analysis/Prepared Text/Salford_Emails.csv'
ohandle = 'C:/Users/jamie.laird/OD/My Documents/2017/2017-06-12 Key Phrase Analysis/Python Output/Salford_5grams.csv'

# Create output file
with open(ohandle, 'w', newline='') as csvfile:
    fieldnames = ['email', 'body', 'ngrams', 'top_ngrams']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Print runtime info
print ('Input file: '+ihandle)
print ('Output file: '+ohandle)
print ('------------------------')
print ('Processing ngrams')

# Read from csv file
with open (ihandle) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # Add contents of the body field to full_text
        full_text = row['body']
        email = row['email']

        # Convert all text to lowercase
        full_text = str.lower(full_text)

        # Split words in email
        words = full_text.split()

        # Add words to the list 'input_list'
        input_list = list(words)

        # Invoke the ngrams function
        ngram_list = find_ngrams(input_list,n)

        # Tally occurrences of ngrams for this piece of text
        cnt = Counter(ngram_list)

        # Determine the top ngrams for this piece of text
        top_ngrams = Counter(cnt).most_common(c)

        # Write current record to CSV
        with open(ohandle, 'a', newline='') as csvfile:
            fieldnames = ['email', 'body', 'ngrams', 'top_ngrams']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'email':email, 'body':full_text, 'ngrams':Counter(cnt), 'top_ngrams':top_ngrams})

# Print runtime info
print ('------------------------')
print('Completed in %s seconds' % (time.time() - start_time))
