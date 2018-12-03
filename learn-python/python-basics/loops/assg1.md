Read about looping in python.

loops in python
1. while loop
Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

2. for loop
Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

3. nested loop  
You can use one or more loop inside any another while, for or do..while loop.

1. While loop:

Syntax:
while expression:
    statement(s)
example:
# while loop 
count = 0
while (count < 3):     
    count = count + 1
    print("Hello all")

output:
Hello all
Hello all
Hello all

2. For loop:

Syntax:

for iterator_var in sequence:
    statement(s)

Examples:

# Python program to illustrate 
# Iterating over a list 
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
    print(i) 

Output:

List Iteration
geeks 
for 
geeks


  
# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
    print(i) 

Output:
Tuple Iteration
geeks
for 
geeks
      
# Iterating over a String 
print("\nString Iteration")     
s = "Geeks"
for i in s : 
    print(i) 

Output:
String Iteration
G
e
e
k
s
       
# Iterating over dictionary 
print("\nDictionary Iteration")    
d = dict()  
d['xyz'] = 123
d['abc'] = 345
for i in d : 
    print("%s  %d" %(i, d[i]))

Output:
Dictionary Iteration
xyz 123
abc 345


3. Nested loops:

Syntax:

with for loops

for iterator_var in sequence: 
    for iterator_var in sequence: 
        statements(s) 
        statements(s) 

with while loops
 
while expression: 
    while expression:  
        statement(s) 
        statement(s) 

Loop Control Statements

Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
1. break statement
Terminates the loop statement and transfers execution to the statement immediately following the loop.
Example:
for letter in 'Python':     
    if letter == 'h':
        break
    print('Current letter :', letter)

Output:
Current letter: P 
Current letter: y 
Current letter: t


2. continue statement
Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
Example:
for letter in 'Python':     
    if letter == 'h':
        continue
    print('Current letter :', letter)

Output:
Current letter: P 
Current letter: y 
Current letter: t
Current letter: o
Current letter: n

3. pass statement
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
Example:
for letter in 'Python':     
    if letter == 'h':
        pass
        print("this is pass block")
    print('Current letter :', letter)

Output:
Current letter: P 
Current letter: y 
Current letter: t
This is pass block
Current letter: h
Current letter: o
Current letter: n
