from main import get_welcome_message


def test_get_welcome_message(mocker, username_fixture):
    # Arrange
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

    mocker.patch("main.is_user_barney", return_value=False)

    # Act
    message = get_welcome_message()

    # Assert
    assert message == "Hello Barney the date is 1980-01-01"
