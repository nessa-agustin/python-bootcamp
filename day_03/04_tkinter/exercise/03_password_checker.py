import tkinter

root = tkinter.Tk()
root.geometry('300x300')


# TODO: Add label for instructions
instruction_var = 'Enter your password:'
instruction_label = tkinter.Label(root, text=instruction_var)
instruction_label.pack()

# TODO: Add entry for instructions

entry_var = tkinter.StringVar(root, value='')
error_color = 'black'
entry = tkinter.Entry(root, textvariable=entry_var,show='*', highlightbackground=error_color, bd=3, highlightthickness=3, highlightcolor="black")
entry.pack()

# TODO: Add StringVar for instruction

message_var = tkinter.StringVar(root, value='Enter your password and press Enter')
message_label = tkinter.Label(root, textvariable=message_var)
message_label.pack()

# TODO: Add label using StringVar

def check_password(event):
    correct_password = "pass"
    entry_value = entry_var.get()

    if correct_password == entry_value:
        message_var.set('Password correct. Access granted')
    else:
        message_var.set('Incorrect password. Try again')
        entry.setvar('highlightcolor','red')



    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password

root.bind('<Return>', check_password)

root.mainloop()
