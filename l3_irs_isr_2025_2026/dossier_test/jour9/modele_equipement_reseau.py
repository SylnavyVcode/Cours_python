"""Module pour modéliser un équipement réseau de base, ainsi que des classes dérivées pour les switches et les routeurs."""
class EquipementReseau:
    
    """Classe représentant un équipement réseau de base.
    Attributs:
        nom (str): Le nom de l'équipement.
        ip (str): L'adresse IP de l'équipement.
        fabricant (str): Le fabricant de l'équipement.
    Méthodes:
        ping(): Simule un ping vers l'équipement.
        se_presenter(): Retourne une chaîne de caractères présentant l'équipement.
    """
    
    def __init__(self, nom, ip, fabricant):
        self.nom = nom
        self.ip = ip
        self.fabricant = fabricant
    
    def ping(self):
        # Simuler un ping vers l'équipement
        import time
        print(f"Ping vers {self.nom} ({self.ip})...")
        time.sleep(1)  # Simuler le temps de réponse
        print(f"{self.nom} répond au ping.") 
    
    def se_presenter(self):
        return f"Je suis {self.nom}, fabriqué par {self.fabricant}, et mon adresse IP est {self.ip}."
    
    def __str__(self):
        return f"EquipementReseau(nom={self.nom}, ip={self.ip}, fabricant={self.fabricant})"


class Switch(EquipementReseau):
    
    def __init__(self, nom, ip, fabricant, nombre_ports):
        super().__init__(nom, ip, fabricant)
        self.nombre_ports = nombre_ports
    
    def segmenter_vlan(self, vlan_id):
        return f"{self.nom} : VLAN {vlan_id} configure sur {self.nombre_ports} ports."
    
    def se_presenter(self):
        return f"Je suis un switch nommé {self.nom}, fabriqué par {self.fabricant}, avec {self.nombre_ports} ports, et mon adresse IP est {self.ip}."

class Routeur(EquipementReseau):
    
    def __init__(self, nom, ip, fabricant, nb_interfaces_wan):
        super().__init__(nom, ip, fabricant)
        self.nb_interfaces_wan = nb_interfaces_wan
        
    def router_paquet(self, destination_ip):
        return f"{self.nom} : Routage du paquet vers {destination_ip} via {self.nb_interfaces_wan} interfaces WAN."

    def se_presenter(self):
        return f"Je suis un routeur nommé {self.nom}, fabriqué par {self.fabricant}, avec {self.nb_interfaces_wan} interfaces WAN, et mon adresse IP est {self.ip}."
    

if __name__ == "__main__":
    # Création d'une instance de Switch
    switch_1 = Switch("Switch01", "192.168.1.1", "Cisco", 24)
    print(switch_1.se_presenter())
    print(switch_1.segmenter_vlan(10))

    # Création d'une instance de Routeur
    routeur_1 = Routeur("Routeur01", "192.168.1.2", "Juniper", 2)
    print(routeur_1.se_presenter())
    print(routeur_1.router_paquet("10.0.0.1"))
    
    switch_1.se_presenter()
    switch_1.ping()