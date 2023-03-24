text_str = "prefer"
n = 11
avg = 5.5
ok = True

bootcamp =  ["python", "sql", "django"]

my_id = {
    "firstName": "Jules",
    "lastName": "Irenge",
    "age": 28
}

cool_langs = ("Python", "C", "Rust")

os_layers = {"Userspace", "Kernel space"}

print(text_str+": "+ str(type(text_str)))
print("{}: {}" .format(n,str(type(n))))
print("{}: {}" .format(avg,str(type(avg))))
print("{}: {}" .format(ok,str(type(ok))))
print("{}: {}" .format(bootcamp,str(type(bootcamp))))
print("{}: {}" .format(my_id,str(type(my_id))))
print("{}: {}" .format(cool_langs,str(type(cool_langs))))
print("{}: {}" .format(os_layers,str(type(os_layers))))


"""
Pseudocode
==========

Declare a string variable  text_str and store string value
Declare a variable of integer type named n  and  store an integer value
Declare a variable  of float type named avg  and assign a float value
Declare a  variable of bool type named ok and store a bool value 
Declare a variable of list type named bootcamp and assign list values to it
Declare a variable of dictionary type named my_id and assign dictionary values to it
Declare a variable of type tuple and assign a tuple value to it
Declare a variable of type set and assign set value to it

print out all the above declared variable type : stored value and type



"""


