class EquipementReseau:
    def __init__(self, nom, ip, fabricant):
        self.nom = nom
        self.ip = ip
        self.fabricant = fabricant
    
    def ping(self):
        return f"{self.nom} ({self.ip}) repond au ping"
    
    def se_presenter(self):
        return f"Je suis {self.nom}, fabriqué par {self.fabricant}, adresse {self.ip}."

    def __str__(self):
        return f"Je suis {self.nom} et mon fabricant {self.fabricant}"
    
switch_1 = EquipementReseau("switch_1", ip="192.168.0.254", fabricant="Cisco")
print(switch_1)

class Swith(EquipementReseau):
    def __init__(self, nom, ip, fabricant, nb_ports):
        super().__init__(nom, ip, fabricant)
        self.nb_ports = nb_ports
    
    def segmenter_vlan(self, vlan_id):
        return f"{self.nom} : VLAN {vlan_id} configuré sur {self.nb_ports} ports."
    
switch_2 = Swith("switch_2", "192.168.1.254", "CISCO", 24)
print(switch_2.segmenter_vlan("142"))