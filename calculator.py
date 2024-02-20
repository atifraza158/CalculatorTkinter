from tkinter import *

first_number=second_number = operator = None
def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
    
    
def clear():
    result_label.config(text='')
    
    
def get_operator(op):
    global first_number, operator
    
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')
    
def get_result():
    global first_number, second_number, operator
    
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=(first_number + second_number))
    elif operator == '-':
        result_label.config(text=(first_number - second_number))
    elif operator == '*':
        result_label.config(text=(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))
       
    


root = Tk()
root.title("Calculator")
root.geometry("290x390")
root.resizable(0, 0)
root.configure(background='black')

# Result Text
result_label = Label(root, text='', fg='white', bg='black')
result_label.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))


# Button Area....
# Button - 7
btn7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(7))
btn7.grid(column=0, row=1)
btn7.config(font=('verdana', 14, 'bold'))


# Button - 8
btn8 = Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(8))
btn8.grid(column=1, row=1)
btn8.config(font=('verdana', 14, 'bold'))


# Button - 9
btn9 = Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(9))
btn9.grid(column=2, row=1)
btn9.config(font=('verdana', 14, 'bold'))


# Button - +
btn_plus = Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2,command =lambda: get_operator("+"))
btn_plus.grid(column=3, row=1)
btn_plus.config(font=('verdana', 14, 'bold'))



# Button - 4
btn4 = Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(4))
btn4.grid(column=0, row=2)
btn4.config(font=('verdana', 14, 'bold'))


# Button - 5
btn5 = Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(5))
btn5.grid(column=1, row=2)
btn5.config(font=('verdana', 14, 'bold'))


# Button - 6
btn6 = Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(6))
btn6.grid(column=2, row=2)
btn6.config(font=('verdana', 14, 'bold'))


# Button - -
btn_minus = Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2,command =lambda: get_operator("-"))
btn_minus.grid(column=3, row=2)
btn_minus.config(font=('verdana', 14, 'bold'))





# Button - 1
btn1 = Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(1))
btn1.grid(column=0, row=3)
btn1.config(font=('verdana', 14, 'bold'))


# Button - 2
btn2 = Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(2))
btn2.grid(column=1, row=3)
btn2.config(font=('verdana', 14, 'bold'))


# Button - 3
btn3 = Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(3))
btn3.grid(column=2, row=3)
btn3.config(font=('verdana', 14, 'bold'))


# Button - *
btn_multi = Button(root, text='*', bg='#00a65a', fg='white', width=5, height=2,command =lambda: get_operator("*"))
btn_multi.grid(column=3, row=3)
btn_multi.config(font=('verdana', 14, 'bold'))







# Button - clr
btn_clr = Button(root, text='C', bg='#00a65a', fg='white', width=5, height=2, command=lambda: clear())
btn_clr.grid(column=0, row=4)
btn_clr.config(font=('verdana', 14, 'bold'))


# Button - 0
btn0 = Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(0))
btn0.grid(column=1, row=4)
btn0.config(font=('verdana', 14, 'bold'))


# Button - equals
btn_equals = Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2, command= lambda: get_result())
btn_equals.grid(column=2, row=4)
btn_equals.config(font=('verdana', 14, 'bold'))


# Button - /
btn_div = Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2,command =lambda: get_operator("/"))
btn_div.grid(column=3, row=4)
btn_div.config(font=('verdana', 14, 'bold'))





root.mainloop()