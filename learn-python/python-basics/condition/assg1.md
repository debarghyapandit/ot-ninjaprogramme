> Read about conditional statements in python.

# Conditional Statements in Python

In the real world, we commonly evaluate information around us and then choose one course of action or another based on what we observe:

> If the weather is nice, then I’ll mow the lawn. (It’s implied that if the weather isn’t nice, then I won’t mow the lawn.)

In a Python program, the if statement is how we perform this sort of decision-making. It allows for conditional execution of a statement or group of statements based on the value of an expression.

# if Statement

```

if <test expr>:
    <statement>
```
Here, the program evaluates the ```test expression``` and will execute ```statement(s)``` only if the test expression is ```True```.

If the test expression is ```False```, the statement(s) is not executed.

**Note that the colon (:)** following <test expr> is required.

In Python, the body of the if statement is indicated by the indentation. Body starts with an indentation and the first unindented line marks the end.
Python interprets non-zero values as True. None and 0 are interpreted as False.


- compound if statement

In a Python program indentation is used to define compound statements or blocks. In a Python program, contiguous statements that are indented to the same level are considered to be part of the same block.

Thus, a compound if statement in Python looks like this:
```
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>

```

- Python if Statement Flowchart

	![](media/1.jpg)


- Example: Python if Statement

```
#If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

```

outout:

```

3 is a positive number
This is always printed
This is also always printed.

```

# Python if-else Statement


- Syntax of if-else

```
if test expression:
    Body of if
else:
    Body of else

if <test expr>:
    <statement(s)>
else:
    <statement(s)>
```

The ```if..else``` statement evaluates ```test expression``` and will execute body of if only when test condition is True.

If the condition is False, body of ```else``` is executed. Indentation is used to separate the blocks.

- Python if-else Flowchart

	![](media/2.png)


- Example of if-else

```
num = 3

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

```

# Python if-elif-else Statement

- Syntax of if-elif-else

```
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else

```

The elif is short for else if. It allows us to check for multiple expressions.

If the condition for if is False, it checks the condition of the next elif block and so on.

If all the conditions are False, body of else is executed.

Only one block among the several if...elif...else blocks is executed according to the condition.

The if block can have only one else block. But it can have multiple elif blocks.

- Flowchart of if-elif-else

	![](media/3.png)


- Example of if-elif-else

```
num = 3.4


if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

```

# Python Nested if statements

We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.

Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting.
This can get confusing, so must be avoided if we can.

- Python Nested if Example

```
# In this program, we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

```

```
Output 1

Enter a number: 5
Positive number
Output 2

Enter a number: -1
Negative number
Output 3

Enter a number: 0
Zero

```
