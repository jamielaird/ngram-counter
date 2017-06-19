# Import the csv module
import csv

# Import the counter module
from collections import Counter

# Read from csv file
with open ('sample-email.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Add contents of the body field to full_text
        full_text = row['body']

    # Convert all text to lowercase
    full_text = str.lower(full_text)

    # Split words in email
    words = full_text.split()

    # Add words to the list 'input_list'
    input_list = list(words)

    # Define the ngrams function
    def find_ngrams(input_list, n):
        return zip(*[input_list[i:] for i in range(n)])

    # Set the length of the ngram
    n = 2

    # Invoke the ngrams function
    ngram_list = find_ngrams(input_list,n)

    # Tally occurrences of words in a list
    cnt = Counter(ngram_list)

    # Print the number of items in the list
    print ('There are '+str(sum(cnt.values()))+' '+str(n)+'-grams in the file.')

    # Print the full list of n-grams
    print ('The full set of '+str(n)+'-grams is: '),(Counter(cnt))

    # Set the number of common ngrams to return
    c = 3

    # Print the most common phrases
    print ('The '+str(c)+' most common '+str(n)+'-grams are: ',(Counter(cnt).most_common(c)))

    # Write back to CSV file
    ofile = open('output.csv',"wb")
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in reader:
        writer.writerow(row)

        csvfile.close()
        ofile.close()
