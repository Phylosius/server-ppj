
# Importation du module socket
import socket

# Création d'un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du serveur à une adresse et un port
adresse_serveur = ('127.0.0.1', 12345)
serveur_socket.bind(adresse_serveur)

# Mise en écoute du serveur (accepte jusqu'à 5 connexions en attente)
serveur_socket.listen(5)
print(f"Le serveur écoute sur {adresse_serveur[0]}:{adresse_serveur[1]}")

# Attente de la connexion d'un client
client_socket, client_address = serveur_socket.accept()
print(f"Connexion établie avec {client_address}")

# Envoi de données au client
message = "Bienvenue sur le serveur!"
client_socket.send(message.encode('utf-8'))

# Fermeture des sockets
client_socket.close()
serveur_socket.close()

