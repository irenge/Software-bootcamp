def print_values_of(dictionary, keys):
    for key in keys:
        # change k into key to iterate through the dictionary values
        print(dictionary[key])

# put "d'oh" on double quotation mark to remove "SyntaxError: unterminated string literal" and add ! to match the output below 
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!", "maggie": " (Pacifier Suck)"}
# as the function take two arguments: we make second argument as a list of those names to remove "TypeError: print_values_of() takes 2 positional arguments but 4 were given"
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

