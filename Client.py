import socket


def send_command(host, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(command.encode())
    client_socket.close()


if __name__ == "__main__":
    host = '172.24.96.1'  # Replace with the IP address of the server
    port = 9999  # Replace with the port number used by the server

    while True:
        command = input("Enter a command (x,y for mouse movement, L for left click, or text for keyboard input): ")
        if command.lower() == 'exit':
            break
        send_command(host, port, command)

# For any Help! Please Send me Email Ashik@Spudblocks.com
