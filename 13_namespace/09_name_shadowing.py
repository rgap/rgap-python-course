# Name shadowing occurs when a local variable in a function has the same name as a global variable.
# In this case, the local variable shadows or overrides the global variable inside the function.

x = "global x"  # Global variable.

def shadowing_example():
    x = "local x"  # Local variable, which shadows the global variable within this function.
    print(x)  # Outputs 'local x' because the local variable takes precedence.

shadowing_example()
print(x)  # Outputs 'global x' because the global variable is unaffected outside the function.
