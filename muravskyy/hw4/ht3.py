from num2words import num2words


num = int(input('enter number\t'))


word = num2words(len(str(abs(int(num)))))
print('positive', word+'-digit') if num > 0 else print('negative', word+'-digit')
