import csv

with open('Empath_Database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    dictDatabase = {rows[0]:rows[1] for rows in reader}

dictDatabase.pop(' Word')
infile.close()

print(dictDatabase)

def get(dataBase):
    return dataBase
