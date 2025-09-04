import subprocess

def run_flake8_check():
    print("\nRunning flake8 compliance check...")
    try:
        result = subprocess.run(["flake8", "sos.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Flake8 check passed: No issues found.")
        else:
            print("Flake8 check failed. Issues found:")
            print(result.stdout)
    except Exception as error:
        print(f"Flake8 check failed to execute: {error}")

def run_test(description, args=None):
    print(f"\nTest: {description}")
    try:
        result = subprocess.run(["python3", "sos.py"] + (args if args else []),
                                capture_output=True, text=True)
        print(result.stdout.strip())
        if result.stderr:
            print("Error:", result.stderr.strip())
    except Exception as error:
        print("Execution failed:", error)

def main():
    # Vérification de la conformité flake8
    run_flake8_check()
    
    # Functional tests
    run_test("Valid input with alphabetic values", ["sos"])
    run_test("Valid input with alphanumeric values ans spaces", ["Please help mi 666"])
    run_test("No arguments")
    run_test("Too many arguments", ["Hello", "extra"])
    run_test("Non-valid values", ["Hello @world"])
    
if __name__ == "__main__":
    main()

