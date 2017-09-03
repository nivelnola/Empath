# Import Helper Functions
import Counter

# Import Emotions Database
import FeelingsDatabase

# Open Test File
from tkinter.filedialog import askopenfilename
testFilename = askopenfilename()
testFile = open(testFilename, "r") 
print("Opening file: ", testFilename)

# Count All Words
numWords = Counter.allWords(testFile)
print("Total number of words in file: ", numWords)

# Count Happy Words
numHappy = Counter.emotion(testFile, FeelingsDatabase.happy)
print("Total number of happy words: ", numHappy)
print("Percent happy: ", (numHappy/numWords * 100), "%")
