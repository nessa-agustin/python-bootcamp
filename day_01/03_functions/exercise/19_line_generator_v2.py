"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""

def line_generator(repeat_num):
    for item in range(repeat_num):
        print('Line ', item)

# TODO: Use the function once
line_input = int(input('Enter how many lines to show: '))
line_generator(line_input)
