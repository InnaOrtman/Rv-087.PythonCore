pi=3.14
s=int(input('push square'))
r=int(input('push radius of cirkle'))
a=s**0.5

if r <= a/2 :
    print ( 'it is possible')

elif r > a/2 :
    print ( 'impossible')