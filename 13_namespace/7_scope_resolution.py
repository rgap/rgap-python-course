# Python provides two useful functions, `globals()` and `locals()`, 
# which return a dictionary of the current global and local namespaces, respectively.

x = "global variable"  # Global variable.

def scope_resolution():
    local_var = "local variable"  # Local variable.

    # The `globals()` function returns the global namespace as a dictionary.
    print("Global namespace:", globals())

    print()

    # The `locals()` function returns the local namespace of the current function as a dictionary.
    print("Local namespace:", locals())

scope_resolution()

# `globals()` can also be used outside of functions to inspect the global namespace.
print()
print("Global namespace outside function:", globals())
