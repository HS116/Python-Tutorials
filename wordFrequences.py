text = "My name is Neil and his name is John and we are friends"
text = text.lower()
words = text.split()

#set is chosen, cuz it will discard duplicates
wordsSet = set(words)

#but we need to order the set by saving it as a list, since it is unordered
wordsList = list(wordsSet)
wordsList.sort()

for word in wordsList:
    print(word + " frequency: " + str(words.count(word)))

