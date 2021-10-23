import num2words

num = int(input("Enter number:"))
if num < 0:
    digits = num2words.num2words(len(str(num)[1:]))
    posneg = 'negative'
elif num > 0:
    digits = num2words.num2words(len(str(num)))
    posneg = 'positive'
else:
    digits = '1'
    posneg = ''

print(f'Is {posneg} {digits}-digit')
