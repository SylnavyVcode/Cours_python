"""
Synthèse : pare-feu anti brute-force avec supervision

    Contexte. 
        Ce dernier exercice combine toutes les notions du jour : une fonction protège un
        service contre les attaques par force brute (comme le fait un outil tel que fail2ban ), en gérant
        à la fois des tentatives mal formées (erreurs de journalisation) et un nombre maximal d'échecs,
        puis un match / case interprète le résultat pour chaque adresse IP.
"""

# jeu d'essai 
connexions_brutes = {
    "192.168.1.10": ["Motdepasse1", " SuperSecret123 ", "azerty"],
    "192.168.1.20": ["azerty", 123456, "password", "qwerty"],
}
mot_de_passe_correct = "supersecret123"
import time
def tenter_connexion(ip, tentatives, mot_de_passe_correct, max_echecs=3):
    echecs = 0
    index = 0
    while index < len(tentatives) and echecs < max_echecs:
        time.sleep(1)
        tentative = tentatives[index]
        index += 1
        try:
            tentative = tentative.strip().lower()
        # L'erreur AttributeError est générée dans le cas ou on veux appliquer 
        # les méthodes d'une chaine de caractère aux valeurs numériques
        except AttributeError:
            print(f"Tentative ignorée (forme invalide : {tentative!r})")
            continue
        
        if tentative == mot_de_passe_correct:
            print(f"Connexion réussie pour {ip}.")
            return "Connectée"
        else:
            echecs += 1
            print(f"Echec {echecs}/{max_echecs} pour {ip}.")
    
    if echecs >= max_echecs:
        print(f"IP {ip} BLOQUÉE.")
        return "Bloquée"
    else:
        return "inconnue"
    

for ip, tentatives in connexions_brutes.items():
    print(f" - - - {ip} - - - ")
    
    resultat = tenter_connexion(ip, tentatives, mot_de_passe_correct)
    
    match(resultat):
        case "Connectée":
            print("Statut final : acces autorise.")
        case "Bloquée":
            print("Statut final : IP bloquee, alerte generee.")
        case _:
            print("Statut final : tentatives insuffisantes pour conclure.")
    