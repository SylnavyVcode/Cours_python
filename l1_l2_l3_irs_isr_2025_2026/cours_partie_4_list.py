# note_1_math = 12
# note_1_pc = 13
# note_1_svt = 10
# note_1_anglais =15

# salle_classe = "12 étudiants"

# moyenne_1 = (note_1_anglais + note_1_math + note_1_pc + note_1_svt) / 4
# print("la moyenne étudiant 1 est : ", moyenne_1)

# note_2_math = 15
# note_2_pc = 14
# note_2_svt = 10
# note_2_anglais =17

# moyenne_2 = (note_2_anglais + note_2_math + note_2_pc + note_2_svt) / 4
# print("la moyenne étudiant 2 est : ", moyenne_2)

list_etudiants = [12, 13, 10, 15, 15, 14, 10, 17]
list_values = [42, "abc", 12.9, True, [14]]
# nom_var[index] : l'index est la position de l'élément
# print(list_values[0])
# print(list_values[1])
# print(list_values[2])
# print(list_values[3])
# print(list_values[4])

# print(list_values[10]) => donne une erreur
# du fait que la position est hors champ

# print(list_values[-1]) => trouve le dernier
# élément de la liste

# print(list_values[-10]) => donne une erreur
# du fait que la position est hors champ
#  
nombres = [9, 75, 4, 10, 6, 5, 3, 7]

# nom_variable[a:b]cours4_part_2_python.py
# a: c'est l'index (position) du premier élément
# à extraire

# b: c'est l'index du dernier élément à extraire 
# sans l'atteindre
print(nombres[2:5])

# nom_variable[a:b:c]
# c c'est le pas, le saut,
print(nombres[1:6:2])

maths = [14, 0, 8, 17, 6, 9, 15]
pc = []
ang = []
svt = []
eps = []
hg = []

# Trouver le  dernier élément de la liste
print("Dernier élément : ", maths[6]) # avec index position
print(maths[-1]) # avec index négatif

# Les erreurs à éviter, lorsque l'index depasse 
#  le nombre d'élément de la liste.

# print(maths[-10])
# print(maths[8])
# print(maths[-8])

# listes des méthodes de bases pour les listes
# la méthode DIR() : permet de donner la listes des 
# méthodes pré-définies pour un type de variable donné

methodes = dir(pc)
# print(methodes)
# print([methode for methode in methodes if not methode.startswith("_")])
print(type(pc))

# append : permet d'ajouter un élément dans une liste (tableau)
# structure : 
"""
    Structure:

        nom_variable.methode(paramettre)

        paramettre : en fonction des méthodes
"""
maths = [14, 0, 8, 17, 6, 9, 15]
maths.append(12)
maths.append(11)
maths.append(7)

print("la nouvelle liste : ", maths)

# extend : permet d'ajouter une liste d'éléments dans notre liste
maths.extend([10, 8, 6])

note_suivant_maths = [17, 10, 13]

maths.extend(note_suivant_maths)
print("la nouvelle liste avec ajout de extend: ", maths)

# count : permet de compter le nombre d'occurence d'une valeur
# le nombre de fois qu'une valeur se retrouve dans notre liste

print("le nombre d'occurence de 17 dans la liste maths : ", maths.count(17))

print("le nombre d'occurence de 21 dans la liste maths : ", maths.count(21))

# pop : permet de supprimer une valeur dans la liste en précisant 
# sa position (index)

print("la valeur supprimer est : ",maths.pop())
print("liste après suppression de l'élément index 1 :", maths)

# remove : permet de supprimer une valeur dans la liste en 
# précisant sa valeur 
