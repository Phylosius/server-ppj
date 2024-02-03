import socket


class Server:

    def __init__(self, _port, host_ip, name: str = "guest"):
        # Infos
        self.port = _port
        self.ip = host_ip
        self.addr = (self.ip, self.port)
        self.name = name

        # Objects
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connect to host the server
        """
        self.socket.connect(self.addr)  # connecting to the host

    def get_data(self):
        """
        return received data
        :return: str
        """
        return self.socket.recv(1024)

    def send_tosocket(self, _socket, _content: str):
        """
        Send data to a socket

        :param _socket: the socket of the target
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
    client = Server(12345, "127.0.0.1")  # instance creation

    # Connecting to the server
    client.connect()
    print(f"Connected to the server at {client.ip}:{client.port}")

    # Receiving data from the server
    data = client.get_data()
    print(f"Received message from the server : {data.decode('utf-8')}")

    # Closing sockets
    client.close_socket(client.socket)
    print("Connection closed.")
