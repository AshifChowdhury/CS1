# COMMENTS: In Python, a single-line comment starts with the pound
# sign

'''Multiline comments are surrounded  by triple single quotes or triple double quotes.'''

#DIFFERENCES

'''Key differences, Idris vs Python

(1) Idris is a complied language; Python is interpreted (by default)
(2) Idris uses static type checking; Python uses dynamic type checking 
(3) Idris values are immutable wheres Python has mutable state
(4) Idris is a language of expressions; Python is a language of commands
'''

def foo(n):
    return n + 3

print(foo(6))

print(print("Happy 200th Birthday, George Boole!"))

print(None)

x = 5
#{(x,5)}

print(x)
#{(x,5)}

x = 6
# {(x,6)}

print(x)
#{(x,6)}

y = 7
#{(x,6), (y,7)}

print(y)
#{(x,6),(y,7)}
