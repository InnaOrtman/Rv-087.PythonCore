words = "Python Python Python Python is an interpreted high-level general-purpose programming language. \
Its design philosophy emphasizes code readability with its use of significant \
indentation. Its language constructs as well as its object-oriented approach \
aim to help programmers write clear, logical code for small and large-scale projects."

word_list = words.split()
wordsDict = {}
repeatList = list()

for i in word_list:
    wordsDict[i] = word_list.count(i)

print(wordsDict)