from collections import Counter
from .equipements import lister_equipements

def statistiques() -> dict:
    """Calcule des statistiques sur le parc d'equipements."""

    equipements = lister_equipements()

    par_type = Counter(e["type"] for e in equipements)
    par_statut = Counter(e["statut"] for e in equipements)

    return {
        "total": len(equipements),
        "par_type": dict(par_type),
        "par_statut": dict(par_statut),
    }