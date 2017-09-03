# Import Helper Functions
import Counter

# Import Emotions Database
import FeelingsDatabase

# Open Test File
testFile = open(Counter.testFilename, "r") 
print("Opening file: ", Counter.testFilename)
print("testFile")

# Count All Words
numWords = Counter.allWords(testFile)
print("Total number of words in file: ", numWords)

# Count Emotion Words
numHappy = Counter.emotion(testFile, FeelingsDatabase.happy)
print("Total number of happy words: ", numHappy)
print("Percent happy: ", (numHappy/numWords * 100), "%")

numSad = Counter.emotion(testFile, FeelingsDatabase.sad)
print("Total number of sad words: ", numSad)
print("Percent sad: ", (numSad/numWords * 100), "%")

numAngry = Counter.emotion(testFile, FeelingsDatabase.angry)
print("Total number of angry words: ", numAngry)
print("Percent angry: ", (numAngry/numWords * 100), "%")

numSurprised = Counter.emotion(testFile, FeelingsDatabase.surprised)
print("Total number of surprised words: ", numSurprised)
print("Percent surprised: ", (numSurprised/numWords * 100), "%")

numAfraid = Counter.emotion(testFile, FeelingsDatabase.afraid)
print("Total number of afraid words: ", numAfraid)
print("Percent afraid: ", (numAfraid/numWords * 100), "%")

numDisgusted = Counter.emotion(testFile, FeelingsDatabase.disgusted)
print("Total number of disgusted words: ", numDisgusted)
print("Percent disgusted: ", (numDisgusted/numWords * 100), "%")

numNeutral = Counter.emotion(testFile, FeelingsDatabase.neutral)
print("Total number of neutral words: ", numNeutral)
print("Percent neutral: ", (numNeutral/numWords * 100), "%")
