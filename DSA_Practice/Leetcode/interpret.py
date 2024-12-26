"""

Write a simple interpreter which understands "+", "-", and "*" operations. 
Apply the operations in order using command/arg pairs starting with the initial value of `value`.
If you encounter an unknown command, return -1.


interpret(1, ["+"], [1]) → 2
interpret(4, ["-"], [2]) → 2
interpret(1, ["+", "*"], [1, 3]) → 6
"""

from tkinter import PIESLICE


def interpret(value, commands, args):
    # Initialise the value
    results = value
    # Number of arguments
    N = len(args)
    # Loop over the arguments
    for i in range(0, N):
        if commands[i] == "+":
            results += args[i]
        elif commands[i] == "-":
            results -= args[i]
        elif commands[i] == "*":
            results *= args[i]
        else:
            results = -1
            break
    return results
    

print(interpret(1, ['+'], [1]) )
print(interpret(4, ['-'], [2]))
print(interpret(1, ['+', '*'], [1, 3]))