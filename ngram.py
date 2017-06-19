# Open a text file
handle = open('sherlock-holmes.txt')

# Read the contents to full_text
full_text = handle.read()

# Convert all text to lowercase
full_text = str.lower(full_text)

# Split words in email
words = full_text.split()

# Add words to the list 'input_list'
input_list = list(words)

# Define the n_grams function
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

# Invoke the n_grams function and set n
ngram_list = find_ngrams(input_list,6)

# Import counter
from collections import Counter

# Tally occurrences of words in a list
cnt = Counter(ngram_list)

# Print the number of items in the list
print ('There are '+str(sum(cnt.values()))+' n-grams.')

# Print the most common phrases
print ('The most common n-grams are:')
print (Counter(cnt).most_common(10))
