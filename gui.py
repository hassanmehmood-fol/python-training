import tkinter as tk

# create main window
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

# label
label = tk.Label(window, text="Hello Hassan!", font=("Arial", 14))
label.pack(pady=20)

# button
def say_hello():
    label.config(text="You clicked the button!")

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()

# run the app
window.mainloop()
