# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion" # Compilation error: NameError: name 'Lion' is not defined, it should be in double quotation mark
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" # logical error: add f 

print (full_spec) # SyntaxError: Missing parentheses in call to 'print'.

