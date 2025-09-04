import sys
import string

def count_characters(text: str) -> dict:
    """
    Count different types of characters in the given text.

    Parameters:
    text (str): The input string to analyze.

    Returns:
    dict: A dictionary with counts of uppercase, lowercase, punctuation, spaces, and digits.
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char.isdigit():
            counts["digits"] += 1

    return counts

def main():
    """
    Main function to handle input and display character counts.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            if sys.argv[1 == "--doc":
                print("Documentation de la fonction count_characters:\n")
                print(count_characters.__doc__)
                return
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.read()

        counts = count_characters(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")

if __name__ == "__main__":
    main()
