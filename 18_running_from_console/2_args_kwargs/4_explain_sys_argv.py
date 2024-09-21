import sys

print(f"sys.argv contains: {sys.argv}")

# `sys.argv` is a list that contains the script name and any command-line arguments passed to the script.
# sys.argv[0] is always the name of the script.
# sys.argv[1:] contains the additional arguments passed after the script name.

# This block runs when the script is executed directly.
if __name__ == "__main__":
    print(f"Script name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Arguments passed: {sys.argv[1:]}")
    else:
        print("No arguments passed.")

# How to run:
# You can run the script without arguments:
# $ python 4_explain_sys_argv.py

# Or pass additional arguments:
# $ python 4_explain_sys_argv.py 3 5 7
