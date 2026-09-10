"""
Module outils_reseau - cas concret TGSSI.
S'appuie sur le module STANDARD "ipaddress" (aucune dependance externe).
"""
import ipaddress

PORTS_STANDARDS = {
22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
80: "HTTP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP",
}

def valider_ip(ip: str) -> bool:
    """Retourne True si 'ip' est une adresse IPv4/IPv6 valide."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
    
def meme_reseau(ip1: str, ip2: str, masque_cidr: str) -> bool:
    """Verifie si deux IP appartiennent au meme reseau (ex: '192.168.1.0/24')."""
    reseau = ipaddress.ip_network(masque_cidr, strict=False)
    return ipaddress.ip_address(ip1) in reseau and ipaddress.ip_address(ip2) in reseau
def adresse_reseau(ip_cidr: str) -> str:
    """Adresse reseau d'un CIDR. Ex: '192.168.1.10/24' -> '192.168.1.0'."""
    reseau = ipaddress.ip_network(ip_cidr, strict=False)
    return str(reseau.network_address)
def adresse_broadcast(ip_cidr: str) -> str:
    """Adresse de broadcast d'un CIDR IPv4."""
    reseau = ipaddress.ip_network(ip_cidr, strict=False)
    return str(reseau.broadcast_address)
def nom_service(port: int) -> str:
    """Nom du service standard associe a un port, ou 'inconnu'."""
    return PORTS_STANDARDS.get(port, "inconnu")