#this is a comment

def addMult(first, second):
    result = first*second
    if result > 1000:
        result = first + second
    print(result)

print("Testing function 1 on 20 and 30")
addMult(20,30)
print("Testing function 1 on 30 and 40")
addMult(30, 40)

def loopAdd():
    last = 0
    for i in range(0,10):
        print("Current Number {0} Previous Number  {1}  Sum:  {2}".format(i,last,i+last))
        last = i

loopAdd()

def evenChars():
    inputStr = input("Enter a word: ")
    print("Original String is {0}".format(inputStr))
    print("Printing only even chars")
    for i in range(0,len(inputStr)):
        if (i % 2) == 0:
            print(inputStr[i])

#evenChars()

def firstLast(numbers):
    if (numbers[0] == numbers[len(numbers)-1]):
        print("True")
    else :
        print("False")

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
firstLast(numbers_x)
firstLast(numbers_y)


def divisFive(numbers):
    for i in range(0,len(numbers)):
        if ((numbers[i]%5) == 0):
            print(numbers[i])

divisFive([10, 20, 33, 46, 55])

def subStringCount(string, subString):
    count = 0
    if(len(subString)>len(string)):
        print(0)
    else:
        for i in range(0, len(string)-len(subString)):
            j = 0
            running = True
            #j in range(i,i+len(subString)):
            while running:
                if(j > i+len(subString)):
                    running = False
                if(string[i+j] != subString[j]):
                    running = False
                elif(j == len(subString)-1):
                    count+=1
                    running = False
                j+=1
        print("Substring Count is {0}".format(count))

subStringCount("Emma is good developer. Emma is a writer","a")

def patternPrint():
    n = 6
    i = 0
    s = 1
    while (s < n):
        i = 0
        while(i<s):
            print("{0} ".format(s), end="")
            i+=1
        print("")
        s+=1
    
patternPrint()

def stutter(word):
    for i in range(0 , 2):
        print("{0}{1}...".format(word[0],word[1]), end="") 
    print("{0}?".format(word))

testWord = "incredible"
stutter(testWord)

def discount(price, disc):
    disc = (100-disc)/100
    price *= disc
    price = round(price,2)
    print(price)

discount(89, 20)

def invertColor(color):
    first = 255-color[0]
    second = 255-color[1]
    third = 255-color[2]
    retVal = tuple((first,second,third))
    print(retVal)

invertColor((0,0,0))
invertColor((255,255,255))
invertColor((165,170,221))

def virtDAC(number):
    conversion = 5/1023
    number *= conversion
    number = round(number,2)
    print(number)

virtDAC(0)
virtDAC(1023)
virtDAC(400)

#def findHighest(list):