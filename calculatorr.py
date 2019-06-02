### calculator

import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("calculator")

first_num_label = tk.Label(mainWindow, text="enter the first num")
first_num_label.pack()

first_num_entry = tk.Entry(mainWindow)
first_num_entry.pack()

second_num_label = tk.Label(mainWindow, text="enter the second num")
second_num_label.pack()

second_num_entry = tk.Entry(mainWindow)
second_num_entry.pack()

operation_label = tk.Label(mainWindow, text="operation")
operation_label.pack()

operation_entry = tk.Entry(mainWindow)
operation_entry.pack()

add_button = tk.Button(mainWindow, text="+", pady=(5), padx(10),
                       command=lambda:addition())
add_button.pack()

sub_button = tk.Button(mainWindow, text="-", pady=(5), padx(10),
                       command=lambda:subtraction())
sub_button.pack()

mul_button = tk.Button(mainWindow, text="*", pady=(5), padx(10),
                       command=lambda:multiplication())
mul_button.pack()

div_button = tk.Button(mainWindow, text="/", pady=(5), padx(10),
                       command=lambda:division())
div_button.pack()

result_label = tk.Label(mainWindow, text="operation result is:", pady(20),padx(20))
result_label.pack()


def addition():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first+second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def multiplication():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first * second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def subtraction():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first - second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def division():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first / second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))

mainWindow.mainloop()
### calculator

import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("calculator")

first_num_label = tk.Label(mainWindow, text="enter the first num")
first_num_label.pack()

first_num_entry = tk.Entry(mainWindow)
first_num_entry.pack()

second_num_label = tk.Label(mainWindow, text="enter the second num")
second_num_label.pack()

second_num_entry = tk.Entry(mainWindow)
second_num_entry.pack()

operation_label = tk.Label(mainWindow, text="operation")
operation_label.pack()

operation_entry = tk.Entry(mainWindow)
operation_entry.pack()

add_button = tk.Button(mainWindow, text="+", pady=(5), padx(10),
                       command=lambda:addition())
add_button.pack()

sub_button = tk.Button(mainWindow, text="-", pady=(5), padx(10),
                       command=lambda:subtraction())
sub_button.pack()

mul_button = tk.Button(mainWindow, text="*", pady=(5), padx(10),
                       command=lambda:multiplication())
mul_button.pack()

div_button = tk.Button(mainWindow, text="/", pady=(5), padx(10),
                       command=lambda:division())
div_button.pack()

result_label = tk.Label(mainWindow, text="operation result is:", pady(20),padx(20))
result_label.pack()


def addition():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first+second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def multiplication():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first * second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def subtraction():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first - second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))
def division():
    first = int(name_field2.get())
    second = int(name_field3.get())
    result = first / second
    # print("the result is:",result)
    result_label.config(text="operation result is:" + str(result))

mainWindow.mainloop()
