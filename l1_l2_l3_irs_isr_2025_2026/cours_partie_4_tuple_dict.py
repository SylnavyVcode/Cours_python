# d'abord une introduction sur les boucles
def analyser_valeur(valeur):
    """
    Analyse le type et la valeur d'une variable.
    """

    match valeur:
        case int() if valeur > 0:
            print(f"{valeur} est un entier positif")
        case int() if valeur < 0:
            print(f"{valeur} est un entier negatif")
        case int():
            print(f"{valeur} est zero")
        case str():
            print(f"'{valeur}' est une chaine de caracteres")
        case list():
            print(f"{valeur} est une liste de {len(valeur)} elements")
        case _:
            print(f"Type non geré : {type(valeur)}")

analyser_valeur(42)
analyser_valeur(-5)
analyser_valeur("Bonjour")
analyser_valeur(0)
analyser_valeur((1, 2, 3))