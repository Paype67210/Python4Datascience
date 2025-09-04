from new_student import Student

# Test normal
print("Test normal :")
student = Student(name="Philippe", surname="aype")
print(student)

# Test d'erreur : tentative d'initialisation de `id`
print("\nTest d'erreur : tentative d'initialisation de `id`")
try:
    student = Student(name="Philippe", surname="aype", id="toto")
except TypeError as error:
    print("Erreur attendue :", error)
