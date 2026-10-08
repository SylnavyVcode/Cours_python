from modele_equipement_reseau import EquipementReseau

print(EquipementReseau.__doc__)

class Surveillable(EquipementReseau):
    """ 
    Classe représentant un équipement réseau qui peut être surveillé.
    """
    
    def __init__(self, nom, ip, fabricant):
        super().__init__(nom, ip, fabricant)
        
    def superviser(self):
        """Méthode pour superviser l'équipement réseau."""
        return f"Supervision de {self.nom} : statut OK."

# class Configurable