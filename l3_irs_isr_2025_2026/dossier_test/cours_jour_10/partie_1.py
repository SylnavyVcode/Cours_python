import re

"""
    Fonction                        Rôle

    re.match(motif, texte)          cherche uniquement au début du texte
    re.search(motif, texte)         cherche n’importe où dans le texte
    re.fullmatch(motif, texte)      le texte entier doit correspondre
    re.findall(motif, texte)        liste de toutes les correspondances
    re.finditer(motif, texte)       itérateur d’objets Match (position incluse)
    re.sub(motif, remp, texte)      remplace les correspondances
    re.split(motif, texte)          découpe le texte selon le motif
    re.compile(motif)               compile un motif pour de meilleures performances
"""

texte = "Log 2024-10-10 : IP 192.168.1.50 - Code HTTP 404 - Erreur !"
match = re.search(r"HTTP\s?\d{3}", texte)
if match:
    print(f"Correspondance trouvée : {match.group()}")
    print(f"Position : {match.start()}-{match.end()}")
else:
    print("Aucune correspondance trouvée.")



text = ""
with open("Français-transcript.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.readlines()
    liste_lignes = []
    for ligne in contenu:
        ligne = ligne[7:].strip()  # Supprime les espaces en début et fin de ligne
        if ligne:  # Vérifie si la ligne n'est pas vide
            liste_lignes.append(ligne)

    text = " ".join(liste_lignes)
print(text)

# import sys
# print(sys.platform)
# print("information sur la version :", sys.version_info)
# print("version complète :", sys.version)
# print("liste des modules installés :", sys.modules.keys())
# print("liste des arguments passés au script :", sys.argv)
# print("dossiers ou python cherche les modules :", sys.path)

# import platform
# print(platform.system())
# # 'Linux', 'Windows', 'Darwin'
# print(platform.node())
# # nom de la machine (hostname)
# print(platform.release())
# # version du noyau/OS
# print(platform.machine())
# # architecture materielle
# print(platform.python_version()) # version de Python
# print(platform.python_implementation()) # 'CPython', 'PyPy'...
# print(platform.uname())

# import os
# print(os.cpu_count())
# print(os.getpid())
# print(os.getppid())
# print(os.getlogin())
# # nombre de coeurs logiques
# # PID du processus Python courant
# # PID du processus parent (ex : le shell)
# # nom d'utilisateur connecte

# import shutil
# GO = 1024 ** 3
# usage = shutil.disk_usage("/")
# print(usage.total / GO)
# # espace total en Go
# print(usage.used / GO)
# # espace utilise
# print(usage.free / GO)
# # espace libre
# pourcentage = usage.used / usage.total * 100