import socket
import pyautogui
import keyboard

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port", port)
    conn, addr = server_socket.accept()
    print("Connected to:", addr)

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            if ',' in data:
                x, y, *button = data.split(',')
                pyautogui.moveTo(int(x), int(y))
                if button and button[0] == 'L':
                    pyautogui.click()
            else:
                keyboard.write(data)
        except Exception as e:
            print("Error:", e)
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    host = '172.24.96.1'  # Bind to all available network interfaces
    port = 9999  # Choose an available port
    start_server(host, port)
