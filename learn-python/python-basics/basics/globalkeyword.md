*Global Keyword:*
Global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.

*Usage:*
We use global keyword to read and write a global variable inside a function.
e.g.
c = 0 # global variable
def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)
add()
print("In main:", c)

*Why Global Variables Should Be Avoided When Unnecessary:*
1) The scope of a variable gets distributed i.e. changing the pure function definition at all.
2) Code Unreadability
3) If two different modules in same code referring/using Global keyword then we might have concurrency issues or more chances of code vulnerability.
4) Difficult to control shared access of variable.

http://wiki.c2.com/?GlobalVariablesAreBad

http://wiki.c2.com/?GlobalVariablesConsideredHarmful


