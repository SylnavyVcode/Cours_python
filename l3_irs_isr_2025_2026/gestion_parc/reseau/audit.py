"""
Sous-module gestion_parc.reseau.audit.
Il a besoin :
- d'un module du package PARENT (gestion_parc.equipements)
=> import relatif avec ".." (remonte d'un niveau)
- d'un module qui n'appartient PAS au package, simple module
voisin du script principal
=> import ABSOLU classique
"""
from ..equipements import lister_equipements
import outils_reseau

def auditer_securite() -> list[str]:
    """
    Parcourt les equipements du parc et signale les anomalies :
    - adresse IP invalide
    - equipement dont le statut n'est pas "UP"
    """
    anomalies = []
    for e in lister_equipements():
        if not outils_reseau.valider_ip(e["ip"]):
            anomalies.append(f"IP invalide pour '{e['nom']}' : {e['ip']}")
        if e["statut"] != "UP":
            anomalies.append(f"'{e['nom']}' n'est pas UP (statut={e['statut']})")
    return anomalies