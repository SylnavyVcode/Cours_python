"""
Simulateur de ping avec abandon après N tentatives

    Contexte. 
        Un script de supervision teste la joignabilité de plusieurs hôtes par une série de
        tentatives de ping simulées (chaque tentative renvoie True en cas de succès, False en cas
        d'échec). Il doit abandonner après un nombre maximum de tentatives si aucune n'a réussi,
        et s'arrêter dès la première réussite.
"""

max_tentatives = 4
hotes = {
    "srv-web": [False, False, True, False],
    "srv-db": [False, False, False, False],
}

for hote, tentatives in hotes.items():
    print(f"- - - Ping vers {hote} - - -")
    tentative = 0
    succes = False
    
    while tentative < max_tentatives:
        if tentatives[tentative]:
            succes = True
            print(f"Tentative <{tentative+1}>/<{max_tentatives}> : <{'succes' if tentatives[tentative] else 'echec'}>")
            break
        else:
            print(f"Tentative <{tentative+1}>/<{max_tentatives}> : <{'succes' if tentatives[tentative] else 'echec'}>")
        tentative += 1
    
    if tentative == max_tentatives:
        print(f"{hote} : injoignable apres {max_tentatives} tentatives, abandon.")
    else:
        print(f"{hote} : joignable (en {tentative} tentative(s)).")