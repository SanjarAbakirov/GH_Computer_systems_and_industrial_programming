import socket
import time

SERVER = "192.168.31.127"


def simple_test():
    print("Testing connection to server...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)

    try:
        # Подключаемся к серверу
        client.connect(('localhost', 5050))
        client.server = "192.168.31.127"
        print("✓ Connected to server!")

        # Отправляем ПРАВИЛЬНЫЙ HTTP запрос
        # ВАЖНО: Две пустые строки в конце!
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: localhost:5050\r\n"
            "User-Agent: TestClient/1.0\r\n"
            "Accept: text/html,application/json\r\n"
            "Connection: close\r\n"
            "\r\n"  # КРИТИЧЕСКИ ВАЖНО: пустая строка - конец headers
        )

        print("Sending request...")
        client.send(request.encode())

        # Даем время серверу обработать
        time.sleep(0.1)

        # Получаем ответ
        print("Waiting for response...")
        response = b""
        try:
            # Читаем данные пока они есть
            client.settimeout(2)
            while True:
                chunk = client.recv(1024)
                if not chunk:
                    break
                response += chunk
        except socket.timeout:
            pass  # Все данные получены

        response_str = response.decode('utf-8', errors='ignore')

        print("\n" + "="*50)
        print("SERVER RESPONSE:")
        print("="*50)

        if response_str:
            # Разделяем headers и body
            parts = response_str.split('\r\n\r\n', 1)
            if len(parts) >= 1:
                headers = parts[0]
                print("Headers:")
                print("-"*30)
                for line in headers.split('\r\n'):
                    print(line)

            if len(parts) >= 2:
                body = parts[1]
                print("\nBody (first 300 chars):")
                print("-"*30)
                print(body[:300])
                if len(body) > 300:
                    print("... [truncated]")
        else:
            print("No response received!")

        print("="*50)

    except ConnectionRefusedError:
        print("\n✗ Connection refused!")
        print("Possible reasons:")
        print("1. Server is not running")
        print("2. Server is on different port")
        print("3. Firewall is blocking connection")

        # Проверяем, слушает ли что-то порт 5050
        print("\nChecking port 5050...")
        try:
            test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            test_socket.settimeout(1)
            result = test_socket.connect_ex(('localhost', 5050))
            if result == 0:
                print("Port 5050 is open but connection refused")
            else:
                print(f"Port 5050 is closed (error code: {result})")
            test_socket.close()
        except:
            pass

    except socket.timeout:
        print("✗ Connection timeout")
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        client.close()
        print("\nConnection closed.")


def check_server():
    """Простая проверка доступности сервера"""
    print("=== Server Check ===")

    # Пробуем разные хосты
    hosts = ['localhost', '127.0.0.1']

    for host in hosts:
        print(f"\nTrying {host}:5050...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        try:
            result = sock.connect_ex((host, 5050))
            if result == 0:
                print(f"✓ {host}:5050 is OPEN")
                sock.close()
                return host
            else:
                print(f"✗ {host}:5050 is CLOSED (error: {result})")
        except Exception as e:
            print(f"✗ Error checking {host}: {e}")
        finally:
            sock.close()

    return None


if __name__ == "__main__":
    print("="*60)
    print("HTTP CLIENT TEST")
    print("="*60)

    # Сначала проверяем сервер
    available_host = check_server()

    if available_host:
        print(f"\n✓ Server found at {available_host}:5050")
        print("Running full test...")
        # Меняем хост на найденный
        import sys
        if available_host != 'localhost':
            print(f"Note: Using {available_host} instead of localhost")
    else:
        print("\n✗ No server found on port 5050")
        print("\nPlease start the server first:")
        print("1. Open a NEW terminal window")
        print("2. Run: python server.py")
        print("3. Wait for message: 'Server is listening on...'")
        print("4. Then run this client again")

        # Спрашиваем, хочет ли пользователь продолжить
        choice = input("\nTry anyway? (y/n): ").lower()
        if choice != 'y':
            exit()

    simple_test()
