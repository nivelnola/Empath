### Import Database
import importDatabase
dataBase = importDatabase.get()
#print("Database imported successfully!")
#print(dataBase)

import Counter 

### Open Test File
from tkinter import *
from tkinter.filedialog import askopenfilename
root = tkinter.Tk()
root.wm_withdraw()
testFilename = askopenfilename()
testFile = open(testFilename, "r")
print (Counter.allWords(testFile))
print (Counter.emotion(testFile, dataBase, "anger"))
print (Counter.emotion(testFile, dataBase, "happy"))
print (Counter.emotion(testFile, dataBase, "sad"))
print (Counter.emotion(testFile, dataBase, "disgust"))
print (Counter.emotion(testFile, dataBase, "fear"))
print (Counter.emotion(testFile, dataBase, "surprise"))
print (Counter.nonEmotion(testFile, dataBase))
print (Counter.allEmotion(testFile, dataBase))
root.destroy()
root.mainloop()

