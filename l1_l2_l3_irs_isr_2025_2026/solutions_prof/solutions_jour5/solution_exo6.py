"""
Recherche d'une signature d'attaque et extraction condensée

    Contexte. 

        Un journal de connexions doit être scruté à la recherche d'une signature précise
        (par exemple un mot-clé associé à une attaque connue). Si elle n'est trouvée nulle part, il faut
        le signaler explicitement - c'est le cas d'usage typique du bloc for / else de Python.
"""

logs = [
    "10:01:02 INFO 192.168.1.5 connexion etablie",
    "10:02:15 INFO 192.168.1.9 requete traitee",
    "10:05:41 WARNING 192.168.1.5 tentative repetee",
    "10:07:03 INFO 192.168.1.12 requete traitee",
    "10:09:59 INFO 192.168.1.5 deconnexion",
]
signature_recherchee = "ERROR"

ips_warnings = []

niveaux = []

for ligne in logs:
    if signature_recherchee in ligne:
        print(f"Signature '{signature_recherchee}' detectée : {ligne}")
        break
    
    if "warning" in ligne.lower():
        ips_warnings.append(ligne.split()[2].strip())
    
    niveaux.append(ligne.split()[1])
else:
    print(f"Aucune occurence de la signature '{signature_recherchee}' dans le journal")

print("niveaux :", niveaux)
print("liste des ip avex warning", ips_warnings)