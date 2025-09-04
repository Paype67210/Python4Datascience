# Tester.py

import subprocess

def run_flake8_check():
    print("\nRunning flake8 compliance check...")
    try:
        result = subprocess.run(["flake8", "building.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Flake8 check passed: No issues found.")
        else:
            print("Flake8 check failed. Issues found:")
            print(result.stdout)
    except Exception as error:
        print(f"Flake8 check failed to execute: {error}")

def run_test(description, args=None, input_text=None):
    print(f"\nTest: {description}")
    try:
        if args:
            result = subprocess.run(["python3", "building.py"] + args, capture_output=True, text=True)
        else:
            result = subprocess.run(["python3", "building.py"], input=input_text, capture_output=True, text=True)
        print(result.stdout.strip())
        if result.stderr:
            print("Error:", result.stderr.strip())
    except Exception as error:
        print("Execution failed:", error)

def main():
    # Vérifications Norminette
    run_flake8_check()

    # Vérification de la documentation de la fontcion
    run_test("Valid DocString", args=["--doc"])
    
    # Test avec un argument valide
    run_test("Valid string argument", args=["Hello World!"])

    # Test sans argument (entrée utilisateur)
    run_test("No argument, user input", input_text="Hello World!\n")

    # Test avec trop d'arguments
    run_test("Too many arguments", args=["Hello", "World"])

    # Test avec un paragraphe complexe
    paragraph = (
        "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible "
        "with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
    )
    run_test("Complex paragraph", args=[paragraph])

if __name__ == "__main__":
    main()

