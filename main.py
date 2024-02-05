from client.client import Server as Client_server
from server.server import Server as Server_server

if __name__ == "__main__":
    server_choice = input("Welcome !!\nYou want to be a server or a client ? (0 a server/1 b client): ")
    name = input("Your nick name: ")

    ip = "localhost"
    port = 7777
    ip_adress = input(f"Enter your server's adress (may be your {ip}): ")
    port_adress = input(f"Enter teh port (may be {port}): ")

    if ip_adress != "": ip = ip_adress
    if port_adress != "": port = int(port_adress)

    if server_choice in ["0", "a", "server", "s"]:

        server = Server_server(port, ip, name)
        # Starting the server
        server.run()
        print(f"The server is listening on {server.ip}:{server.port}")

        # Waiting for connection
        client_socket, client_address = server.wait_connection()
        print(f"Connexion established to {client_address}")

        # Sending data to the connected client
        message = "Welcome to the server!"
        client_socket.send(message.encode('utf-8'))

        # Closing sockets
        server.close_socket(client_socket)
        server.close_socket(server.socket)
        print("Server closed.")
    if server_choice in "1 b client s".split(' '):
        client = Client_server(port, ip)  # instance creation

        # Connecting to the server
        client.connect()
        print(f"Connected to the server at {client.ip}:{client.port}")

        # Receiving data from the server
        data = client.get_data()
        print(f"Received message from the server : {data.decode('utf-8')}")

        # Closing sockets
        client.close_socket(client.socket)
        print("Connection closed.")
