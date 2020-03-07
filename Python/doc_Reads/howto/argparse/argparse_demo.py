# This program demonstrates how to use argparse in python.
import argparse

parser = argparse.ArgumentParser(description='This program demonstrates how to use argparse module in python.')

# Define your args from here:

# 1.Positional argument.
# This method indicates which arg is **required** in this program.
# Actually, echo is a **positional argument**.
# 'help' keyword indicates the help msg shown when the --help/-h is used.
parser.add_argument("echo", help="echo the string you use here.")

# 'type' keyword indicates the type that argparse will treat the input value.
# If the type mismatches, then a error will be raised:
    # argparse_demo.py: error: argument square: invalid int value: '123.321'
# square is a positional argument.
parser.add_argument("square", help="display a square of a given number.", type=int)

# -----------------------------------------
# 2.Introducing Optional arguments
# The order of optional arguments doesn't matter.
# Add '-' or '--' in front of a argument, then the argument will become optional.
# 'choice' keyword indecates the range of accetable input.
    # should use 'type' here other wise, choice should be ['0', '1', '2']
parser.add_argument('-v','--verbosity', help='increase output verbosity.', choices=[0,1,2], type=int)

# By default, if an optional argument isn't used, the relavent variable, in this case, args.verbosity
# is given None as a value, which is the resaon it falls the truth test of the if statement.
# That is to say, if we do not use the --verbosity args, the program will not go run.
# If we use the --verbosity args, but do not pass a value to the program, then the program
# will crash.
# If we use the --verbosity args, and pass it **any value**, the program will print the msg:
# 'Verbosity turned on.'

parser.add_argument('-l', help='Demonstrate the usage of action-store_ture.', action='store_true')
# if action is set to store_ture, then, when the arg is used, the value of the arg will be set to
# True. If action is not set, then the value of arg will be set to False.

# If we dont set action keyword, then after -l is used, the program will expect a value input.
# If we set action keyword, then after -l is used, if another value is passed, then the program 
# will crash. In another word, action keyword determines whether a args is a switch or not.

# usage: argparse_demo.py [-h] [--verbosity VERBOSITY] [-l] echo square
# VERBOSITY means if --verbosity is used, then a input value is expected.


# The 'count' param of action:
# count the number of occurances of a specific optional arguments.
# count(-cc) = 2, count(-c) =1, count(not use) = 0.
# don't have choice keyword.
# but could be replaced with default.
parser.add_argument('-c', help='Demonstrate the usage of action-count.', action='count', default=0)


# Conflicting options
# optional args in the same conflicting group can't be used at the same time.
# usage: argparse_demo.py ... [-a | -b] ...
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

# get all the args:
args = parser.parse_args()

if args.c >= 2:
    print('2 or more -c used')
elif args.c >= 1:
    print('1 -c used')
else:
    print('-c not used.')

if args.verbosity:
    print('Verbosity turned on.')

if args.l:
    print('l turned on.')

# For positional args, it's required to get a input from terminal.
print(args.square ** 2)