
import subprocess

def run_flake8_check():
    print("\nRunning flake8 compliance check...")
    try:
        result = subprocess.run(["flake8", "filterstring.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Flake8 check passed: No issues found.")
        else:
            print("Flake8 check failed. Issues found:")
            print(result.stdout)
    except Exception as error:
        print(f"Flake8 check failed to execute: {error}")

def run_test(description, args):
    print(f"\nTest: {description}")
    try:
        result = subprocess.run(["python3", "filterstring.py"] + args, capture_output=True, text=True)
        print("Output:")
        print(result.stdout.strip())
        if result.stderr:
            print("Errors:")
            print(result.stderr.strip())
    except Exception as error:
        print(f"Execution failed: {error}")

def main():
    # Vérifications Norminette
    run_flake8_check()
    
    # Cas valides
    run_test("Phrase avec mots filtrés", ["Ceci est une démonstration de filtrage", "5"])
    run_test("Phrase sans mots assez longs", ["un mot", "10"])

    # Cas invalides
    run_test("Pas d'arguments", [])
    run_test("Un seul argument", ["Bonjour"])
    run_test("Trop d'arguments", ["Bonjour", "5", "extra"])
    run_test("Argument numérique invalide", ["Bonjour le monde", "abc"])
    run_test("Argument numérique négatif", ["Bonjour le monde", "-3"])
    run_test("Argument numérique nul", ["Bonjour le monde", "0"])
    run_test("Argument chaîne vide", ["", "3"])

if __name__ == "__main__":
    main()

