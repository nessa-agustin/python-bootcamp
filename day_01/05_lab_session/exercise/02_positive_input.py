# TODO: Ask the user for an input that should be a number

# TODO: Then try to convert this into an integer using the following:
# number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case
running = True
while running:
    number = input("Enter number: ")
    try:
        number_converted = int(number)
        if number_converted < 1:
            raise ValueError
        running = False
    except ValueError:
        print('Invalid entry')
        retry_mode = input('Retry? y/n: ')
        if retry_mode != 'y':
            running = False


# Challenge: TODO: Give the user infinite times to retry


