import socket

PORT = 2405


def main():
    # create socket → bind → recvfrom → sendto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", PORT))
        while True:
            data, addr = s.recvfrom(1024)
            s.sendto(data[::-1], addr)


if __name__ == "__main__":
    main()
