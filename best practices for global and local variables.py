## Best practices for global and local variables
## When working with variables and functions, it is very important to make sure that you only use a certain
## variable name once, even if one is defined globally and the other is defined locally. 

username = "elarson"
def identify_user():
    print(username)
identify_user()



## Best practices for global and local variables
## Reuse the name of a global variable within a function, it will create a new local variable with that name.
## In other words, there will be both a global variable with that name and a local variable with that name, and
## they'll have different values.

username = "elarson"
print("1:" + username)
def greet():
    username = "bmoreno"
    print("2:" + username)
greet()
print("3:" + username)