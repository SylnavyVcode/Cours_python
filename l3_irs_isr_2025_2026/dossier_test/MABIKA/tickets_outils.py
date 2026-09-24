# Exercice 1
from sympy import li


def nettoyer_champ(valeur: str) -> str:
    """Retire les espaces superflus autour d'un champ."""
    return valeur.strip()

CHAMPS = ["date" ,"site" , "type" , "priorite" , "statut" , "duree_min"]

# Exercice 2
class TicketInvalideError(Exception):
    pass

def valider_ticket(ticket: dict) -> bool:
    """Renvoie True si le ticket est coherent, False sinon."""
    if ticket["statut"] == "resolu" or ticket["statut"] == "en_cours" and ticket["duree_min"]>=0:
        return True
    else:
        return False

# Exercice 3
def parser_ligne(ligne: str) -> dict:
    """Transforme une ligne 'date;site;type;priorite;statut;duree_min'
    en dictionnaire. Leve TicketInvalideError si la ligne est mal formee."""
    ligne = ligne.split(";")
    for index, valeur in enumerate(ligne):
        ligne[index] = nettoyer_champ(valeur)

    print("ligne", ligne)
    if len(ligne) != 6:
        raise TicketInvalideError("Le format attend 6 champs pour un ticket qui sont : 'date;site;type;priorite;statut;duree_min'")

    for valeur in ligne[:5]:
        if len(valeur) == 0:
            raise TicketInvalideError(f"Tous les champs doivent avoir une valeur")

    if not ligne[-1].isdigit():
        raise TicketInvalideError(f"La durée  minimum doit avoir que des chiffres")

    # dictonnaire[key] = valeur
    ligne[-1] = int(ligne[-1])
    resultat = {}
    for element in CHAMPS:
        resultat[element] = ligne.pop(0)

    if not valider_ticket(resultat):
        raise TicketInvalideError(f"Le ticket n'est conforme")

    return resultat

# Exercice 4
def charger_tickets(chemin) -> tuple[list[dict], list[str]]:
    """Lit le fichier, renvoie (tickets_valides, messages_d_erreur)."""
    import os
    if not os.path.exists(chemin):
        raise FileNotFoundError("Le fichier est introuvable")

    liste_valide = []
    liste_non_valide = []

    with open(chemin, mode="r", encoding="utf-8") as fichier:
        for index, ligne in enumerate(fichier.readlines()):
            try:
                valide = parser_ligne(ligne)
                liste_valide.append(valide)
            except TicketInvalideError as error:
                # "ligne <numero> : <message de l'exception>"
                non_valide = f"ligne <{index}> : <{error}>"
                liste_non_valide.append(non_valide)

    return (liste_valide, liste_non_valide)


from collections import Counter
def statistiques(tickets: list[dict]) -> dict:
    """Calcule des statistiques a partir d'une liste de tickets valides."""
    return {
       "nb_total":len(tickets),
       "nb_par_site": dict(Counter(ticket["site"] for ticket in tickets))
    }
    


if __name__ == "__main__":
    text = "      Brazzaville "
    print(repr(text))
    print(repr(nettoyer_champ(text)))
    resultat = parser_ligne("2026-09-13;Pointe-Noire;maintenance;basse;resolu;25")  
    print(resultat)
    liste_resultat = charger_tickets("MABIKA/donnees/tickets.txt")
    print(len(liste_resultat[0]),"tickets valides et", len(liste_resultat[1]),"lignes en erreur")
    stat = statistiques(liste_resultat[0])
    print(stat)