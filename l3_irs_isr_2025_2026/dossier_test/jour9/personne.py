class Personne:
    def __init__(self, nom, age, salaire, numero_secret):
        self.nom = nom
        # PUBLIC
        self._age = age
        # PROTEGE (convention)
        self.__salaire = salaire
        # PRIVE (name mangling)
        self.__numero_secret = numero_secret
        # PRIVE
        
    def se_presenter(self):
        print(f"Nom : {self.nom} | Age : {self._age} | Salaire : {self.__salaire} FCFA"
        )
    def get_salaire(self):
        return self.__salaire
        # acces controle via methode
        
    def set_salaire(self, nouveau_salaire):
        if nouveau_salaire > 0:
            self.__salaire = nouveau_salaire
        else:
            print("Le salaire doit etre positif.")

p = Personne("Kenny", 25, 350000, "ABC123")
print("nom", p.nom)
print("age", p._age)
# acces public : fonctionne
# acces protege : possible mais DECONSEILLE
try:
    print("salaire test", p.__salaire)
    # acces prive DIRECT : erreur !
except AttributeError as e:
    print(f"Erreur : {e}")
    print("salaire", p.get_salaire())
    p.set_salaire(400000)
    p.set_salaire(-5000)
    # acces prive via methode : correct
    # refuse par la validation
    # Name mangling : Python renomme __salaire en _Personne__salaire en interne
print("Attributs et méthodes de l'objet p :", dir(p))
print("Numéro secret", p._Personne__numero_secret)