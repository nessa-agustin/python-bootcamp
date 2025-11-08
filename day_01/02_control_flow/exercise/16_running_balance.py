total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        # TODO: Ask for number
        # TODO: Add that number to the total
        # TODO: Print the current total
        number = int(input('Add amount: '))
        total += number
        print('Total: ', total)

    if command == "sub":
        # TODO: Ask for number
        # TODO: Add that number to the total
        # TODO: Print the current total
        number = int(input('Deduct amount: '))
        total -= number
        print('Total: ', total)

    elif command == "exit":
        running = False



#fixed or known values - for loops
#unpredictable or conditional - while loops
    # user
    # server
    # files
