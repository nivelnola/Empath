# import emotion database
import FeelingsDatabase

# open test file
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
file = open(filename, "r") 

# general emotion counter function
def count(file, emotion):
    count = 0
    for line in file:
        words = line.lower().split()
        for word in words :
            if word in emotion:
                count += 1
    return (count)
print (count(file, FeelingsDatabase.happy))
