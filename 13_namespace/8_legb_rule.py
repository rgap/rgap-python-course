# Python resolves variable names following the LEGB rule, which stands for:
# 1. **Local**: Python looks first in the local namespace (the current function).
# 2. **Enclosing**: If not found locally, it checks the namespace of any enclosing functions.
# 3. **Global**: If the variable isn't found in local or enclosing scopes, Python checks the global namespace (the module level).
# 4. **Built-in**: Finally, Python looks in the built-in namespace, containing functions like `print()` and `len()`.

x = "global x"  # (3) Global variable.

def outer_function():
    x = "enclosing x"  # (2) Enclosing variable (outer function).

    def inner_function():
        x = "local x"  # (1) Local variable (inner function).
        print(x)  # Prints the local variable: 'local x' because it takes precedence (Local).

    inner_function()  # Call inner_function, which uses its local 'x'.
    print(x)  # Prints 'enclosing x' from the enclosing scope.

outer_function()  # Call to outer_function, which prints the enclosing variable 'x'.
print(x)  # Prints the global variable 'x': 'global x', since it's outside of any function.
