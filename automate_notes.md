# Automate the Boring Stuff - Notes

## Storing Values in Variables
A variable is like a box in the computer’s memory where you 
can store a single value. to use the result of an evaluated expression later in your program, 
you can save it inside a variable

Assignment Statements
assignment statement is variable name, an equal sign (called the assignment operator)
spam = 42
variable named spam will have the integer value 42 stored in it.

### examples of legal variable names
- It can be only one word with no spaces.
- It can use only letters, numbers, and the underscore (_) character.
- It can’t begin with a number.
Variable names are case-sensitive

Camelcase lookLikeThis


### print()
The _print()_ function displays the string value inside its parentheses on the screen.
print('Hello, world!')
print('What is your name?') # ask for their name

### input()
The input() function waits for the user to type some text on the keyboard and press ENTER.
myName = input()

### Printing the User’s Name
print('It is good to meet you, ' + myName)

### len() 
You can pass the len() function a string value (or a variable containing a string), and the 
function evaluates to the integer value of the number of characters in that string.
len('My very energetic monster just scarfed nachos.')
46

### str()
The str() function is handy when you have an integer or float that you want to concatenate to a 
string. The int() function is also helpful if you have a number as a string value that you want 
to use in some mathematics. For example, **the input() function always returns a string**, even 
if the user enters a number. Enter spam = input() into the interactive shell and enter 101 when 
it waits for your text.
```
>>>spam = input()
101
>>>spam
'101'
The value stored inside spam isn’t the integer 101 but the string '101'.
If you want to do math using the value in spam, use the int() function
to get the integer form of spam and then store this as the new value in spam.
>>>spam = int(spam)
>>>spam
101
Now you should be able to treat the spam variable as an integer instead of a string.
spam * 10 / 5
202.0
```
### int()
The int() function is also useful if you need to round a floating-point number down.
```
>>> int(7.7)
7
>>> int(7.7) + 1
8
```

```
TEXT AND NUMBER EQUIVALENCE

Although the string value of a number is considered a completely different value
from the integer or floating-point version, an integer can be equal to a
floating point.

>>> 42 == '42'
False
>>> 42 == 42.0
True
>>> 42.0 == 0042.000
True

Python makes this distinction because strings are text, while integers
and floats are both numbers.
```

You can even do string replication easily by copying and pasting text.
But **expressions, and their component values—operators, variables, and
function calls—are the basic building blocks that make programs**. Once
you know how to handle these elements, you will be able to instruct
Python to operate on large amounts of data for you.

### Function Calls
Functions are reusable blocks of code that perform specific tasks.
A function call runs the code inside the function and returns a result
```
def add(a, b):
    return a + b

result = add(3, 4)  # Function call: evaluates to 7
```
In a program, you combine values, variables, operators, and function
calls to create expressions that drive the logic and flow of your
program.
```
x = 10           # variable assignment
y = 20           # variable assignment
sum_value = x + y  # expression using variables and operator
print(sum_value)  # function call that outputs the result of the expression
```

### Expressions
Expressions are made up of values, variables, operators, and function
calls, and they are the building blocks that allow a program to
evaluate and return a result.

### Boolean Values
There are two:
- true
- false
When entered as Python code, the Boolean values
True and False lack the quotes you place around strings, and
**they always start with a capital T or F**, with the rest of the word
in lowercase.

### Comparison Operators
Comparison operators, also called relational operators, compare two
values and evaluate down to a single Boolean value.
```

**Operator Meaning**

== Equal to

!= Not equal to

< Less than

> Greater than

<= Less than or equal to

>= Greater than or equal to

```
Note that an integer or floating-point value will always be 
unequal to a string value. The expression 42 == '42'
The <, >, <=, and >= operators, on the other hand, work properly
only with integer and floating-point values.
```
THE DIFFERENCE BETWEEN THE == AND = OPERATORS

You might have noticed that the == operator (equal to) has two
equal signs, while the = operator (assignment) has just one equal
sign. It’s easy to confuse these two operators with each other.
Just remember these points:

The == operator (equal to) asks whether two values are the same as each other.

The = operator (assignment) puts the value on the right into the
variable on the left.

To help remember which is which, notice that
the == operator (equal to) consists of two characters,
just like the != operator (not equal to) consists of two characters.
```
### Boolean Operators
The three Boolean operators (and, or, and not) are used to compare
Boolean values.

The Boolean operators have an order of operations just like the math
operators do. After any math and comparison operators evaluate,
Python evaluates the not operators first, then the and operators,
and then the or operators.

### Elements of Flow Control
Flow control statments ofternstart with a part called the *condition* and
are always followed by a block of code called the *clause*. 

### Conditions
Condition is a more specific name in the contect of 
flow control staements. Conditions always evaluate doen to a Boolean value, *True* or 
*False*. Flow control statement decides what to do based on whether its condition is 
*True* or *False*, and almost every flow control statemt uses a conditon.

### Blocks of Code
Lines of Python code can be grouped together in *blocks*.

### Mixing Boolean and Comparison Operators
the and, or, and not operators are called Boolean operators because they always operate
on the Boolean values True and False. While expressions like 4 < 5 aren’t Boolean values,
they are expressions that evaluate down to Boolean values.

The computer will evaluate the left expression first, and then it will evaluate the right
expression. When it knows the Boolean value for each, it will then evaluate the whole
expression down to one Boolean value. You can think of the computer’s evaluation process
for (4 < 5) and (5 < 6) as the following:

![Boolean Image](https://github.com/user-attachments/assets/ad4c2681-9c9e-4b0d-9b51-5eb081394f1c)

The Boolean operators have an order of eperations just like the math operators do. 
Python evaluates the *not* operators first, then the *and* iperators, and then the 
*or* operators.

### Conditions
Conditions always evaluate down to a Boolean value, True or False. A flow control statement
decides what to do based on whether its condition is True or False, and almost every flow
control statement uses a condition.

### Blocks of Code
Lines of Python code can be grouped tofether in *blocks*. You can tell when a block
begins and ends from the indentation of the lines of code. There are three rules of blocks.
1. Blocks begin when the indentation increases
2. Blocks can contain other blocks
3. Blocks end when the indentation decreases to zero or to a containing block's indentation

```
name = 'Mary'
  password = 'swordfish'
  if name == 'Mary':
    ➊ print('Hello, Mary')
       if password == 'swordfish':
        ➋ print('Access granted.')
       else:
        ➌ print('Wrong password.')

```
The first block of code ➊ starts at the line print('Hello, Mary') and contains all the
lines after it. Inside this block is another block ➋, which has only a single line in
it: print('Access Granted.'). The third block ➌ is also one line long: print('Wrong password.').

### Flow Control Statements

## if Statements
The most common type of flow control statement is the if statement. An if statement’s clause
(that is, the block following the if statement) will execute if the statement’s condition is True.
The clause is skipped if the condition is False.

In plain English, an if statement could be read as, “If this condition is true, execute the code
in the clause.” In Python, an if statement consists of the following:

- The *if* keyword
- A condition (that is, an expression that evaluates to *True* or *False*)
- A colon
- Startin on the next line, an indented block of code (called the *if* clause)
```
if name == 'Alice':
    print('Hi, Alice.')
```

## else Statements

An if clause can optionally be followed by an else statement. The *else* clause is executed only
when the if statement’s condition is False. In plain English, an else statement could be read
as, “If this condition is true, execute this code. Or else, execute that code.” An else
statement doesn’t have a condition, and in code, an *else* statement always consists of the following:
- The *else* keyword
- A colon
- Starting on the next line, an indented block of code (called the *eles* clause)
```
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
```

## elif Statements

The *elif* statement is an "else if" statement
that always follows an *if* or another *elif* statement.
It provides another condition that is checked only if all of the previous 
conditions were *False*. In code, an *elif* statement always consists of the 
following:
- The *elif* keyword
- A condition (that is, an expression that evaluates to *True* or *False*)
- a colon
- Starting on the next line, an indented block of code (called the *elif* clause)

```
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
```
Remember that the rest of the *elif* clauses are automatically skipped once a True
condition has been found. The order of the clauses will matter.

## while Loop Statements

You can make a block of code execute over and over again using a *while* statement. 
The code in a *while* calause will be executed as long as the *while* statement's
condition is *True*.
In code, a *while* statement always consists of the following:
- The *while* keyword
- A condition (that is, an expression that evaluates to *True* or *False*)
- A colon
- Starting with the next line, an indented block of code (called the *while* clause)

Let’s look at an if statement and a while loop that use the same condition and
take the same actions based on that condition. Here is the code with an if statement:
```
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

Here is the code with a while statement:

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
```

## break Statements

If the execution reaches a *break* statement, it immediately exits the *while* loop’s clause.
In code, a *break* statement simply contains the *break* keyword.

<<<<<<< HEAD




=======
## Continue Statements

Like *break* statements, *continue* statements are used inside loops. When the program 
execution reaches a *continue* statement, the program execution immediately jumps back to 
the start of the loop and reevaluates the loop’s condition. (This is also what happens 
when the execution reaches the end of the loop.)

![break chart](https://automatetheboringstuff.com/2e/images/000078.jpg)

If you ever run a program that has a bug causing it to get stuck in an infinite loop, 
press CTRL-C.

## for loops and the range() Function

The *while* loop keeps looping wile its condition is *true* (which is the reason for its
name), but what if you want to execute a block of code only a certain number of times?
You can do this with a *for* loop statement and the *range()* function.

In code, a *for* statement looks something like *for i in range(5)*: and includes the 
following:
- The *for* keyword
- a variable name
- the *in* keyword
- A call to the *range()* method with up to three integers passed to it
- A colon
- Starting on the next line, an indented block of code (called the *for* clause)
```
{print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')}
```

## Starting, Stopping, and Stepping Arguments to range()

Some functions can be called with multiple arguments separated by a comma,
and *range()* is one of them. This lets you change the intefer passed to *range()*
to follow any sequence of integers, including starting wt a number other than zero.
```
for i in range(12, 16):
    print(i)
```

The first athument will be where the *for* loop's wariable starts, and the second
argument will be up to, but not including, the number to stop at.

```
12
13
14
15
```
The *range()* function can also be called with three arguments.
The first two arguments will be the start and stop values, and the third will be the *step 
argument*. The step is the amount that the variable is increased by after each iteration.
```
for i in range(0, 10, 2):
    print(i)
```
So calling range(0, 10, 2) will count from zero to eight by intervals of two.
```
0
2
4
6
8
```
## Importing Modules

All Python programs can call a basic set of functions called *built-in functions*, 
including the *print()*, *input()*, and *len()* functions you’ve seen before. Python also 
comes with a set of modules called the *standard library*. Each module is a Python program 
that contains a related group of functions that can be embedded in your programs. For 
example, the *math* module has mathematics-related functions, the random module has random 
number-related functions, and so on.

Before you can use the functions in a module, you must import the module with an import 
statement. In code, an import statement consists of the following:

The *import* keyword
The name of the module
Optionally, more module names, as long as they are separated by commas

Here's an example of an *import* statement that imports four different modules:
```
import random, sys, os, math
```

## Functions
>>>>>>> 0657be8b40d3ffd4c9fb4258274956c48dfa2636









