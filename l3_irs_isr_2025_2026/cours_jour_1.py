"""
je fais une documentation
"""
# alias

from random import *
# __all__ = ["methodes, variables"]

import random as rm

print(rm.__file__)

print(hasattr(rm, "__file__"))

print(rm.__name__)

print(rm)


# import gestion_parc

# print(dir(gestion_parc))

# gestion_parc.ajouter_equipement("router-01", "routeur", "192.168.1.1")
# # print(gestion_parc.equipements.lister_equipements())
# print(gestion_parc.lister_equipements())


# from gestion_parc.equipements import ajouter_equipement, lister_equipements
# ajouter_equipement("router-test", "routeur", "192.168.1.1")
# print(lister_equipements())


# from gestion_parc import *

import gestion_parc

gestion_parc.ajouter_equipement("router-01", "routeur", "192.168.1.1")
gestion_parc.ajouter_equipement("switch-01", "switch", "192.168.1.2")
gestion_parc.ajouter_equipement("srv-web", "serveur", "192.168.1.10")

# Acces direct au sous-module : modifie la MEME liste interne
gestion_parc.equipements.ajouter_equipement("srv-db", "serveur", "192.168.1.11", statut
="DOWN")

for e in gestion_parc.lister_equipements():
    print(f"{e['nom']:10} {e['type']:10} {e['ip']:15} [{e['statut']}]")
print(gestion_parc.statistiques())

import gestion_parc.reseau

# Equipement volontairement problematique, pour declencher des anomalies
gestion_parc.ajouter_equipement("capteur-iot", "capteur", "999.999.1.1", statut="DOWN")

anomalies = gestion_parc.reseau.auditer_securite()

print(anomalies)