from datetime import date
import requests
from requests import RequestException


def is_user_barney(username):
    return username == "Barney"


def get_welcome_message():
    current_date = date.today()
    response = requests.get("dummy_url")
    if response.status_code != 200:
        raise RequestException("Error fetching username")
    username = response.json()["data"]["username"]
    if is_user_barney(username):
        raise ValueError("We don't say hi to Barney")
    return f"Hello {username} the date is {current_date}"


if __name__ == "__main__":
    print(get_welcome_message())
