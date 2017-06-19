import csv
with open ('sample-email.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        full_text = row['body']
        print(full_text)
