stock = ["cable-rj45", "switch-8ports", "routeur-wifi", "cable-rj45",
"point-acces", "switch-8ports", "cable-rj45"]

print("Le stock de départ est : ", stock)

print("le nombre d'article en stock :", len(stock))
# Ajout de l'article "pare-feu"
stock.append("pare-feu")

# Trouver la position de l'article "switch-8ports"
position = stock.index("switch-8ports")
print("position du switch-8ports", position)

# insertion de l'article defectueux ("switch-8ports-defectueux")
stock.insert(position, "switch-8ports-defectueux")

# Ajout de plusieurs articles en une fois
stock.extend(["baie-brassage","onduleur", "cable-fibre"])

# vente puis Suppression d'un cable rj-45 dans le stock
# avec POP il faut préciser la position ou l'index
# de l'élément que l'on veux supprimer
# stock.pop(0)

# avec REMOVE il faut préciser l'élément que l'on
# veut supprimer
stock.remove("cable-rj45")

# Le nombre d'article cable-rj45 restant
print("nombre d'article cable-rj45 :", stock.count("cable-rj45"))

# suppression du dernier élément du stock
dernier_element_supprime = stock.pop()
print("Le dernier élément supprimer est :", dernier_element_supprime)

# Trier la liste de stock
stock.sort()

# Faire copie
copie_stock = stock.copy()
copie_stock_2 = stock


copie_stock.remove("switch-8ports-defectueux")

copie_stock_2.remove("switch-8ports-defectueux")
print("stock propre", stock)
print("stock copié", copie_stock)

print(len(stock))