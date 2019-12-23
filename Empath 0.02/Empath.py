### Import Database
import importDatabase
dataBase = importDatabase.get()
#print("Database imported successfully!")
#print(dataBase)

import Counter 

### Open Test File
import tkinter
from tkinter.filedialog import askopenfilename
root = tkinter.Tk()
root.title("Select File")
tkFrame = tkinter.Frame(root).pack()
openFileText = tkinter.Label(tkFrame, text="Select a File and Check Your Emotions").pack()
testFilename = askopenfilename()
testFile = open(testFilename, "r")

def allword():
    print (Counter.allWords(testFile))
def anger():
    print (Counter.emotion(testFile, dataBase, "anger"))
    print (str(round(Counter.emotion(testFile, dataBase, "anger")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def happy():
    print (Counter.emotion(testFile, dataBase, "happy"))
    print (str(round(Counter.emotion(testFile, dataBase, "happy")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def sad():
    print (Counter.emotion(testFile, dataBase, "sad"))
    print (str(round(Counter.emotion(testFile, dataBase, "sad")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def disgust():
    print (Counter.emotion(testFile, dataBase, "disgust"))
    print (str(round(Counter.emotion(testFile, dataBase, "disgust")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def fear():
    print (Counter.emotion(testFile, dataBase, "fear"))
    print (str(round(Counter.emotion(testFile, dataBase, "fear")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def surprise():
    print (Counter.emotion(testFile, dataBase, "surprise"))
    print (str(round(Counter.emotion(testFile, dataBase, "surprise")/Counter.allEmotion(testFile, dataBase)*100, 2))+"%")
def nonemotion():
    print (Counter.nonEmotion(testFile, dataBase))
def allemotion():
    print (Counter.allEmotion(testFile, dataBase))

allwordbutton = tkinter.Button(tkFrame, text="Count All the Words", command=allword).pack()
angerbutton = tkinter.Button(tkFrame, text="Percentage of Anger", command=anger).pack()
happybutton = tkinter.Button(tkFrame, text="Percentage of Happiness", command=happy).pack()
sadbutton = tkinter.Button(tkFrame, text="Percentage of Sadness", command=sad).pack()
disgustbutton = tkinter.Button(tkFrame, text="Percentage of Disgust", command=disgust).pack()
fearbutton = tkinter.Button(tkFrame, text="Percentage of Fear", command=fear).pack()
surprisebutton = tkinter.Button(tkFrame, text="Percentage of Surprise", command=surprise).pack()
nonemotionbutton = tkinter.Button(tkFrame, text="Count All Non-Emotional Words", command=nonemotion).pack()
allemotionbutton = tkinter.Button(tkFrame, text="Count All Emotional Words", command=allemotion).pack()

root.mainloop()

