import pytest

from main import get_welcome_message


@pytest.fixture(autouse=True)
def reusable_mock(mocker, username_fixture):
    requests_mock = mocker.patch("main.requests")
    requests_mock.get.return_value = mocker.Mock(
        **{
            "status_code": 200,
            "json.return_value": {
                "status_code": 200,
                "data": {"username": username_fixture},
            },
        }
    )

    date_mock = mocker.patch("main.date")
    date_mock.today.return_value = "1980-01-01"


def test_get_welcome_message(mocker):
    mocker.patch("main.is_user_barney", return_value=False)

    assert get_welcome_message() == "Hello Barney the date is 1980-01-01"


def test_get_welcome_message_barney_error():
    with pytest.raises(ValueError):
        get_welcome_message()
