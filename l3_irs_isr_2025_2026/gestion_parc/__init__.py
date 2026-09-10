from .equipements import (
    supprimer_equipement,
    rechercher_equipement, 
    ajouter_equipement, 
    lister_equipements
)

from .inventaires import statistiques
__version__ = "1.0"

__all__ = [
    "ajouter_equipement", 
    "lister_equipements",
    "rechercher_equipement", 
    "supprimer_equipement", 
    "statistiques",
]