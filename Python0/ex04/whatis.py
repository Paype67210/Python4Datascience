# Whatis.py

import sys

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided" if len(sys.argv) > 2 else "argument is not an integer")
        arg = sys.argv[1]
        if not arg.lstrip('-').isdigit():
            raise AssertionError("argument is not an integer")
        number = int(arg)
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()
