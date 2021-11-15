aInput = str(input("Enter the first string: "))
bInput = str(input("Enter the second string: "))

a = list(aInput)
b = list(bInput)

inBoth = set(a+b)
inA = set(a)
inB = set(b)

print("First string: ", aInput) 
print("")
print("Second string: ", bInput)
print("")
print("Set of letters, that are in both arrays ", sorted(inBoth, key=str.casefold))
print("")
print("Set of letters, that are only in first array ", sorted(inA, key=str.casefold))
print("")
print("Set of letters, that are only in second array ", sorted(inB, key=str.casefold))


#Wait A Minute, Doc. Are You Telling Me You Built A Time Machine...Out Of A DeLorean?
#If My Calculations Are Correct, When This Baby Hits 88 Miles Per Hour, You're Gonna See Some Serious Sh*t