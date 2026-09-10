"""Sous-module gestion_parc.equipements : stockage des equipements en memoire."""
_EQUIPEMENTS = []

def ajouter_equipement(nom: str, type_: str, ip: str, statut: str = "UP") -> None:
    """Ajoute un equipement au parc."""
    _EQUIPEMENTS.append({"nom": nom, "type": type_, "ip": ip, "statut": statut})

def lister_equipements() -> list[dict]:
    """Retourne la liste de tous les equipements."""
    return list(_EQUIPEMENTS)

def rechercher_equipement(nom: str) -> dict | None:
    """Retourne un equipement par son nom, ou None."""
    for e in _EQUIPEMENTS:
        if e["nom"] == nom:
            return e
    return None

def supprimer_equipement(nom: str) -> bool:
    """Supprime un equipement par son nom. Retourne False si absent."""
    for position, equipement in enumerate(_EQUIPEMENTS):
        if equipement["nom"] == nom:
            del _EQUIPEMENTS[position]
            return True
    return False