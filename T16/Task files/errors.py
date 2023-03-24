# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")  # Syntax Error: Missing parentheses in call to 'print'
print ("\n")   #Compilation error; incorrect space indentation, needs to be in line with the first print
             #SyntaxError: Missing parentheses in call to 'print'

ageStr = "24" #I'm 24 years old.
                         # Compilation error: IndentationError: unexpected indent,  needs to be in line with the print above
                         # Compilation error: comparison operator has to be replaced with equal sign
age = int(ageStr)  #compilation error: incorrect space indentation, needs to be in line with the ageStr
                   # syntax error : change ageStr to hold a string of the number only
print("I'm" + f" {age}" + " years old.") #compilation error: incorrect space indentation, needs to be in line with the age
                                  #Compilation error: TypeError: can only concatenate str (not "int") to st
three = "3" #compilation error: incorrect space indentation, needs to be in line with the print

answerYears = age + int(three) #Compilation error: incorrect space indentation, needs to be in line with the three
                          # Compilation error: TypeError: unsupported operand type(s) for +: 'int' and 'str'


print ("The total number of years:" + "answerYears") # SyntaxError: Missing parentheses in call to 'print'
answerMonths = answerYears * 12 # Compilation error: NameError: name 'answer' is not defined: Change answer to answerYears

print ("In 3 years and 6 months, I'll be " + f"{answerMonths + 6}"+ " months old") #SyntaxError: Missing parentheses in call to 'print'
                                                                           # Compilation error: TypeError: can only concatenate str (not "int") to str
                                                                           # Logicall error: in the answer in 3 years and 6 months one will be 330 months old, so add 6 months in the answerMonths
#HINT, 330 months is the correct answer

