from tkinter.filedialog import askopenfilename
filename = askopenfilename()
file = open(filename, "r") 

def count_others(file):
    from FeelingsDatabase import others
    file = open(filename, "r") 
    countothers = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in others:
                countothers += 1
    return (countothers)
print (count_others(file))

def count_all (file):
    file = open(filename, "r")
    countall = 0
    for line in file:
        words = line.split()
        countall += len(words) 
    return countall - count_others(file)
allword = (count_all(file))
print (allword)

def count_happy(file):
    from FeelingsDatabase import happy
    file = open(filename, "r") 
    counthappy = 0
    for line in file:
        words = line.lower().split()
        for word in words :
            if word in happy:
                counthappy += 1
    return (counthappy)
print (count_happy(file))
print ((count_happy(file)/allword)*100)

def count_sad(file):
    from FeelingsDatabase import sad
    file = open(filename, "r") 
    countsad = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in sad:
                countsad += 1
    return (countsad)
print (count_sad(file))
print ((count_sad(file)/allword)*100)

def count_mad(file):
    from FeelingsDatabase import mad
    file = open(filename, "r") 
    countmad = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in mad:
                countmad += 1
    return (countmad)
print (count_mad(file))
print ((count_mad(file)/allword)*100)

def count_confusion(file):
    from FeelingsDatabase import confusion
    file = open(filename, "r") 
    countconfusion = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in confusion:
                countconfusion += 1
    return (countconfusion)
print (count_confusion(file))
print ((count_confusion(file)/allword)*100)

def count_neutral(file):
    from FeelingsDatabase import neutral
    file = open(filename, "r") 
    countneutral = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in neutral:
                countneutral += 1
    return (countneutral)
print (count_neutral(file))
print ((count_neutral(file)/allword)*100)

def count_scared(file):
    from FeelingsDatabase import scared
    file = open(filename, "r")
    countscared = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in scared:
                countscared += 1
    return (countscared)
print (count_scared(file))
print ((count_scared(file)/allword)*100)

def count_interested(file):
    from FeelingsDatabase import interested
    file = open(filename, "r")
    countinterested = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in interested:
                countinterested += 1
    return (countinterested)
print (count_interested(file))
print ((count_interested(file)/allword)*100)

def count_love(file):
    from FeelingsDatabase import love
    file = open(filename, "r")
    countlove = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in love:
                countlove += 1
    return (countlove)
print (count_love(file))
print ((count_love(file)/allword)*100)

def count_brave(file):
    from FeelingsDatabase import brave
    file = open(filename, "r")
    countbrave = 0
    for line in file:
        words = line.lower().split()
        for word in words:
            if word in brave:
                countbrave += 1
    return (countbrave)
print (count_brave(file))
print ((count_brave(file)/allword)*100)

file.close()
