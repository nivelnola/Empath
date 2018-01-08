import csv

#Open file and establish format of dictionary
with open('Empath_Database.csv', mode='r') as infile:
    reader = csv.reader(infile)
    dictDatabase = {rows[0]:rows[1] for rows in reader}

#Removes Header
dictDatabase.pop(' Word')

infile.close()

#print(dictDatabase)

def get():
    return dictDatabase
