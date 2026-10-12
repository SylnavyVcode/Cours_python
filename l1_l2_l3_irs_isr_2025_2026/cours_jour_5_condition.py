sit_mat = ""
nbre_enfant = 0

# sit_mat = input("Quel est votre situation matrimoniale? Réponse possible : Cel -> Célibataire, mar, div, veuf")
# nbre_enfant = int(input("Saisissez le nombre d'enfant que vous avez. Exemple : 0, 1, 2, 3, ..."))

match(sit_mat):
    case "Cel":
        print("Disponible")
    case "Mar":
        print("déjà occupé")
    case "Div":
        print("de nouveau libre")
    case "Veuf":
        print("Problème")
    case _:
        print("les autres cas")

# if sit_mat == "Cel" and nbre_enfant > 0 :
#     print("Disponible")
# if sit_mat == "Cel" and nbre_enfant == 0 :
#     print("Disponible")
# elif sit_mat == "Mar":
#     print("déjà occupé")
# elif sit_mat == "Div":
#     print("de nouveau libre")
# elif sit_mat == "Veuf":
#     print("Problème")
# else:
#     print("les autres cas")

div = 24/4
print(div)

div2 = 12/5
print(div2)

try:
    div3 = 10/0
    print(div3)
except ZeroDivisionError as error:
    print("VOus ne pouvez pas diviser par 0")


div4 = 4/3
print(div4)

