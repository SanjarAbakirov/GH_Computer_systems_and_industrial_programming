import socket


def simple_test():
    print("Testing connection to server...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(3)

    try:
        client.connect(('localhost', 5050))
        print("✓ Connected to server!")

        request = (
            "GET / HTTP/1.1\r\n"
            "Host: localhost:5050\r\n"
            "Connection: close\r\n"
            "\r\n"
        )

        client.send(request.encode())

        response = client.recv(4096).decode()

        print("\nServer response:")
        print("-" * 40)

        lines = response.split('\r\n')
        if lines:
            print(f"Status: {lines[0]}")

        if '\r\n\r\n' in response:
            body = response.split('\r\n\r\n')[1]
            print(f"\nBody (first 200 chars):")
            print(body[:200] + ("..." if len(body) > 200 else ""))
        print("-" * 40)

    except ConnectionRefusedError:
        print("Error. Cannot connect to server")
    except socket.timeout:
        print("Connection timeout")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    simple_test()
