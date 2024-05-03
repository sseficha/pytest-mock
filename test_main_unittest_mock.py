from unittest.mock import patch, Mock

from main import get_welcome_message


@patch("main.is_user_barney", return_value=False)
@patch("main.date")
@patch("main.requests")
def test_get_welcome_message(requests_mock, date_mock, _, username_fixture):
    requests_mock.get.return_value = Mock(
        **{
            "status_code": 200,
            "json.return_value": {
                "status_code": 200,
                "data": {"username": username_fixture},
            },
        }
    )

    date_mock.today.return_value = "1980-01-01"

    assert get_welcome_message() == "Hello Barney the date is 1980-01-01"
