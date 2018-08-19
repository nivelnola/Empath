### Import Database
import importDatabase
dataBase = importDatabase.get()
#print("Database imported successfully!")
#print(dataBase)

import Counter 

### Open Test File
from tkinter.filedialog import askopenfilename
testFilename = askopenfilename()
Counter.allWords(testFilename)
Counter.emotion(testFilename, dataBase, "happy")
Counter.nonEmotion(testFilename, dataBase)



