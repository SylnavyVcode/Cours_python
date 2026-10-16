"""
Génération d'un plan d'adressage VLAN

    Contexte. 
        Vous devez générer automatiquement un plan d'adressage IP pour plusieurs VLAN,
        chacun avec ses premières adresses hôtes, sans rien écrire " en dur " : tout doit être calculé à
        partir de quelques paramètres, à l'aide de boucles imbriquées et de range().
"""

vlan_debut = 10
nb_vlans = 3
pas_vlan = 10
hotes_par_vlan = 3

vlan_ids = range(vlan_debut, vlan_debut + nb_vlans * pas_vlan, pas_vlan)

liste_vlan_ids = list(vlan_ids)

print(liste_vlan_ids)

for vlan_id in vlan_ids:
    print(f"VLAN {vlan_id} :")

    for h in range(1, hotes_par_vlan+1):
        print(f"    192.168.{vlan_id}.{h}")