import pprint
import socket
import ssl

html = b"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: 59\r\n\r\n<!DOCTYPE html><html><body><h1>This is Bank32.com!</h1></body></html>"""

SERVER_CERT = "./cert.pem"
SERVER_PRIVATE = "./key.pem"

# Set up the TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(SERVER_CERT, SERVER_PRIVATE)

# Set up the TCP server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Using a non-privileged port (e.g., 4433) avoids permission errors on local testing
sock.bind(("127.0.0.1", 433))
sock.listen(5)

print("TLS Server running on port 433...")

while True:
    newsock, fromaddr = sock.accept()
    ssock = None
    try:
        # Bind the TLS layer to the TCP connection
        ssock = context.wrap_socket(newsock, server_side=True)
        print(f"TLS connection established with {fromaddr}")

        data = ssock.recv(1024)  # Read data over TLS
        pprint.pprint(f"Request: {data.decode('utf-8', errors='ignore')}")
        ssock.sendall(html)  # Send data over TLS

    except Exception as e:  # noqa: BLE001
        print(f"TLS connection fails: {e}")
    finally:
        # Safely close the TLS/TCP socket if it was successfully wrapped
        if ssock:
            try:
                ssock.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            ssock.close()
        else:
            newsock.close()
