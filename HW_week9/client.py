import requests
import json


def test_api():
    base_url = "http://localhost:5050"

    try:
        # Тест главной страницы
        print("1. Testing home page:")
        response = requests.get(base_url + "/")
        print(f"Status: {response.status_code}")

        # Тест статуса сервера
        print("\n2. Testing status page:")
        response = requests.get(base_url + "/status")
        print(f"Status: {response.status_code}")

        # Тест информации API
        print("\n3. Testing API info:")
        response = requests.get(base_url + "/api/info")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

        # Тест получения пользователей
        print("\n4. Testing GET /api/users:")
        response = requests.get(base_url + "/api/users")
        print(f"Status: {response.status_code}")
        print(f"Users: {response.json()}")

        # Тест создания пользователя
        print("\n5. Testing POST /api/users:")
        new_user = {
            "name": "Alice Johnson",
            "email": "alice@example.com"
        }
        response = requests.post(
            base_url + "/api/users",
            json=new_user,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

        # Тест получения конкретного пользователя
        print("\n6. Testing GET /api/users with ID:")
        response = requests.get(base_url + "/api/users?id=1")
        print(f"Status: {response.status_code}")
        print(f"User: {response.json()}")

    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_api()
