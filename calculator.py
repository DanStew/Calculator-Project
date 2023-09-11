import tkinter as tk

#Initialising calculation in the program
calculation = ""

#Function used to add a symbol to the calculation
def add_to_calculation(symbol):
    #Making the calculation variable global
    global calculation

    #Adding the symbol to the calculation
    #str is used so even integers can be successfully added to calculation
    calculation += str(symbol)

    #Deleting the current content of the text_result field
    #(1.0,"end") is how you delete all information from the field
    text_result.delete(1.0,"end")

    #Adding the calculation to the text result field
    text_result.insert(1.0, calculation)


#Function used to work out the result of the calculation
def evaluate_calculation():
    global calculation
    #Try is used in case an error occurs in calculation (ie /0)
    try:
        #Uses the eval function to evaluate the calculation
        #Note : the eval function can also evaluate python code
        #See readMe for more details
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)  
    except:
        clear_field()
        text_result.insert(1.0,"Error")

#Function to reset the calculation (upon error)
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

#Building the GUI
#This makes and defines the dimensions of the GUI
root = tk.Tk()
root.geometry("300x275")

#Making the text field for the result
text_result = tk.Text(root, height = 2, width = 16, font=("Arial",24))
#This defines how many columns wide the field will take up
text_result.grid(columnspan=5)

#Creating the buttons for the app
#Note, if lambda isn't implemented, the functions will run as soon as seen in code, not when function is actually called
#Lambda allows you to get around this
#Similar to callback functions needing to be used in event listeners in Javascript
btn_0 = tk.Button(root,text="0",command= lambda: add_to_calculation(0), width=5, font=("Arial",14))
btn_1 = tk.Button(root,text="1",command= lambda: add_to_calculation(1), width=5, font=("Arial",14))
btn_2 = tk.Button(root,text="2",command= lambda: add_to_calculation(2), width=5, font=("Arial",14))
btn_3 = tk.Button(root,text="3",command= lambda: add_to_calculation(3), width=5, font=("Arial",14))
btn_4 = tk.Button(root,text="4",command= lambda: add_to_calculation(4), width=5, font=("Arial",14))
btn_5 = tk.Button(root,text="5",command= lambda: add_to_calculation(5), width=5, font=("Arial",14))
btn_6 = tk.Button(root,text="6",command= lambda: add_to_calculation(6), width=5, font=("Arial",14))
btn_7 = tk.Button(root,text="7",command= lambda: add_to_calculation(7), width=5, font=("Arial",14))
btn_8 = tk.Button(root,text="8",command= lambda: add_to_calculation(8), width=5, font=("Arial",14))
btn_9 = tk.Button(root,text="9",command= lambda: add_to_calculation(9), width=5, font=("Arial",14))

#Creating the function buttons
btn_addition = tk.Button(root, text="+", command= lambda: add_to_calculation("+"), width=5, font=("Arial,14"))
btn_subtract = tk.Button(root, text="-", command= lambda: add_to_calculation("-"), width=5, font=("Arial,14"))
btn_multiply = tk.Button(root, text="x", command= lambda: add_to_calculation("*"), width=5, font=("Arial,14"))
btn_divide = tk.Button(root, text="/", command= lambda: add_to_calculation("/"), width=5, font=("Arial,14"))
btn_equals = tk.Button(root, text="=", command= lambda: evaluate_calculation(), width=5, font=("Arial,14"))
btn_openBracket = tk.Button(root, text="(", command= lambda: add_to_calculation("("), width=5, font=("Arial,14"))
btn_closeBracket = tk.Button(root, text=")", command= lambda: add_to_calculation(")"), width=5, font=("Arial,14"))

#Positioning the buttons on the grid
btn_0.grid(row=5,column=1)
btn_1.grid(row=2,column=1)
btn_2.grid(row=2,column=2)
btn_3.grid(row=2,column=3)
btn_4.grid(row=3,column=1)
btn_5.grid(row=3,column=2)
btn_6.grid(row=3,column=3)
btn_7.grid(row=4,column=1)
btn_8.grid(row=4,column=2)
btn_9.grid(row=4,column=3)

#Positioning function buttons
btn_addition.grid(row=2,column=4)
btn_subtract.grid(row=3,column=4)
btn_multiply.grid(row=4,column=4)
btn_divide.grid(row=5,column=4)
btn_openBracket.grid(row=5,column=2)
btn_closeBracket.grid(row=5,column=3)
btn_equals.grid(row=6,columnspan=5)


#Mainloop infinitely runs the application, waits for an event to occur, and then runs said event
root.mainloop()