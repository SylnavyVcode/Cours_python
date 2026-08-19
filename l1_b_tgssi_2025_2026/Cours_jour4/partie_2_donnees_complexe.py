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