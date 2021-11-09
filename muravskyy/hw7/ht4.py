def count_word(string):
    count_word = {}
    string = list(string.split())
    for i in set(string):
        count_word[i] = string.count(i)
    return count_word

text = input('enter the text\t')
print(count_word(text))