import tkinter as tk

def submit_name():
    name = entry_name.get()
    if name:
        label_result.config(text="Student Name: " + name)
    else:
        label_result.config(text="Please enter a name")

# Create the main window
root = tk.Tk()
root.title("Student Name Input")

# Create a label and an entry widget for the name
label_name = tk.Label(root, text="Enter Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Create a button to submit the name
submit_button = tk.Button(root, text="Submit", command=submit_name)
submit_button.pack(pady=5)

# Create a label to display the result
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()