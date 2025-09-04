# Tester.py

import subprocess

# Liste des cas de test avec les arguments et la description attendue
test_cases = [
    (["14"], "Even number"),
    (["-5"], "Odd number"),
    (["0"], "Zero (Even)"),
    ([], "No argument"),
    (["Hi!"], "Non-integer argument"),
    (["13", "5"], "More than one argument")
]

# Exécution de chaque test
for args, description in test_cases:
    print(f"\nTest: {description}")
    try:
        result = subprocess.run(["python3", "whatis.py"] + args, capture_output=True, text=True)
        print(result.stdout.strip())
        if result.stderr:
            print("Error:", result.stderr.strip())
    except Exception as error:
        print("Execution failed:", error)
