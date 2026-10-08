"""Modele de base pour gérer les services réseau."""


class Service:
    """Classe représentant un service réseau."""
    
    def __init__(self, nom, port, protocole):
        self.nom = nom
        self.port = port
        self.protocole = protocole
        self.actif = False
        
    def demarrer(self):
        if not self.actif:
            self.actif = True
            print(f"Service {self.nom} démarré sur le port {self.port} ({self.protocole})")
        else:
            print(f"Service {self.nom} est déjà actif.")
    
    def arreter(self):
        if self.actif:
            self.actif = False
            print(f"Service {self.nom} arrêté.")
        else:
            print(f"Service {self.nom} est déjà inactif.")
            
    def redemarrer(self):
        print(f"Redémarrage du service {self.nom}...")
        self.arreter()
        self.demarrer()
    
    def __str__(self):
        return f"Service {self.nom} (port: {self.port}, protocole: {self.protocole})"

    def __repr__(self):
        return f"Service(nom={self.nom}, port={self.port}, protocole={self.protocole})"


if __name__ == "__main__":
    ssh = Service("SSH", 22, "TCP")
    print(ssh)

    ssh.demarrer()
    ssh.demarrer()

    print(ssh)
    print(repr(ssh))

    type_services = {
                    "dns": (53, "UDP"),
                    "http": (80, "TCP"),
                    "https": (443, "TCP"),
                    "ftp": (21, "TCP"),
                    "smtp": (25, "TCP"),
                    "pop3": (110, "TCP"),
                    "imap": (143, "TCP"),
                    "telnet": (23, "TCP"),
                    "snmp": (161, "UDP"),
                    "ntp": (123, "UDP"),
                    "ldap": (389, "TCP"),
                    "rdp": (3389, "TCP"),
                    "mysql": (3306, "TCP"),
                    "postgresql": (5432, "TCP"),
                    "mongodb": (27017, "TCP"),
                    "redis": (6379, "TCP"),
                    "memcached": (11211, "TCP"),
                    "docker": (2375, "TCP"),
                    "kubernetes": (6443, "TCP"),
                    "rabbitmq": (5672, "TCP"),
                    "elasticsearch": (9200, "TCP"),
                    "kafka": (9092, "TCP"),
                    "zookeeper": (2181, "TCP"),
                    "cassandra": (9042, "TCP"),
                    "hadoop": (50070, "TCP"),
                    "spark": (7077, "TCP"),
                    "jenkins": (8080, "TCP"),
                    "gitlab": (80, "TCP"),
                    "jira": (8080, "TCP"),
                    "confluence": (8090, "TCP"),
                    "grafana": (3000, "TCP"),
                    "prometheus": (9090, "TCP"),
                    "vault": (8200, "TCP"),
                    "consul": (8500, "TCP"),
                    "traefik": (8080, "TCP"),
                    "haproxy": (80, "TCP"),
                    "nginx": (80, "TCP"),
                    "apache": (80, "TCP"),
                    "varnish": (6081, "TCP"),
                    "samba": (445, "TCP"),
                    "nfs": (2049, "TCP"),
                    "iscsi": (3260, "TCP"),
                    "vpn": (1194, "UDP"),
                    "openvpn": (1194, "UDP"),
                    "wireguard": (51820, "UDP"),
                    "ipsec": (500, "UDP"),
                    "pptp": (1723, "TCP"),
                    "l2tp": (1701, "UDP"),
                    "sftp": (22, "TCP"),
                    "rsync": (873, "TCP")}

    liste_services = []

    for nom, (port, protocole) in type_services.items():
        service = Service(nom, port, protocole)
        liste_services.append(service)


    print(f"Liste des services ({len(liste_services)}):")
    print(20 * "= *")
    import time
    for service in liste_services:
        time.sleep(0.1)
        print(20 * "-")
        print(service)
    
    print(type(ssh))
    
    print(isinstance(ssh, Service))
    
    liste_test = [("DNS", 53, "UDP"), ("HTTPS", 443, "TCP"), ("FTP", 21, "TCP"), ("NTP", 123, "UDP")]
    service_tcp = []
    
    """Affichez-les numérotés (enumerate(..., 1)), puis construisez avec une compréhension de liste la sous-liste des services en
    "TCP" et affichez son nombre d'éléments."""
    
    for index, (nom, port, protocole) in enumerate(liste_test, 1):
        print(f"{index}. {Service(nom, port, protocole)}")
        if protocole == "TCP":
            service_tcp.append((nom, port, protocole))


    print(f"Nombre de services en TCP: {len(service_tcp)}")
