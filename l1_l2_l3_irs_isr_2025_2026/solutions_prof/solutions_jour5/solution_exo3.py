"""Scan de ports avec arrêt anticipé et filtrage

    Contexte : 
        Un scanner de sécurité doit parcourir une liste de ports brutsc continue (sans exécuter le reste du corps
de la boucle pour ce port).
2. Si le port fait partie de ports_watchlist, utilisez pass : c'est un traitement spécifique
pas encore implémenté, qui ne doit (parfois invalides),
        ignorer certains ports "en watchlist" dont le traitement spécifique n'est pas encore 
        implémenté, et s'arrêter dès qu'il détecte le port SSH (22) ouvert.
"""

ports_watchlist = {3389}
ports_a_scanner = [0, 80, -5, 443, 3389, 99999, 22, 8080]

for port in ports_a_scanner:
    if port <= 0 or port > 65535:
        print(f"Port {port} : invalide, ignore")
        continue
        
    if port in ports_watchlist:
        pass
    
    if port == 22:
        print(f"Port {port} (SSH) :Trouvé, arrêt du scan.")
        break
    
    print(f"Port {port} : scanné, rien de particulier a signaler.")
    
print("San terminé ou interrompu.")