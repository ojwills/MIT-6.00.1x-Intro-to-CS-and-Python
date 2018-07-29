#Exercise: apply to each 1
#5.0/5.0 points (graded)
#
#Here is the code for a function applyToEach:
#
#def applyToEach(L, f):
#    for i in range(len(L)):
#        L[i] = f(L[i])
#Assume that
#
#testList = [1, -4, 8, -9]
#For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.
#
#Example Question:
#
#>>> print(testList)
#[5, -20, 40, -45]

# >>> print(testList)
#  [1, 4, 8, 9]

def positiveNumbers(a):
    return abs(a)

applyToEach(testList, positiveNumbers)

#Correct 

# >>> print(testList)
#  [2, -3, 9, -8]

def addOne(a):
    return a + 1

applyToEach(testList, addOne)

#Correct

#>>> print testList
#  [1, 16, 64, 81]

def numberSquared(a):
    return a**2

applyToEach(testList, numberSquared)

#Correct