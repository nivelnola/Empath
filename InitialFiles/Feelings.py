from FeelingsCount import (count_happy, count_mad, count_interested,
count_confusion, count_brave, count_sad, count_others, count_all)

from tkinter.filedialog import askopenfilename
filename = askopenfilename()
file = open(filename, "r") 

allcount = [count_happy(file), count_mad(file), count_interested(file),
count_confusion(file), count_brave(file), count_sad(file)]

for counters in allcount:
    if (counters / (count_all(file) - count_others(file))) < .1:
        print(counters)

max_count = max(allcount)
print ("the biggest num is", max_count) 
