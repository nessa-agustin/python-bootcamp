# TODO: Ask the user for three values
# expense_1 = 0  # Let the user enter a number
# expense_2 = 0  # Let the user enter a number
# expense_3 = 0  # Let the user enter a number
expense_1 = int(input('Enter first expense: \n'))
expense_2 = int(input('Enter second expense: \n'))
expense_3 = int(input('Enter third expense: \n'))

# TODO: Then, print each information one line at a time10
print(expense_1)
print(expense_2)
print(expense_3)

total = expense_1 + expense_2 + expense_3
print(total)

# TODO: Format this part using f-strings
print(f'{expense_1} + {expense_2} + {expense_3} = {total}')
