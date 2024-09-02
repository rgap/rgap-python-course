# main.py

# Import only the greet function from the example_module and give it an
# alias 'say_hello'.
from example_module import greet as say_hello

# We can now call greet using its alias 'say_hello'.
print(say_hello())
