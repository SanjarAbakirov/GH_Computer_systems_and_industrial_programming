# client_multiple_messages.py
import socket

HOST = '192.168.31.13'
PORT = 9090


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Подключен к {HOST}:{PORT}")
        print("Введите 'exit' для выхода")

        while True:
            # Получаем сообщение от пользователя
            message = input("Ваше сообщение: ")

            if message.lower() == 'exit':
                print("Завершение работы...")
                break

            # Отправляем сообщение серверу
            client.send(message.encode('utf-8'))

            # Получаем ответ от сервера
            response = client.recv(1024).decode('utf-8')
            print(f"Сервер ответил: {response}")

    except ConnectionRefusedError:
        print(f"Сервер {HOST}:{PORT} недоступен")
    except KeyboardInterrupt:
        print("\nПрервано пользователем")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        client.close()
        print("Соединение закрыто")


if __name__ == "__main__":
    main()
