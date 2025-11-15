# test1 = {
#     'ph' : 'philippines',
#     'au' : 'australia'
# }

# for x in test1:
#     print



import tkinter

root = tkinter.Tk()
root.geometry('300x300')

entry = tkinter.Entry(root)
entry.pack()

def show_input(event):
    given_text = entry.get()
    print(given_text)

root.bind('<Return>', show_input)

root.mainloop()