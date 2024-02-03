import socket

class Server:

    def __init__(self, _port, _ip, name: str = "host"):
        # Infos
        self.port = _port
        self.ip = _ip
        self.addr = (self.ip, self.port)
        self.name = name
        self.listened = 5  # Listening count

        # Objects
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        """
        Start the server
        """
        self.socket.bind(self.addr)  # Liaison du serveur à un addresse
        self.socket.listen(self.listened)  # ecoute

    def wait_connection(self):
        """
        Waiting for connection and return connection's infos

        :return:
        tuple: (client_socket, client_address)

        """
        client_socket, client_address = self.socket.accept()
        return client_socket, client_address

    def send_tosocket(self, _socket, _content: str):
        """
        Send data to a client socket

        :param _socket: the socket of target client
        :param _content: the data to send
        :return: none
        """
        _socket.send(_content.encode("utf-8"))

    def close_socket(self, _socket: socket.socket):
        """
        Close the given socket

        :param _socket: socket to close
        :return: none
        """
        _socket.close()


# Example of usage
if __name__ == "__main__":
    server = Server(12345, "127.0.0.1")  # instance creation

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

