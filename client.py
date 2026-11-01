import socket
import sys

HOST = "127.0.0.1"
PORT = 2405


def main():
    message = sys.argv[1] if len(sys.argv) > 1 else "meow"
    # create socket → connect → send → recv
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(message.encode())
        print(s.recv(1024).decode())


if __name__ == "__main__":
    main()
