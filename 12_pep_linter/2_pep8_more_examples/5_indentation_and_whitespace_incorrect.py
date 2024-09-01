# This script demonstrates improper use of indentation and whitespace, violating PEP 8.
# Issues include inconsistent indentation and improper use of blank lines.

def display_message(message):
  if message:
    print(message)
  else:
    print("No message provided.")
def main():
    message="Hello, World!"
    display_message(message)
if __name__ == "__main__":main()
