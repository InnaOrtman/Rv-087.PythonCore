print ('Введіть розмір файлу в байтах')
bytes = int(input())

kilobytes = bytes / 1024;
megabytes = kilobytes / 1024;

print('Значення в байтах: ', bytes, 'Б')
print('Значення в кілобайтах: ', kilobytes, 'КБ')
print('Значення в мегабайтах: ', megabytes, 'МБ')


