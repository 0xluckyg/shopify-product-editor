import csv
from tempfile import NamedTemporaryFile

new = NamedTemporaryFile(delete=False)

with open('original.csv', 'rt', encoding='utf8') as original, new: 
    reader = csv.reader(original,delimiter=',')
    writer = csv.writer(new,delimiter=',')
    print(reader)
    for row in reader:            
        
def setAvailability(row):