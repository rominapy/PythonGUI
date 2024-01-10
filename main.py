"""
This script is a simple unit converter application using tkinter for the GUI.
"""


# Import necessary modules
import customtkinter 
from tkinter import *
from tkinter import messagebox


# Create the application window
app =  customtkinter.CTk()
app.title('Unit Converter') # Set the title of the window
app.geometry('500x450')  # Set the size of the window
app.config(bg = '#020a24')  # Set the background color of the window

# Define the fonts to be used in the application
font1 = ('Comic Sans MS', 30 , 'bold')
font2 = ('Comic Sans MS', 25 , 'bold')
font3 = ('Comic Sans MS', 15 , 'bold')

# Define the options for the units
unit_options =['Length', 'Mass']
length_options =['Meter', 'Centimeter', 'Foot']
mass_options = ['Kilogram' , 'Gram', 'Pound']


# Define the variables to hold the selected options and the value to be converted
variable1 = StringVar()
variable1= StringVar()
variable2= StringVar()
variable3= StringVar()

def convert():
    """
    This function converts the value from one unit to another.
    It uses the conversion factors for length and mass units.
    """   
    length_factors={ 'Meter':1, 'Centimeter': 0.01,'Foot':0.3048}
    mass_factors= {'Kilogram':1, 'Gram':0.001, 'Pound':0.45359}

    try: 
        if variable1.get()== 'Length':
            meters= float(value_entry.get())* length_factors[variable2.get()]
            #from meter to the desired unit
            converted_value = meters/ length_factors[variable3.get()]
        else:
            kilograms = float(value_entry.get())* mass_factors[variable2.get()]
            converted_value= kilograms / mass_factors[variable3.get()]
        result_label.configure(text=f'{value_entry.get()} {variable2.get()} = {converted_value: .2f} {variable3.get()}')
    except:
        messagebox.showerror("Error","Enter valid values!!")


def clear_fields():
    """
    This function clears the input fields.
    """
    value_entry.delete(0, END)
    result_label.configure(text='')



# Create and place the labels, options, and buttons on the window
title_label = customtkinter.CTkLabel(app, font=font1, text='Unit Converter', text_color='#fff', bg_color='#020a24')
title_label.place(x=150, y=20)

unit_label = customtkinter.CTkLabel(app, font=font2, text='Unit', text_color='#fff', bg_color='#020a24')
unit_label.place(x=180, y=90)

unit_option = customtkinter.CTkComboBox(app, font=font3,
                                        text_color='#000',
                                        fg_color='#fff',
                                        dropdown_hover_color='#06911f',
                                        values=unit_options,
                                        variable=variable1,
                                        width=120)
unit_option.place(x=180, y=130)

from_label = customtkinter.CTkLabel(app, font=font2, text='From', text_color="#fff", bg_color='#020a24')
from_label.place(x=20, y=170)

from_option = customtkinter.CTkComboBox(app, font=font3,
                                         text_color='#000',
                                         fg_color='#fff',
                                         dropdown_hover_color='#06911f',
                                         variable=variable2,
                                         width=120)
from_option.place(x=20, y=210)

to_label = customtkinter.CTkLabel(app, font=font2, text='To', text_color="#fff", bg_color='#020a24')
to_label.place(x=180, y=170)

to_option = customtkinter.CTkComboBox(app, font=font3,
                                       text_color='#000',
                                       fg_color='#fff',
                                       dropdown_hover_color='#06911f',
                                       variable=variable3,
                                       width=120)
to_option.place(x=180, y=210)

value_label = customtkinter.CTkLabel(app, text='Value', font=font1, text_color="#fff", bg_color='#020a24')
value_label.place(x=340, y=170)

value_entry = customtkinter.CTkEntry(app, font=font3, text_color='#000', fg_color='#fff', bg_color="#fff", width=150)
value_entry.place(x=340, y=210)

convert_button = customtkinter.CTkButton(app, command=convert, font=font2, text_color="#fff", text='Convert',
                                          fg_color='green', hover_color='#a8057d', bg_color='#020a24', cursor='hand2',
                                          corner_radius=10, width=200)
convert_button.place(x=150, y=280)

result_label = customtkinter.CTkLabel(app, text='', font=font2, text_color='#fff', bg_color='#020a24')
result_label.place(x=70, y=380)

clear_button = customtkinter.CTkButton(app, command=clear_fields, font=font2, text_color="#fff", text='Clear',
                                        fg_color='red', hover_color='#a8057d', bg_color='#020a24', cursor='hand2',
                                        corner_radius=10, width=200)
clear_button.place(x=150, y=330)

def update_options(*args):
    if variable1.get() == 'Length':
        from_option.configure(values=length_options)
        to_option.configure(values=length_options)
        # default values:
        from_option.set('Meter')
        to_option.set('Centimeter')
    else:
        from_option.configure(values=mass_options)
        to_option.configure(values=mass_options)
        from_option.set('Kilogram')
        to_option.set('Gram')

variable1.trace('w', update_options)

app.mainloop()