# Tuples
# c'est structure de données comme lest listes mais qui :
# est immuable : ces données ne peuvent pas être modifier
# ces éléments sont récupérer grace aux index
# voici un exemple  : (152, 50, 15)

test_tuple = (12, 14, 9, 12, 14, 0, 6)
# un tuple vide
tuple_vide = ()

print("le type de la variable test_tuple est :", type(test_tuple))

# les méthodes prédéfinies des tuples
# print(dir(test_tuple))

print("le premier élément de la liste", test_tuple[0])

# pas de modification possible pour les tuples
# test_tuple[0] = 12  # ceci engendre une erreur 
print(test_tuple)
# il y a une erreur : typeError
# c'est à cause des tuples qui sont non modifiable


# méthode count : permet de compter les occurence d'une valeur
print("l'occurence de 12 est :", test_tuple.count(12))

# méthode index : permet de trouver l'index d'une valeur dans le
# tuple
print("l'index de 9 est : ", test_tuple.index(9))

age = 12,  5
print("type de age est :", type(age))
print(age[0])
print("2e valeur:", age[1])

# dictionnaires
# dictionnaire vide
dict_test = {}

# dictionnaire avec un contenu
notes = {"maths":10, "anglais":15}

notes["maths"] = 13

print("la note de maths est :", notes["maths"])