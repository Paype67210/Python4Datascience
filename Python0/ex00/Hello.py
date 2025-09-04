# Hello.py

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modification des objets
# List est indexé
ft_list[1] = "World!"
# Tuple est immuable donc modification = remplacement
ft_tuple = (ft_tuple[0], "France!")
# set n'est pas indexé
ft_set = {"Hello", "Mulhouse!"}
# dict est un ensemble de couples clé -> valeur
ft_dict["Hello"] = "42Mulhouse!"

# Affichage
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
