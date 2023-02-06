rawstr = input("Enter a Number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival>0:
    print("Nice Work")
else:
    print("Not a Number")    


def thing(x,y):
    val = x+y
    print("Hello")
    print("friend",val)

thing(8,888)


def shan(lang):
    if lang == "es":
        print("Hello")
    elif lang == 'en':
        print('Love')
    else:
        print("Love You")

shan('en')
shan('es')
shan('fkk')
#556shan()


#for i in range[1,25]:
 #   print(i)
#print('Blastoff')


Largest_No_Sofar = -1
print("Brfore",Largest_No_Sofar)
for num in [12,43,53,2,4,5,78,23,54,53,44]:
    if num>Largest_No_Sofar:
        Largest_No_Sofar = num
    print(Largest_No_Sofar,num)
print("After",Largest_No_Sofar )


Smallest = None
print("Brfore", Smallest)
for num in [12,43,53,2,4,5,78,23,54,53,44]:
    if Smallest is None:
        Smallest = num
    elif  num < Smallest:
        Smallest = num
    print(Smallest,num)
print("After",Smallest )


# Strings

fruit = 'banana'
for letter in fruit:
    print(letter)


word = 'banana'
count = 0

for letter in word:
    if letter == 'a':
        count = count+1
print('Total a:', count)


s = 'Monty Python'

print(s[0:4])
print(s[4:5])
print(s[6:20])


a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)


fruit = 'banana'
if 'n' in fruit:
    print(True)

if 'NaN' in fruit:
    print(False)

greet = 'Hello shan'
zap = greet.lower()
print(zap)
zap = greet.upper()
print(zap)


gsd = 'findd'
print(type(gsd))

print(dir(gsd))