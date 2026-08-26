"""
notes = [15, 7, 9, 12, 13, 6, 8, 9, 14, 14, 12]
# Une liste est ordonnée
# UNe liste est indexable
# Une liste est mutable
# La première valeur d'une liste est à l'index 0

# nom_var[position]
print(notes[3])

# nom_var[a:b]
# a c'est la position (index) de debut
# b c'est la position de fin (on recuperer l'élément à l'index b-1)
print(notes[2:6])

# nom_var[a:b:c]
print(notes[1:8:2])
print(notes[1:8:3])

print(notes[-1])
print(notes[-2])
print(notes[-3])
print(notes[-4])
print(notes[-11])

# print(notes[-12]) : renvois une erreurs car l'index est hors champs

print(sorted(notes))

# print(notes)
print(notes)
print(notes[::-1])
print(notes[::-2])

# print(dir(notes))

# x = dir("")
# print([a for a in x if not a.startswith("_")])
# print(dir(notes))
list_met = dir(notes)

print([a for a in list_met if not a.startswith("_")])

# nom_variable.methode()
print(notes.count(12)) # le nombre de fois qu'on a 12 dans la liste

print(notes.count(16))

# append : permet d'ajouter un élément dans la liste

notes.append(16) # on ajoute 16 dans la lite

# extend : permet d'ajouter une liste de valeur

notes.extend([20, 13, 14])
print(notes)

# sort : permet de trier les valeurs

notes.sort(reverse=True)
# reverse = True : c'est du plus grand au plus petit
print(notes)


notes.sort()
# reverse = False : du plus petit au plus grand
# si l'on ne precise pas le reverse, la liste sera trié du plus petit au plus grand
print(notes)

print("je trie ===>", notes.sort())

"""
# 26 Aout 2026

notes = [15, 7, 9, 12, 13, 6, 8, 9, 14, [14, 15, 10, [14, 0, 0.5]], 14, 12]

notes_copie = notes # Mauvaise copie

notes_copie_2 = notes.copy() # une meilleure copie
notes_copie.append(8)
# print(notes_copie)

print(notes[9][3])
notes_copie_2[9][3].append(2)
print("liste apres copie de la liste notes avec .copy()", notes_copie_2)
print("La liste notes", notes)

# ==== Attention à la méthode copy() quand nous avons une liste avec des 
# listes (Listes profondes)


notes = [15, 7, 9, 12, 13, 6, 8, 9, 14, 14, 12]
# sorted() ==> structure : sorted(nom_variable)
# sort() ==> structure : nom_variable.sort()

notes1 = sorted(notes)
# il faut faire une affectation du trie pour voir le trie.
print("Liste notes : ", notes1)

# notes.sort(reverse=True)
# print("notes2 triée :", notes)

# print(notes)
# notes.reverse()
# Reverse() : permet de renverser la liste (le dernier élément devient le premier)
# et vice-versa sur la liste de depart

# print(notes)

# notes.clear()
# clear(): permet de vider la liste : supprimer toutes les valeurs de la liste
# la liste devient vide : []
print(notes)

# count() : permet de compter le nombre d'occurence d'une valeur
print("le nombre de fois qu'on a 14 dans la liste est :", notes.count(14))

# index(): permet de retrouver l'index (la position) d'une valeur dans la liste
print(notes.index(14))

# retrouver la taille de la liste (le nombre d'élement de la liste),
#  on utilise la méthode : len()
print(len(notes))

notes.insert(2, 11)

print(notes)

# La suppression :
"""
    On a :
    La méthode : pop
    structure:
        nom_var.pop(index)
        index : c'est la position ou l'index de l'élément à supprimer
        si nom_var.pop() : il supprime le dernier élément de la liste

    La méthode : remove
    structure:
        nom_var.remove(valeur)
        valeur : c'est l'élément que l'on veut supprimer
"""

print("ON supprimer le dernier élément qui est : ", notes.pop())
print("ON supprimer l'élément à la position 9 qui est : ",notes.pop(9))
print("la nouvelle liste :", notes)
