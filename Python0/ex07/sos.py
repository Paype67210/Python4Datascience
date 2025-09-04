import sys

# Dictionary for Morse code
NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}

def encode_to_morse(input_string: str) -> str:
    """
    Encodes a given string into Morse code using a predefined dictionary.

    Args:
        input_string (str): The string to be encoded into Morse code.

    Returns:
        str: The Morse code representation of the input string.
    """
    morse_code = []
    for char in input_string.upper():
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
        else:
            raise AssertionError("the arguments are bad")
    return ''.join(morse_code).strip()

def main():
    """
    Main function to handle command line arguments and execute the encoding process.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    input_string = sys.argv[1]
    try:
        morse_result = encode_to_morse(input_string)
        print(morse_result)
    except AssertionError as error:
        print("AssertionError: ", error)

if __name__ == "__main__":
    main()
