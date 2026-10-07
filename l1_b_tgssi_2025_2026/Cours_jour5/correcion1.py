situation_mat = ""

if situation_mat == "célibataire":
    print("vous êtes toujours célibataire ?")
elif situation_mat == "Marié":
    print("vous êtes déjà marié")
elif situation_mat == "veuf":
    print("veuf trop tot")
elif situation_mat == "divorcé":
    print("ce n'est pas bien de divorcé")
else:
    print("vous êtes dans quel cas ?")
    

match(situation_mat):
    case "célibataire":
        print("vous êtes toujours célibataire ?")
        
    case "Marié":
        print("vous êtes déjà marié")
        
    case "veuf":
        print("veuf trop tot")
        
    case "divorcé":
        print("ce n'est pas bien de divorcé")
        
    case _:
        print("autres cas")

"""
case int() if gravite >= 1 and gravite <= 5 : la gravité est valide, poursuivez
avec les étapes 2 à 4 à l'intérieur de ce cas.
 case int() (un entier, mais hors de 1-5) : affichez "Alerte ignoree : gravite
<gravite> hors plage (1-5)".
 case str() (la gravité est un texte) : affichez "Alerte ignoree : gravite recue
en texte ('<gravite>')".
 case _ (tout autre type) : affichez "Alerte ignoree : type de gravite non
reconnu".
"""
alertes = [
    (5, True, False),
    ("2", True, False),
    (4, False, False),
    (3, True, True),
    (-1, True, False),
]

print(15*"*")
import time
for gravite, service_actif, en_maintenance in alertes:
    # etape 1 : c'est le timeur
    time.sleep(4)
    
    # etape 2 : c'est l'affichage des element avec le contenu
    print(f"gravité : {gravite}, service_actif: {service_actif}, maintenance : {en_maintenance}")
    
    # etape 3 : une ligne de séparation
    print(20*"-")
    
    # etape 4 : c'est la structure match - case ==> pour tester la gravité
    match(gravite):
        case int() if gravite >= 1 and gravite <= 5 :
            print("la gravité est valide")
            # question 2 : test de maintenance (True / False)
            if en_maintenance:
                print(f"Alerte (gravite=<{gravite}>) -> suspendue (maintenance en cours)")
        case int():
            print(f"Alerte ignoree : gravite <{gravite}> hors plage (1-5)")
        case str():
            print(f"Alerte ignoree : gravite recue en texte ('<{gravite}>')")
        case _:
            print(f"Alerte ignoree : type de gravite <{gravite}> non econnu")
        
