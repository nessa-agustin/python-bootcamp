import tkinter

root = tkinter.Tk()
root.geometry('300x300')

# TODO: Add label for instructions
instruction_var = 'Enter your password:'
instruction_label = tkinter.Label(root, text=instruction_var)
instruction_label.pack()

# TODO: Add entry for instructions

entry_var = tkinter.StringVar(root, value='')
entry = tkinter.Entry(root, textvariable=entry_var,show='*',highlightthickness=3, highlightcolor='gray')
entry.pack()

# TODO: Add StringVar for instruction

message_var = tkinter.StringVar(root, value='Enter your password and press Enter')
message_label = tkinter.Label(root, textvariable=message_var)
message_label.pack()

# TODO: Add label using StringVar


def check_password(event=None):
    correct_password = "pass"
    entry_value = entry_var.get()

    if correct_password == entry_value:
        message_var.set('Password correct. Access granted')
        entry.config(highlightcolor='gray')
    else:
        message_var.set('Incorrect password. Try again')
        entry.config(highlightcolor='red')



    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password

root.bind('<Return>', check_password)
# TODO: Add button that uses check_password
button = tkinter.Button(root, text='Submit', command=check_password)
button.pack()




root.mainloop()
