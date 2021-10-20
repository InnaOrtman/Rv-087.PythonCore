dataInBytes = int(input("Enter the amount of information in Bytes: "))
dataInKB = round(dataInBytes/1024,2)
dataInMB = round(dataInBytes/1024**2,2)
print(f'{dataInBytes}Bytes = {dataInKB}KBytes or {dataInMB}MBytes') 
