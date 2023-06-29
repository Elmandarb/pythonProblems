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

evenChars()