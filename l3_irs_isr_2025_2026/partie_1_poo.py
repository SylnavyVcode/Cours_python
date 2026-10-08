class Voiture:
    """
    Classe representant une voiture.
    La docstring decrit ce que fait la classe.
    """
    # attribut de classe
    Nombre_voiture = 0
    # __init__ est le CONSTRUCTEUR : il s'execute automatiquement
    # quand on cree un objet. "self" represente l'objet lui-meme.
    def __init__(self, marque_voiture, modele_voiture, annee_voiture, couleur_voiture):
    # Ces attributs appartiennent a CHAQUE instance (objet)
        self.marque = marque_voiture
        self.modele = modele_voiture
        self.annee = annee_voiture
        self.couleur = couleur_voiture
        
        Voiture.Nombre_voiture  = Voiture.Nombre_voiture + 1
    
    def demarrer(self):
        return f"La voiture {self.marque} {self.modele} demarre."
    
    def __str__(self):
        return f"La voiture {self.marque} {self.modele} de couleur {self.couleur}."

# voiture_1 = Voiture("Peugeot", "208", 2020, "Rouge")
# print(Voiture.Nombre_voiture)
# voiture_2 = Voiture("Renault", "Clio", 2021, "Bleu")
# print(Voiture.Nombre_voiture)
# # # print(dir(voiture_1))
# # print(voiture_1.annee)
# # print(voiture_1)

# # print(voiture_2)
# # voiture_3 = ""
# # print(isinstance(voiture_2, Voiture))  # True

# # print(type(voiture_1))


# print(Voiture.Nombre_voiture)
# print(voiture_2.marque)

# print(voiture_1.Nombre_voiture)
# print(voiture_2.Nombre_voiture)

class Vehicule:
    
    def __init__(self, type, nom, nombre_roue):
        self.nom = nom
        self.type = type
        self.nombre_roue = nombre_roue

class Moto_2(Vehicule):
    
    def __init__(self, type, nom, nombre_roue):
        super().__init__()
        