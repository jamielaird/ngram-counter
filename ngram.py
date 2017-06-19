# Open and read a text file
handle = open('sherlock-holmes.txt')

email = handle.read()

# convert email to lowercase
email = str.lower(email)

# split words in email
words = email.split()

# add words to the list 'input_list'
input_list = list(words)

# define the n_grams function
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

# invoke the n_grams function and set n
ngram_list = find_ngrams(input_list,6)

# import counter
from collections import Counter

# Tally occurrences of words in a list
cnt = Counter(ngram_list)

# Print the number of items in the list
print ('There are '+str(sum(cnt.values()))+' n-grams.')

# Print the most common phrases
print ('The most common n-grams are:')
print (Counter(cnt).most_common(10))
