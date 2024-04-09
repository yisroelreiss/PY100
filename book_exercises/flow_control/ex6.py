# Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def caps_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(caps_long('hello world'))
print(caps_long('goodbye'))