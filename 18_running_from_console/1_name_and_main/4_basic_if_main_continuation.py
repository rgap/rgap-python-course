# The `c_basic_if_main` module will execute any code that is not under the `if __name__ == "__main__"` block.
# Specifically, the `print("This always runs.")` line will execute because
# it's outside that conditional block.

import c_basic_if_main

# In this script, we have our own `if __name__ == "__main__"` block.
# This block will only run if this script is executed directly.
# If this script is imported into another module, this block won't run.

if __name__ == "__main__":
    print("d_basic_if_main_continuation: This runs only when the script is executed directly.")
