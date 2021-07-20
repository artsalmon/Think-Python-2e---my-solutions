"""
Exercise 7.2.
The built-in function eval takes a string and evaluates it using the Python
interpreter. For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the
resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of
the last expression it evaluated.

This example is detailed and added content for end user understanding.
"""


def eval_loop():
    while True:
        user_input  = input("Enter a command (or 'done' to quit):\n")
        if user_input == "done":
            print("The last user input was: ", eval(user_var)) # if "done" is entered, this line will print the last variable (see comment below)
            print("You have entered done, program now exiting.")
            break
        print(eval(user_input))
        user_var = user_input  # this adds the last evaluated to a new variable "user_var"

eval_loop()