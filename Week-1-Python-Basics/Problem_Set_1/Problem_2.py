#Problem 2
#10.0/10.0 points (graded)
#Assume s is a string of lower case characters.
#
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print:
#Number of times bob occurs is: 2

count = 0
for i in range (0, len(s)-2):
    if (s[i:i+3]) == 'bob':
        count+=1
print("Number of times bob occurs is: " + str(count))        
    