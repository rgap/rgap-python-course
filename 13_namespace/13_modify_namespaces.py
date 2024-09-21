# Python allows you to access and modify variables in the global and local namespaces
# using the `globals()` and `locals()` functions, which return dictionaries representing these namespaces.

x = "global variable"  # Global variable.

def modify_namespaces():
    local_var = "local variable"  # Local variable.
    
    # Access and print the global namespace.
    print("Global namespace before modification:", globals())
    
    # Modify a global variable via the `globals()` dictionary.
    globals()['x'] = "modified global variable"
    
    # Access and print the local namespace.
    print("Local namespace before modification:", locals())
    
    # Modify the local variable via the `locals()` dictionary (this change is not persistent).
    locals()['local_var'] = "modified local variable"
    
    print("Local variable after attempting modification:", local_var)  # Local variable remains unchanged.

modify_namespaces()

# The global variable 'x' has been modified.
print("Global variable after modification:", x)
