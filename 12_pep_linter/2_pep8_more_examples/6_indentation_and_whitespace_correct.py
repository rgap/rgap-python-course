# This script corrects the indentation and whitespace issues from indentation_and_whitespace_incorrect.py
# by following PEP 8 guidelines, using consistent indentation and appropriate blank lines.

def display_message(message):
    if message:
        print(message)
    else:
        print("No message provided.")


def main():
    message = "Hello, World!"
    display_message(message)


if __name__ == "__main__":
    main()
