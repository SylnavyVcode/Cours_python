"""Exercice 2 : Lecture sécurisée d'un fichier de configuration réseau"""

config_brute = {
    "port": "8080",
    "timeout": "30",
    "max_connexions": "cent"
}

def lire_parametre(config, cle, mini, maxi):
    
    # Le try Except permet d'éviter l'intéruption du programme en interception tout type d'érreur (Exceptions)
    try:
        value = int(config[cle])
        if not (mini <= value <= maxi):
            raise ValueError(f"La clé : {cle} dont la valeur : {value} doit être comprise entre {mini} et {maxi}")
        
    except KeyError:
        print(f"Erreur : la cle : '{cle}' est absente de la configuration.")
    except ValueError:
        print("Erreur : Le texte n'est pas un nombre")
    
    # Le Else ici c'est pour le cas ou il n'y a pas eu de problème dans l'exécution du code
    else:
        print(f"OK : <{cle}> = <{value}>")
        return value
    
    # Le finally est utiliser pour avoir un message global en toute circonstance (Echec ou réussite)
    finally:
        print(f"Tentative de lecture de '<{cle}>' terminée.")

print(lire_parametre(config_brute, "max_connexions", 1, 1000))