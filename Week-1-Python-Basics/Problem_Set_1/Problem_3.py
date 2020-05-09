#Problem 3
#15.0/15.0 points (graded)
#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
#
#Longest substring in alphabetical order is: abc

i = 0
long_run = ''
run = s[0]

while i <= len(s)-1:
    
    count = 0
    
    for i in range(i, len(s)-1):
        if s[i] <= s[i+1]:
            run = s[(i-count):(i+2)]
            count +=1
        else:
            break
    if len(run) > len(long_run):
        long_run = run
    i+=1

print("Longest substring in alphabetical order is: " + str(long_run))
 