#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def beam():
	print('+ - - - -', end=' ')

def post():
	print('|        ', end=' ')

def print_beam():
	do_twice(beam)
	print('+')

def print_post():
	do_twice(post)
	print('|')

def section():
	print_beam()
	do_four(print_post)

def two_by_two():
	do_twice(section)
	print_beam()

two_by_two()

def print_beam_4():
	do_four(beam)
	print('+')

def print_post_4():
	do_four(post)
	print('|')

def section_4():
	print_beam_4()
	do_four(print_post_4)

def four_by_four():
	do_four(section_4)
	print_beam_4()

four_by_four()

# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    



if __name__ == "__main__":
    main()