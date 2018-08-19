import importDatabase
# Count All Words in File
def allWords(file):
    countall = 0
    for line in file:
        words = line.split()
        countall += len(words) 
    return countall

# General Emotion Counter:count number of words in each category
def emotion(file, db, emoWord):
    count = 0
    for line in file:
        words = line.lower().split()
        for word in words :
            #print("Word: ", word)
            if word in db :
                #print("Word found")
                if db.get(word) == emoWord:
                    count += 1
    return count

# Count Non-Emotional Words
def nonEmotion(file, db):
    allEmotional = 0
    allEmotional += emotion(file, db, "anger")
    allEmotional += emotion(file, db, "happy")
    allEmotional += emotion(file, db, "sad")
    allEmotional += emotion(file, db, "disgust")
    allEmotional += emotion(file, db, "fear")
    allEmotional += emotion(file, db, "surprise")
    return allWords(file) - allEmotional
