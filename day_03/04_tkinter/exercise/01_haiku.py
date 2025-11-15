import tkinter

root = tkinter.Tk()
root.title('Haiku')

message = """
Loops within loops again
A silent function returns
The logic is clear
"""

label = tkinter.Label(
    root, 
    text=message,
    font=('Edwardian Script ITC', 50),
    # width=800,
    # height=800,
    bg='#ccccff',
    padx=100,
    pady=100)
label.pack()

# TODO: Show message using a label

root.mainloop()
