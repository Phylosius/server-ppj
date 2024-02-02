
# Importation du module socket
import socket

# Création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Définition de l'adresse du serveur auquel se connecter
serveur_address = ('127.0.0.1', 12345)

# Connexion au serveur
client_socket.connect(serveur_address)
print(f"Connecté au serveur sur {serveur_address[0]}:{serveur_address[1]}")

# Réception des données du serveur
donnees_recues = client_socket.recv(1024)
print(f"Message reçu du serveur : {donnees_recues.decode('utf-8')}")

# Fermeture du socket client
client_socket.close()
