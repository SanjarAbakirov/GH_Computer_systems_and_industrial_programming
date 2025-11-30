import socket

HEADER = 64  # 64 TELLS message that is going to come next
PORT = 5050
FORMAT = 'utf-8'
DISCONECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.31.127"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("The World! is the best")
input()
send("Please push Enter btn")
input()
send("Hello Sam")

send(DISCONECT_MESSAGE)


# slamadashoo


def greet_user():
    """Алгоритм приветствия пользователя"""

    # Запрашиваем имя
    name = input("Пожалуйста, введите ваше имя: ").strip()

    # Проверяем, что имя не пустое
    while not name:
        print("Имя не может быть пустым!")
        name = input("Пожалуйста, введите ваше имя: ").strip()

    # Запрашиваем дополнительную информацию
    print(f"Привет, {name}!")

    mood = input("Как у вас дела сегодня? ").strip()

    # Формируем ответ в зависимости от настроения
    if any(word in mood.lower() for word in ['хорошо', 'отлично', 'прекрасно', 'замечательно']):
        print("Рад слышать, что у вас всё хорошо! 😊")
    elif any(word in mood.lower() for word in ['плохо', 'ужасно', 'грустно', 'скучно']):
        print("Надеюсь, ваш день станет лучше!")
    else:
        print("Спасибо, что поделились!")

    print(f"Хорошего дня, {name}!")


# Запускаем функцию
greet_user()
