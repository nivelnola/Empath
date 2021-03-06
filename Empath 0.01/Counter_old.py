# Open Test File
from tkinter.filedialog import askopenfilename
testFilename = askopenfilename()

# Count All Words in File
def allWords(file):
    countall = 0
    for line in file:
        words = line.split()
        countall += len(words) 
    return countall

# General Emotion Counter
def emotion(file, emotionList):
    file = open(testFilename, "r") 
    count = 0
    for line in file:
        words = line.lower().split()
        for word in words :
            #print("Word: ", word)
            if word in emotionList:
                #print("Word found")
                count += 1
    return count

# Count Non-Emotional Words
def nonEmotion(file):
    allEmotional = 0
    allEmotional += emotion(file, FeelingsDatabase.happy)
    allEmotional += emotion(file, FeelingsDatabase.sad)
    allEmotional += emotion(file, FeelingsDatabase.angry)
    allEmotional += emotion(file, FeelingsDatabase.surprised)
    allEmotional += emotion(file, FeelingsDatabase.afraid)
    allEmotional += emotion(file, FeelingsDatabase.disgusted)
    allEmotional += emotion(file, FeelingsDatabase.neutral)
    return allWords(file) - allEmotional
